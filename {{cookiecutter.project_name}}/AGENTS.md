# Project layout

This study uses an IMRaD-like layout:

- `materials/`: inputs and supporting materials, including datasets and models.
- `methods/`: analysis procedures, notebooks, and reusable code.
- `results/`: outputs of the analysis, including datasets, figures, and models.

The contents and subdirectories depend on the study.

## Notebook and dependencies

`methods/main.ipynb` is the starter notebook. Its first cell defines
`PROJECT_ROOT`, `MATERIALS_PATH`, `METHODS_PATH`, and `RESULTS_PATH`, assuming
`methods/` is the current working directory.

This template has no installable Python package or predefined pipeline.
`requirements.txt` starts empty for the study's dependencies.
