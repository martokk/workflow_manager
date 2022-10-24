from typing import Optional

from dataclasses import dataclass
from pathlib import Path

import toml


@dataclass
class Config:
    app_name: str = "WorkflowManagerExampleApp"
    statusbar_text: str = "App designed by v3services"
    about_text: str = (
        "App designed by v3services. \n\n"
        "If you need support, bug fixes, or new scripts created, "
        "please contact us at mike.villarreal@outlook.com."
    )
    pos_x: int = 0
    pos_y: int = 0
    height: int = 1200
    width: int = 800


def import_pyproject_config(pyproject_file: Path | str) -> Config:
    toml_data = toml.load(Path(pyproject_file))
    workflow_manager_toml_data = toml_data["workflow_manager"]
    return Config(**workflow_manager_toml_data)
