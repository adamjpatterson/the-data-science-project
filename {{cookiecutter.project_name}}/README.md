# Project

## Introduction

Describe the question or purpose of this study.

## Organization

- `materials/`: inputs and supporting materials for this study.
- `methods/`: notebooks, reusable Python code, and other methods.
- `results/`: outputs from the study.

Organize the contents of these directories to suit your study. No particular data,
model, or output categories are required.

The Python package is in `methods/{{cookiecutter.package_name}}/`. After cloning this
study, install it from the project directory with `python -m pip install -e .`.
Open `methods/main.ipynb` in the same environment. Its first cell uses:

```python
from {{cookiecutter.package_name}} import PROJECT_ROOT, MATERIALS_PATH, METHODS_PATH, RESULTS_PATH
from {{cookiecutter.package_name}} import utils
```

The four constants in `__init__.py` derive absolute paths from the package's
location in this source layout. They do not create or validate directories.
Put reusable functions in `utils.py` or add modules as the study grows.

Run `python -m {{cookiecutter.package_name}}` to call the starter `main()` in
`__main__.py`. It does nothing until you add your workflow. Define any arguments
or input and output locations your analysis needs. Notebooks run separately.

Share the study repository on GitHub with its documentation and shareable data.
For data kept elsewhere, document how to obtain it. Readers can clone the study
and install it in editable mode. A standalone wheel does not contain the study
folders; these source-layout path constants are intended for editable use.

The generated package starts at version `0.0.1`, recorded in `__about__.py`.
Manage that version independently of the template release. Before publishing
your package, choose its license and add the corresponding file and metadata.

## Discussion

Describe and interpret the results here.
