# The Data Science Project

The [IMRaD](https://en.wikipedia.org/wiki/IMRAD)-like Python project templates for data science projects.

## Introduction

In the data science domain, projects are sometimes shared as an informal assemblage of scripts. This repository proposes two familiar [IMRaD](https://en.wikipedia.org/wiki/IMRAD)-like project templates that can be used for organizing your data science or statistical analysis. This IMRaD-inspired approach is aimed at meeting the requirements of a wide range of data science and statistical applications while still offering a project layout that is immediately recognizable by persons working in the science domains.

This repository provides two [Cookiecutter](https://github.com/cookiecutter/cookiecutter) templates for creating these project layouts:

The [Installable IMRaD-like Project](#an-installable-imrad-like-project) template offers an intuitive and familiar project layout. It organizes your project into `materials`, `methods`, and `results` directories. It adds an installable Python package within `methods`, while keeping `materials` and `results` in the project workspace. You can create an [installable IMRaD-like project](#create-an-installable-imrad-like-project-using-the-cookiecutter) using the Cookiecutter.

The simple [IMRaD-like Project](#an-imrad-like-project) template is an intuitive non-installable Python project organized into `materials`, `methods`, and `results` directories. You can create a non-installable [IMRaD-like project](#create-an-imrad-like-project-using-the-cookiecutter) using the Cookiecutter.

## Table of contents

- [An installable IMRaD-like project](#an-installable-imrad-like-project)
- [An IMRaD-like project](#an-imrad-like-project)
- [Data science and statistical analysis with AI assistance](#data-science-and-statistical-analysis-with-ai-assistance)
- [Release](#release)
- [Development checks](#development-checks)
- [Other solutions](#other-solutions)
- [Support](#support)

## An installable IMRaD-like project

The installable project features `materials`, `methods`, and `results` directories at the project root. Their contents are up to you; no particular data, model, or output subdirectories are specified. This approach accommodates a wide range of data science and statistical applications, while offering an instantly recognizable IMRaD-like project layout.

Use the `materials` directory for source data, intermediary datasets, and models consumed by your analysis. Use the `results` directory for storing the products of your analysis, such as datasets, visualizations, and models. The `methods` directory stores your procedures, including notebooks and the installable package.

### Features

- A familiar [IMRaD](https://en.wikipedia.org/wiki/IMRAD)-like layout.
- An installable Python package (with support for editable installation) that facilitates importing user defined modules and utilities.
- A study repository that can be shared on GitHub and installed in editable mode.
- Simple path constants useful for navigating the project from a notebook.

### Explore the project layout

You can [create an installable project using the Cookiecutter](#create-an-installable-imrad-like-project-using-the-cookiecutter).

#### The directory structure looks like this.

```text
├── project ⬅ This is the project directory. Choose a name for your project.
    │
    ├── AGENTS.md ⬅ Optional guidance for AI assistants working on this study.
    │
    ├── __about__.py
    │
    ├── materials ⬅ Put inputs and supporting materials here; organize them for your study.
    │   │
    │   └── README.md
    │
    ├── methods ⬅ Put your notebooks, reusable Python code, and other methods here.
    │   │
    │   ├── README.md
    │   │
    │   ├── main.ipynb
    │   │
    │   └── package ⬅ This is the Python package. Cookiecutter lets you choose its name.
    │       │
    │       ├── __init__.py ⬅ Import the study's path constants from the package.
    │       │
    │       ├── __main__.py ⬅ Define your package's pipeline here.
    │       │
    │       └── utils.py ⬅ Put reusable Python functions here.
    │
    ├── results ⬅ Put your study's outputs here; organize them for your study.
    │   │
    │   └── README.md
    │
    ├── pyproject.toml ⬅ Configure your package and its dependencies here.
    │
    └── README.md ⬅ Put your Introduction and Discussion here.
```

The default Python package name is `package`. You can specify a different package name using the [Cookiecutter](#create-an-installable-imrad-like-project-using-the-cookiecutter).

### Create an installable IMRaD-like project using the Cookiecutter

Install the Cookiecutter package.

```bash
python -m pip install cookiecutter
```

Use the Cookiecutter to create an installable IMRaD-like project.

```bash
cookiecutter https://github.com/adamjpatterson/the-data-science-project.git --checkout installable-imrad-project-v1.0.0
```

The form lets you configure the project directory, Python package, repository URL, description, and author information:

```text
[1/7] Project directory name (project):
[2/7] Python package name (package):
[3/7] Repository URL (https://github.com/pypa/sampleproject):
[4/7] Package description (A small example package):
[5/7] Author name (Example Author):
[6/7] Author email (author@example.com):
[7/7] Include AGENTS.md guidance?
    1 - yes
    2 - no
    Choose from [1/2] (1):
```

Press Enter to accept each displayed default or enter a custom value. Project directory names may contain dashes, such as `my-study`. Use a valid Python import name for the package, such as `my_study`.

#### Install the package

From the generated project directory, activate your environment and install your package in editable mode. Editable installation lets you change the package code without reinstalling it. Restart the notebook kernel or reload affected modules to use changes to code already imported.

```bash
python -m pip install -e .
```

#### Run a notebook

Open `methods/main.ipynb` in the same environment. Its first cell imports the four path constants and `utils` from your configured package.

#### Add dependencies to your project

Add dependencies to `pyproject.toml` and rerun the installation command when they change. Put reusable functions in your package and import them into notebooks.

### Workspace paths

Editable installation makes the package's utilities and path constants importable without modifying `sys.path` or setting `PYTHONPATH`:

```python
from package import PROJECT_ROOT, MATERIALS_PATH, METHODS_PATH, RESULTS_PATH
from package import utils
```

Replace `package` with your configured package name. The constants in `__init__.py` are simple definitions based on the generated source layout:

```python
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MATERIALS_PATH = PROJECT_ROOT / "materials"
METHODS_PATH = PROJECT_ROOT / "methods"
RESULTS_PATH = PROJECT_ROOT / "results"
```

They work independently of the notebook's current directory. Adapt them if you change the layout. They are intended for editable use within the cloned study.

### Pipeline invocation

You can optionally build a runnable analysis in `__main__.py`. It starts with:

```python
def main():
    # Define your analysis workflow here.
    pass


if __name__ == "__main__":
    main()
```

Run it with `python -m package`, replacing `package` with your configured package name. It does nothing until you add your workflow. Define any arguments your analysis needs. You can extend the pipeline to run notebooks using [Papermill](https://papermill.readthedocs.io/en/latest/).

### Share a study on GitHub

Share the complete study repository, including its code, notebooks, documentation, and shareable data. Document how to obtain any data stored elsewhere and the steps needed to reproduce the analysis.

Readers clone the repository, activate their Python environment, and run `python -m pip install -e .` from the study root. They can then import the package from notebooks and run the analysis steps you have documented.

The project includes a `.gitignore` based on [GitHub’s Python template](https://github.com/github/gitignore/blob/main/Python.gitignore). Use the `.gitignore` to exclude materials or generated files you do not want to commit. Document how others can obtain or recreate anything needed to reproduce the analysis. Ignore rules do not affect files already tracked by Git.

## An IMRaD-like project

The [IMRaD](https://en.wikipedia.org/wiki/IMRAD)-like Project is a useful and intuitive project layout. It also serves as an introduction to the [installable IMRaD-like project](#an-installable-imrad-like-project). It isn't installable; however, its IMRaD-like naming convention makes its organization immediately recognizable to persons working in the science domains.

### Features

- A simple [IMRaD](https://en.wikipedia.org/wiki/IMRAD)-like layout.

### Explore the project layout

You can [create an IMRaD-like project using the Cookiecutter](#create-an-imrad-like-project-using-the-cookiecutter).

#### The directory structure looks like this.

```
├── project ⬅ This is the project directory.
    │
    ├── AGENTS.md ⬅ Optional guidance for AI assistants working on this study.
    │
    ├── materials ⬅ Put inputs and supporting materials here; organize them for your study.
    │   │
    │   └── README.md
    │
    ├── methods ⬅ You can put your utility functions and notebooks in the methods directory.
    │   │
    │   ├── main.ipynb
    │   │
    │   └── README.md
    │
    ├── results ⬅ You can put the outputs of your scripts (e.g., tables and visualizations) in the results directory.
    │   │
    │   └── README.md
    │
    ├── requirements.txt ⬅ You can specify your project requirements in this file.
    │
    ├── README.md ⬅ You can put your Introduction and Discussion in the README.md file.
    │
    └── .gitignore
```

### Create an IMRaD-like project using the Cookiecutter

Install the Cookiecutter package.

```bash
python -m pip install cookiecutter
```

Use the Cookiecutter to create an IMRaD-like project.

```bash
cookiecutter https://github.com/adamjpatterson/the-data-science-project.git --checkout imrad-project-v1.0.0
```

This template asks only for the project directory name and optional AI guidance:

```text
[1/2] Project directory name (project):
[2/2] Include AGENTS.md guidance?
    1 - yes
    2 - no
    Choose from [1/2] (1):
```

Open `methods/main.ipynb` with `methods` as the working directory. Its first cell uses `pathlib` to define absolute paths to the project root and its three
directories; no package installation is needed.

## Data science and statistical analysis with AI assistance

These layouts provide a simple organizational convention for developing data science and statistical analyses with AI assistance. The names `materials`, `methods`, and `results` give people and AI assistants a shared vocabulary for discussing the study and deciding where its files belong. Inputs and supporting materials go in `materials`, procedures go in `methods`, and products of the analysis go in `results`. The contents of each directory can evolve with the study.

In the installable project, reusable Python code belongs in the package within `methods`, where it can be imported by notebooks and other procedures. The workspace paths provide consistent locations for reading inputs and writing outputs. This gives an AI assistant concrete conventions to follow when extending an analysis, while leaving the choice of scientific methods and the interpretation of results to the study itself.

By default, each generated project includes an `AGENTS.md` at its root with guidance for AI assistants on file organization, workspace paths, and running the analysis. Select `no` for "Include AGENTS.md guidance?" during Cookiecutter setup to omit this file. Adapt it as the study develops to record project-specific conventions and validation commands.

The examples below show the complete files generated by the templates. The installable example uses the default package name, `package`; Cookiecutter substitutes the name you choose.

<details>
<summary>AGENTS.md — Installable IMRaD-like Project</summary>

```markdown
# Working on this study

This is an IMRaD-like project for data science and statistical analysis. Read the
root README and the relevant directory READMEs for the study's purpose and
existing conventions before extending it.

## Organization

- `materials/`: source data, supporting materials, intermediate datasets, and
  models consumed by the analysis.
- `methods/`: procedures, notebooks, and reusable Python code.
- `results/`: products of the analysis, including datasets, figures, and models.

Organize subdirectories to suit the study; no fixed data or model taxonomy is
required. Preserve original inputs and make transformations traceable through
code. Describe the study's question and interpretation in the root README.

## Python code and workspace paths

Put reusable Python code in `methods/package/` and notebooks
in `methods/`. From the project root, install the package into the
working environment with `python -m pip install -e .`. Use that environment for
notebooks and scripts. Declare dependencies in `pyproject.toml`.

Import `PROJECT_ROOT`, `MATERIALS_PATH`, `METHODS_PATH`, and `RESULTS_PATH` from
`package`. These constants are defined in `__init__.py` relative to
this source layout. They do not create or validate directories. Use an editable
installation so imports refer to this study's source code. Put reusable functions
in `utils.py` or other package modules.

## Running and sharing the analysis

The `main()` function in `methods/package/__main__.py` starts empty.
Run it with `python -m package` after adding workflow steps.
The study author chooses any command-line arguments and file locations.
Run notebooks separately unless the study adds notebook execution to its workflow.

Share the complete study through its GitHub repository. Document dependency
installation, how to obtain data, and how to reproduce the analysis. Readers
clone the repository and run `python -m pip install -e .` in its root.

## Checking changes

Run the affected analysis steps and any existing checks in the intended
environment. Record the commands used and distinguish results actually verified
from steps that could not be run. Keep outputs traceable to their inputs and
methods, and explain analytical assumptions in the study documentation.
```

</details>

<details>
<summary>AGENTS.md — IMRaD-like Project</summary>

```markdown
# Working on this study

This is an IMRaD-like project for data science and statistical analysis. Read the
root README and the relevant directory READMEs for the study's purpose and
existing conventions before extending it.

## Organization

- `materials/`: source data, supporting materials, intermediate datasets, and
  models consumed by the analysis.
- `methods/`: procedures, notebooks, and reusable Python code.
- `results/`: products of the analysis, including datasets, figures, and models.

Organize subdirectories to suit the study; no fixed data or model taxonomy is
required. Preserve original inputs and make transformations traceable through
code. Describe the study's question and interpretation in the root README.

## Python code and workspace paths

Keep notebooks and utility scripts in `methods/`. This project has no installable
Python package. List dependencies in `requirements.txt` and use the same working
environment for scripts and notebooks.

Run `methods/main.ipynb` with `methods` as the working directory. Its first cell
uses `pathlib` to define `PROJECT_ROOT`, `MATERIALS_PATH`, `METHODS_PATH`, and
`RESULTS_PATH`. Use these absolute paths for file access. If adding another entry
point, establish its workspace paths explicitly; do not assume that these
notebook variables exist in other processes.

## Running the analysis

Run the relevant notebooks or scripts directly. There is no package entry point
or predefined pipeline. Document the execution order and working-directory
requirements as the analysis develops.

## Checking changes

Run the affected analysis steps and any existing checks in the intended
environment. Record the commands used and distinguish results actually verified
from steps that could not be run. Keep outputs traceable to their inputs and
methods, and explain analytical assumptions in the study documentation.
```

</details>

## Release

The template release is **1.0.0**. The commands above select its fixed release
tags. For ongoing development, use the `installable_imrad_project_cookiecutter`
or `imrad_project_cookiecutter` branch instead. The two templates live on
independent branches; `main` contains shared documentation and tests.

Generated packages have their own version, initially `0.0.1` in `__about__.py`.
Study authors manage that version independently of the template release.

## Development checks

See [the integration test instructions](https://github.com/adamjpatterson/the-data-science-project/blob/main/tests/README.md) for testing both Cookiecutter templates across the project branches.

## Other solutions

Other approaches to organizing data science projects include:

- [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/): A project template from DrivenData with dedicated directories for data, models, notebooks, and reports, plus configurable development tools.

## Support

If you have a feature request or run into any issues, feel free to submit an [issue](https://github.com/adamjpatterson/the-data-science-project/issues). You’re also welcome to reach out directly to the author.

- [Adam Patterson](https://github.com/adamjpatterson)
