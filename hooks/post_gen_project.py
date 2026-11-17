"""Omit optional starter files when requested."""
from pathlib import Path

if "{{ cookiecutter.include_agents_md }}" == "no":
    Path("AGENTS.md").unlink()

if "{{ cookiecutter.include_utils }}" == "no":
    Path("methods/{{ cookiecutter.package_name }}/utils.py").unlink()
