# Project layout

This study uses an IMRaD-like layout:

- `materials/`: inputs and supporting materials, including datasets and models.
- `methods/`: analysis procedures, notebooks, and reusable code.
- `results/`: outputs of the analysis, including datasets, figures, and models.

The contents and subdirectories depend on the study.

## Python package and notebook

`methods/main.ipynb` is the starter notebook. The Python package is in
`methods/{{cookiecutter.package_name}}/`; `utils.py` starts empty for reusable functions.

An editable installation (`python -m pip install -e .` from the project root)
makes `{{cookiecutter.package_name}}` importable from the study's source code.
The package's `__init__.py` defines `PROJECT_ROOT`, `MATERIALS_PATH`,
`METHODS_PATH`, and `RESULTS_PATH` relative to this layout. These constants do
not create or validate directories.

`python -m {{cookiecutter.package_name}}` calls `main()` in the package's `__main__.py`.
The starter function is empty; no analysis or notebook execution is predefined.
