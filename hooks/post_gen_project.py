"""Omit optional AI guidance when requested."""
from pathlib import Path

if "{{ cookiecutter.include_agents_md }}" == "no":
    Path("AGENTS.md").unlink()
