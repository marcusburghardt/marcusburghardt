"""
update_readme.py

This script calculates the experience in years since a hard-coded start date
and updates a README file using a Jinja2 template.

Author: Marcus Burghardt
SPDX-License-Identifier: Apache-2.0
"""

import sys
from datetime import datetime
from pathlib import Path

from jinja2 import Template

# Resolve paths relative to this script's location so that
# the script works regardless of the current working directory.
SCRIPT_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = SCRIPT_DIR / "README.template.md"
README_PATH = SCRIPT_DIR.parent / "README.md"


def calculate_experience() -> int:
    """Return the number of full years since the career start date."""
    first_job = datetime(2003, 1, 1)
    today = datetime.now()
    return (today - first_job).days // 365


def render_template(info: dict) -> None:
    """Render the README file using Jinja2 template."""
    try:
        template_content = TEMPLATE_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: The template file '{TEMPLATE_PATH}' was not found.")
        sys.exit(1)

    template = Template(template_content)
    rendered_content = template.render(info)

    try:
        README_PATH.write_text(rendered_content, encoding="utf-8")
    except OSError as exc:
        print(f"Error writing README file '{README_PATH}': {exc}")
        sys.exit(1)

    print(f"README updated successfully: {README_PATH}")


def main() -> None:
    info = {
        "experience": calculate_experience(),
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
    }

    render_template(info)


if __name__ == "__main__":
    main()
