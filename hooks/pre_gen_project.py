import re
import sys

PROJECT = "{{ cookiecutter.project_slug }}"

if not re.match(r"^[a-z_][a-z0-9_]*$", PROJECT):
    print(f"ERROR: project_slug '{PROJECT}' must be lowercase with underscores only.")
    sys.exit(1)
