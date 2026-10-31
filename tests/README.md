# Integration tests

CI checks both templates on pushes and pull requests to their development
branches and `main`. It also runs weekly and can be started manually on `main`.
It renders projects, executes notebooks, verifies editable imports and source-layout
paths, and checks that package archives exclude study files. Tests also cover
custom names, metadata escaping, and optional `AGENTS.md` guidance.

The test runner uses Python 3.11; generated projects are built, installed, and
executed in fresh environments using Python 3.8, 3.11, 3.13, and 3.14 on Ubuntu
24.04. This does not establish Windows or every intermediate Python version's
compatibility. Source templates and their notebook outputs are never modified.

<details>
<summary>Run tests locally</summary>

From the repository root, on Linux or macOS, use Python 3.11.4 or newer and
network access to install dependencies. Make sure `python` selects that version:

```bash
python -m venv /tmp/data-science-project-tests
/tmp/data-science-project-tests/bin/python -m pip install -r tests/requirements.txt
/tmp/data-science-project-tests/bin/python -m pytest -v tests
```

Tests use local `origin/*` refs for the two template branches, falling back to
local branches if a remote ref is absent. Run `git fetch origin` first to test
the latest remote commits.

To use another Python for generated projects:

```bash
PROJECT_TEST_PYTHON=/absolute/path/to/python3.8 /tmp/data-science-project-tests/bin/python -m pytest -v tests
```

The test runner still requires Python 3.11.4 or newer. `PROJECT_TEST_PYTHON`
controls only generated projects' environments and builds; when unset, they
use the test runner's Python.

</details>

<details>
<summary>Test uncommitted templates and work across branches</summary>

The two independent template branches are `installable_imrad_project_cookiecutter`
and `imrad_project_cookiecutter`. They are not feature branches to merge into
`main`, which holds shared documentation and tests.

To test uncommitted work, set `PROJECT_TEST_SOURCES` to a directory containing
one subdirectory or symlink per template, named exactly like its branch:

```bash
PROJECT_TEST_SOURCES=/absolute/path/to/template-sources /tmp/data-science-project-tests/bin/python -m pytest -v tests
```

Create the test environment using the local instructions above first. Sources
are copied to temporary directories before testing.

When checking out local template branches, configure tracking:

```bash
git branch --set-upstream-to=origin/installable_imrad_project_cookiecutter installable_imrad_project_cookiecutter
git branch --set-upstream-to=origin/imrad_project_cookiecutter imrad_project_cookiecutter
```

A push from `main` does not push the template branches. For coordinated changes:

```bash
git push origin main installable_imrad_project_cookiecutter imrad_project_cookiecutter
```

Template branches call the shared workflow on `main`. Their runs test the
triggering event's exact commit and the current other template branch, logging
both source commit IDs. Push shared workflow changes to `main` before updating
its callers on the template branches.

</details>

<details>
<summary>Test release 1.0.1</summary>

In a separate clone, run the following from the repository root on Linux or
macOS, with `python` selecting Python 3.11.4 or newer. The release dependency file is `tests/requirements.txt`.

```bash
git fetch origin --tags
git checkout v1.0.1
python -m venv /tmp/data-science-project-release-tests
/tmp/data-science-project-release-tests/bin/python -m pip install -r tests/requirements.txt
release_sources=$(mktemp -d)
mkdir "$release_sources/installable_imrad_project_cookiecutter" "$release_sources/imrad_project_cookiecutter"
git archive installable-imrad-project-v1.0.1 | tar -x -C "$release_sources/installable_imrad_project_cookiecutter"
git archive imrad-project-v1.0.1 | tar -x -C "$release_sources/imrad_project_cookiecutter"
PROJECT_TEST_SOURCES="$release_sources" /tmp/data-science-project-release-tests/bin/python -m pytest -v tests
```

Dependencies are resolved at test time; the release does not include a lockfile
for third-party packages.

</details>
