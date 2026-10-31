# The Data Science Project: Installable IMRaD-like Project

This template creates a study with `materials`, `methods`, and `results` at the
project root. Organize their contents to suit your study. Reusable Python code
lives in `methods/package` by default; `package_name` is configurable.

After cloning a generated study, run `python -m pip install -e .` in its root.
Import its path constants and `utils` from the configured package. Define a
workflow in the starter `main()` in `__main__.py`, then run it with
`python -m <package_name>`. Notebooks run separately.

Share the study on GitHub, including documentation and shareable data or data
retrieval instructions. See the generated README and the
[project introduction](https://github.com/adamjpatterson/the-data-science-project/blob/main/INTRODUCTION.md).

## Release 1.0.1

```bash
python -m pip install cookiecutter
cookiecutter https://github.com/adamjpatterson/the-data-science-project.git --checkout installable-imrad-project-v1.0.1
```

These commands select the fixed 1.0.1 release. This branch contains ongoing development.

## Optional AI guidance

The `include_agents_md` choice defaults to `yes`. Select `no` to omit the
generated project's `AGENTS.md`. The remaining project files are unchanged.

Setup uses readable prompt labels.
