from unittest.mock import Mock

from workflow_manager.config import import_pyproject_config


def test_import_toml(mocker: Mock) -> None:
    mocker.patch(
        "toml.load", return_value={"workflow_manager": {"app_name": "abc", "about_text": "def"}}
    )
    config = import_pyproject_config(pyproject_file=".")
    assert config.app_name == "abc"
    assert config.statusbar_text == "App designed by v3services"
    assert config.about_text == "def"
    assert config.pos_x == 0
    assert config.pos_y == 0
    assert config.height == 1200
    assert config.width == 800
