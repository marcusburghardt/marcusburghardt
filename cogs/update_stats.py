"""
update_stats.py

This script calculates the experience in years since a hard-coded start date
and updates a README file using a Jinja2 template.

Author: Marcus Burghardt
SPDX-License-Identifier: Apache-2.0
"""
from datetime import datetime
from jinja2 import Template


def calculate_experience() -> int:
    first_job = datetime(2003, 1, 1)
    today = datetime.now()
    return (today - first_job).days // 365


def render_template(info: dict) -> None:
    """Render the README file using Jinja2 template."""
    template_path = "README.template.md"
    readme_path = "../README.md"

    try:
        with open(template_path, "r") as template_file:
            template_content = template_file.read()
    except FileNotFoundError:
        print(f"Error: The template file '{template_path}' was not found.")
        return

    template = Template(template_content)
    rendered_content = template.render(info)

    try:
        with open(readme_path, "w") as readme_file:
            readme_file.write(rendered_content)
    except FileNotFoundError:
        print(f"Error: The README file '{readme_path}' was not found.")


def main():
    info = {
        "experience": calculate_experience(),
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
    }

    render_template(info)


if __name__ == "__main__":
    main()
