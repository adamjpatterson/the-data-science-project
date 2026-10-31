"""Integration checks for the repository's two Cookiecutter templates."""
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tomllib
import zipfile

import pytest
from cookiecutter.main import cookiecutter

REPO = Path(__file__).resolve().parents[1]
BRANCHES = (
    "installable_imrad_project_cookiecutter",
    "imrad_project_cookiecutter",
)


def run(*args, cwd, env=None):
    result = subprocess.run(
        [str(arg) for arg in args], cwd=cwd, env=env,
        text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=300,
    )
    assert result.returncode == 0, result.stdout
    return result.stdout


@pytest.fixture(scope="session")
def sources(tmp_path_factory):
    """Use explicit working copies when supplied; otherwise export Git refs."""
    root = tmp_path_factory.mktemp("branches")
    override = os.environ.get("PROJECT_TEST_SOURCES")
    for branch in BRANCHES:
        target = root / branch
        if override:
            source = Path(override) / branch
            assert source.is_dir(), f"Missing branch source: {source}"
            shutil.copytree(source, target, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        else:
            ref = f"refs/remotes/origin/{branch}"
            if subprocess.run(["git", "rev-parse", "--verify", ref], cwd=REPO,
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode:
                ref = f"refs/heads/{branch}"
            archive = root / f"{branch}.tar"
            run("git", "archive", "--output", archive, ref, cwd=REPO)
            target.mkdir()
            with tarfile.open(archive) as stream:
                stream.extractall(target, filter="data")
    return root


def render(sources, tmp_path, branch, custom, extra_context=None):
    context = {"project_name": "custom-project"} if custom else {}
    if custom and branch == "installable_imrad_project_cookiecutter":
        context.update({
            "package_name": "custom_package",
            "package_description": 'A "quoted" study using C:\\data',
            "author_name": 'Alice "AJ" Jones',
        })
    context.update(extra_context or {})
    project = Path(cookiecutter(
        str(sources / branch), no_input=True, extra_context=context,
        output_dir=str(tmp_path),
        default_config={"replay_dir": str(tmp_path / "replay"),
                        "cookiecutters_dir": str(tmp_path / "cookiecutters")},
    ))
    assert project.name == ("custom-project" if custom else "project")
    assert (project / "AGENTS.md").is_file() == (context.get("include_agents_md", "yes") == "yes")
    for path in project.rglob("*"):
        assert "{{" not in str(path.relative_to(project))
        if path.is_file():
            assert b"{{cookiecutter." not in path.read_bytes(), path
    return project, "custom_package" if custom else "package"


def environment(tmp_path):
    root = tmp_path / "venv"
    target = os.environ.get("PROJECT_TEST_PYTHON", sys.executable)
    run(target, "-m", "venv", root, cwd=tmp_path)
    python = root / "bin/python"
    env = dict(os.environ)
    env.pop("PYTHONPATH", None)
    env.pop("PYTHONHOME", None)
    env["PATH"] = f"{root / 'bin'}{os.pathsep}{env.get('PATH', '')}"
    env["JUPYTER_PATH"] = str(root / "share/jupyter")
    env["JUPYTER_CONFIG_DIR"] = str(tmp_path / "jupyter-config")
    env["IPYTHONDIR"] = str(tmp_path / "ipython")
    return python, env


def install_notebook_tools(python, env, tmp_path, *packages):
    run(python, "-m", "pip", "install", "nbclient", "ipykernel", *packages,
        cwd=tmp_path, env=env)
    run(python, "-m", "ipykernel", "install", "--prefix", python.parent.parent,
        "--name", "python3", cwd=tmp_path, env=env)


def execute_notebook(python, env, notebook, cwd, project):
    checks = f"""
from pathlib import Path
expected_root = Path({str(project.resolve())!r})
assert PROJECT_ROOT == expected_root
assert (MATERIALS_PATH, METHODS_PATH, RESULTS_PATH) == tuple(
    expected_root / name for name in ('materials', 'methods', 'results'))
assert all(p.is_absolute() and p.is_dir() for p in (
    PROJECT_ROOT, MATERIALS_PATH, METHODS_PATH, RESULTS_PATH))
"""
    run(python, "-c", """
import nbformat, sys
from nbclient import NotebookClient
nb = nbformat.read(sys.argv[1], as_version=4)
nb.cells.append(nbformat.v4.new_code_cell(sys.argv[2]))
NotebookClient(nb, timeout=120, kernel_name='python3').execute()
""", notebook, checks, cwd=cwd, env=env)


@pytest.mark.parametrize("custom", [False, True], ids=["defaults", "custom-names"])
def test_imrad_template(sources, tmp_path, custom):
    project, _ = render(sources, tmp_path, "imrad_project_cookiecutter", custom)
    for name in ("materials", "methods", "results"):
        assert (project / name / "README.md").is_file()
    assert (project / "requirements.txt").is_file()
    python, env = environment(tmp_path)
    install_notebook_tools(python, env, tmp_path)
    execute_notebook(
        python, env, project / "methods/main.ipynb", project / "methods",
        project,
    )


def assert_paths(python, env, cwd, package, project, code_dir):
    run(python, "-c", f"""
from pathlib import Path
import sys
import {package}
from {package} import PROJECT_ROOT, MATERIALS_PATH, METHODS_PATH, RESULTS_PATH
root = Path(sys.argv[1]).resolve()
assert PROJECT_ROOT == root
assert (MATERIALS_PATH, METHODS_PATH, RESULTS_PATH) == tuple(root / name for name in ('materials', 'methods', 'results'))
assert Path({package}.__file__).resolve().parent == Path(sys.argv[2]).resolve()
""", project, code_dir, cwd=cwd, env=env)


@pytest.mark.parametrize("variant", ["defaults", "custom-names"])
def test_installable_distribution(sources, tmp_path, variant):
    project, package = render(sources, tmp_path, "installable_imrad_project_cookiecutter",
                              variant == "custom-names")
    stale_wheel = project / "dist/previous-0.0.0-py3-none-any.whl"
    stale_wheel.parent.mkdir()
    stale_wheel.write_bytes(b"previous build artifact")
    for name in ("materials", "methods", "results"):
        assert (project / name / "README.md").is_file()
        assert not (project / name / "__init__.py").exists()
    assert (project / "methods" / package / "__init__.py").is_file()
    study_files = {
        "materials/input.csv": "synthetic input\n",
        "results/output.csv": "synthetic output\n",
        "methods/study-notes.txt": "study notes\n",
        "private-notes.txt": "workspace notes\n",
    }
    for name, content in study_files.items():
        (project / name).write_text(content)
    python, env = environment(tmp_path)
    run(python, "-m", "pip", "install", "build>=1.2,<2", cwd=tmp_path, env=env)
    # Build the wheel from the sdist using the target Python version.
    distributions = tmp_path / "distributions"
    run(python, "-m", "build", "--outdir", distributions, project, cwd=tmp_path, env=env)
    sdist, = distributions.glob("*.tar.gz")
    with tarfile.open(sdist) as archive:
        names = {"/".join(Path(member.name).parts[1:])
                 for member in archive.getmembers() if member.isfile()}
        assert {"pyproject.toml", "README.md", "__about__.py", "PKG-INFO"} <= names
        assert f"methods/{package}/__init__.py" in names
        # Hatchling also preserves .gitignore to reproduce file selection.
        assert all(name in {"pyproject.toml", "README.md", "__about__.py", "PKG-INFO", ".gitignore"}
                   or name.startswith(f"methods/{package}/") for name in names), names
    for name, content in study_files.items():
        assert (project / name).read_text() == content
    wheel, = distributions.glob("*.whl")
    assert stale_wheel.read_bytes() == b"previous build artifact"
    with zipfile.ZipFile(wheel) as archive:
        names = archive.namelist()
        assert f"{package}/__init__.py" in names
        assert f"{package}/__main__.py" in names
        assert all(name.startswith((package + "/",)) or ".dist-info/" in name for name in names)
        assert not any(name.endswith((".ipynb", ".pkl", ".data")) for name in names)
        assert not any(name.startswith(f"{package}/{section}/") for name in names
                       for section in ("materials", "methods", "results"))
    # Readers clone the complete study and install its package in editable mode.
    install_notebook_tools(python, env, tmp_path)
    run(python, "-m", "pip", "install", "--editable", project, cwd=tmp_path, env=env)
    outside = tmp_path / "outside"
    outside.mkdir()
    source_code = project / "methods" / package
    assert_paths(python, env, outside, package, project, source_code)
    # A utility added by the study author is importable without path manipulation.
    (source_code / "utils.py").write_text("def double(value):\n    return value * 2\n")
    run(python, "-c", f"from {package} import utils; assert utils.double(21) == 42",
        cwd=outside, env=env)
    execute_notebook(python, env, project / "methods/main.ipynb", outside, project)
    assert run(python, "-m", package, cwd=outside, env=env) == ""


@pytest.mark.parametrize("value", [
    'A "quoted" value',
    r"C:\new\trials",
    "First line\nSecond line\tRésumé 🧪",
], ids=["quotes", "backslashes", "multiline-unicode"])
def test_template_metadata_round_trip(sources, tmp_path, value):
    context = dict.fromkeys(
        ("author_name", "author_email", "package_description", "repository_url"), value,
    )
    project, _ = render(sources, tmp_path, "installable_imrad_project_cookiecutter", False, context)
    metadata = tomllib.loads((project / "pyproject.toml").read_text())["project"]
    assert metadata["authors"] == [{"name": value, "email": value}]
    assert metadata["description"] == value
    assert metadata["urls"] == {"Homepage": value, "Issues": value + "/issues"}


@pytest.mark.parametrize("branch", BRANCHES)
def test_optional_agents_guidance(sources, tmp_path, branch):
    included, package = render(sources, tmp_path / "included", branch, True,
                               {"include_agents_md": "yes"})
    omitted, _ = render(sources, tmp_path / "omitted", branch, True,
                        {"include_agents_md": "no"})
    guidance = (included / "AGENTS.md").read_text()
    if branch == "installable_imrad_project_cookiecutter":
        assert f"methods/{package}/" in guidance
        assert f"`{package}`" in guidance
        assert f"python -m {package}" in guidance
    else:
        assert "methods/main.ipynb" in guidance
    # Opting out must remove only the guidance, preserving all other files.
    def files(root):
        return {p.relative_to(root): p.read_bytes() for p in root.rglob("*")
                if p.is_file() and p.name != "AGENTS.md"}
    assert not (omitted / "AGENTS.md").exists()
    assert files(included) == files(omitted)
