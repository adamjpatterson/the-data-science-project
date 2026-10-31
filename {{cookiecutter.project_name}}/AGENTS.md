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

Put reusable Python code in `methods/{{cookiecutter.package_name}}/` and notebooks
in `methods/`. From the project root, install the package into the
working environment with `python -m pip install -e .`. Use that environment for
notebooks and scripts. Declare dependencies in `pyproject.toml`.

Import `PROJECT_ROOT`, `MATERIALS_PATH`, `METHODS_PATH`, and `RESULTS_PATH` from
`{{cookiecutter.package_name}}`. These constants are defined in `__init__.py` relative to
this source layout. They do not create or validate directories. Use an editable
installation so imports refer to this study's source code. Put reusable functions
in `utils.py` or other package modules.

## Running and sharing the analysis

The `main()` function in `methods/{{cookiecutter.package_name}}/__main__.py` starts empty.
Run it with `python -m {{cookiecutter.package_name}}` after adding workflow steps.
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
