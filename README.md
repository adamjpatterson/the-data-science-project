# The Data Science Project: IMRaD-like Project

Create a project with `materials`, `methods`, and `results` directories. Organize
their contents to suit your study; no particular data or output categories are
required. This layout does not include an installable Python package.

## Release 1.0.0

These commands select the fixed 1.0.0 release. This branch contains ongoing development.

```bash
python -m pip install cookiecutter
cookiecutter https://github.com/adamjpatterson/the-data-science-project.git --checkout imrad-project-v1.0.0
```

Open the generated `methods/main.ipynb` with `methods` as the working directory.
Its first cell defines absolute paths to the project root and its three
directories. List your project's dependencies in `requirements.txt`.

See the [project introduction](https://github.com/adamjpatterson/the-data-science-project/blob/main/INTRODUCTION.md).

## Optional AI guidance

The `include_agents_md` choice defaults to `yes`. Select `no` to omit the
generated project's `AGENTS.md`. The remaining project files are unchanged.

Setup uses readable prompt labels.
