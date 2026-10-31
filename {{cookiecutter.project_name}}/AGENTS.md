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
