from typing import Any, Callable

import os
from abc import abstractmethod
from pathlib import Path

from loguru import logger
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor, QFont

from workflow_manager_example.workflow_manager.action_script import ActionScript
from workflow_manager_example.workflow_manager.config import Config, import_pyproject_config

CWD = os.getcwd()


# pylint: disable=invalid-name,too-few-public-methods
class Ui_MainWindow:
    def __init__(self) -> None:
        self.centralwidget = QtWidgets.QWidget()
        self.header = QtWidgets.QWidget()
        self.header_app_name = QtWidgets.QLabel()
        self.body = QtWidgets.QWidget()
        self.script_output = QtWidgets.QGroupBox()
        self.script_output_text_edit = QtWidgets.QPlainTextEdit()
        self.about_action = QtWidgets.QAction()

    def setupUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        pass


class WorkflowManager(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        logger.info("Start WorkflowManager().__init__()")
        super().__init__()

        self.config: Config = self.config or import_pyproject_config(
            pyproject_file="pyproject.toml"
        )
        logger.info(f"WorkflowManager.config: loaded ok. {self.config=}")

        # Load UI
        self.ui = self.ui or Ui_MainWindow()
        self.ui.setupUi(self)

        # Customize Window
        self.setWindowTitle(self.config.app_name)
        self.ui.header_app_name.setText(self.config.app_name)
        self.statusBar().showMessage(self.config.statusbar_text)
        self.setGeometry(
            self.config.pos_x, self.config.pos_y, self.config.width, self.config.height
        )

        # Connections
        self.connect_buttons()

        # Show
        logger.info("WorkflowManager.ui: loaded ok. WorkflowManager().show()...")
        self.show()

    @abstractmethod
    def connect_buttons(self) -> None:
        """Connects UI buttons the the callback function."""
        self.ui.about_action.triggered.connect(self.display_about_message_box)

    @abstractmethod
    def validate_inputs(self, **kwargs: object) -> Any:
        """Validation on required inputs. ie. Ensure file exists, ensure value is int, etc."""
        return

    def _get_file_name(
        self,
        file_filter: str = "",
        initial_filter: str = "",
        directory: str = CWD,
    ) -> str:
        # file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls)'
        response = QtWidgets.QFileDialog.getOpenFileName(
            parent=self,
            caption="Select a file",
            directory=directory,
            filter=file_filter,
            initialFilter=initial_filter,
        )
        logger.info(f"WorkflowManager._get_file_name.{response[0]=}")
        return response[0]

    def _get_file_names(
        self,
        file_filter: str = "",
        initial_filter: str = "",
        directory: str = CWD,
    ) -> list[str]:
        response = QtWidgets.QFileDialog.getOpenFileNames(
            parent=self,
            caption="Select files",
            directory=directory,
            filter=file_filter,
            initialFilter=initial_filter,
        )
        logger.info(f"WorkflowManager._get_file_names.{response[0]=}")
        return response[0]

    @staticmethod
    def _get_color() -> QColor:
        color = QtWidgets.QColorDialog().getColor()
        logger.info(f"WorkflowManager._get_color.{color=}")
        return color

    def _get_color_name(self, color: QColor | None = None) -> str:
        if not color:
            color = self._get_color()
        logger.info(f"WorkflowManager._get_color_name.{color.name()=}")
        return color.name()

    @logger.catch()
    @staticmethod
    def _get_font() -> QFont:
        font, valid = QtWidgets.QFontDialog.getFont()
        if valid:
            return font
        raise FileNotFoundError("Font Not Found.")

    def _get_font_name(self, font: QFont | None = None) -> str:
        if not font:
            font = self._get_font()
        font_name = font.toString().split(",")[0]
        logger.info(f"WorkflowManager._get_font_name.{font_name=}")
        return font_name

    def _get_directory(self, directory: str = CWD) -> str:
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            self, caption="Select a folder", directory=directory
        )
        logger.info(f"WorkflowManager._get_directory.{directory=}")
        return directory

    def _get_save_file_name(
        self,
        initial_file_name: str = "save.txt",
        file_filter: str = "",
        initial_filter: str = "",
        directory: str = CWD,
    ) -> str:
        directory_path = Path(directory)
        initial_file_path = directory_path / initial_file_name

        response = QtWidgets.QFileDialog.getSaveFileName(
            parent=self,
            caption="Save to file",
            directory=str(initial_file_path),
            filter=file_filter,
            initialFilter=initial_filter,
        )
        logger.info(f"WorkflowManager._get_save_file_name.{response[0]=}")
        return response[0]

    def print_to_output(self, text: str) -> None:
        text = f"\n{text}" if self.ui.script_output_text_edit.toPlainText() else text
        return self.ui.script_output_text_edit.appendPlainText(text)

    def display_script_completed_message_box(self) -> QtWidgets.QMessageBox.StandardButton:
        logger.success("The script successfully completed!")
        return QtWidgets.QMessageBox().information(
            self, "Completed!", "The script successfully completed!"
        )

    def display_script_error_message_box(
        self, error_msg: str
    ) -> QtWidgets.QMessageBox.StandardButton:
        logger.error(f"Script Error: {error_msg=}")
        return QtWidgets.QMessageBox().critical(self, "Script Error!", error_msg)

    def display_about_message_box(self) -> None:
        dlg = QtWidgets.QMessageBox(self)
        dlg.setWindowTitle("")
        dlg.setIcon(QtWidgets.QMessageBox.Information)  # type: ignore
        dlg.setText(self.config.about_text)
        dlg.exec()

    def inputs_are_valid(self, **kwargs: object) -> bool:
        if rtn := self.validate_inputs(**kwargs):
            text = f"Invalid inputs. Please double check all inputs.\n{rtn}"
            self.print_to_output(text)
            QtWidgets.QMessageBox().warning(self, "Invalid inputs!", text)
            logger.error(f"Invalid Inputs: {rtn=}")
            return False
        return True

    def run_action_script(self, script_cls: Callable[..., ActionScript], **kwargs: object) -> None:
        # Run Script
        logger.info(f"WorkflowManager.run_action_script.{kwargs=}")
        self.print_to_output("Running script...")
        settings = "\n".join([f"  - {k}: {v}" for k, v in kwargs.items()])
        self.print_to_output(f"SETTINGS: \n{settings}")

        rtn = script_cls().run(**kwargs)
        self.print_to_output(f"OUTPUT: {rtn}")

        # Completion Tasks
        if "error:" in rtn.lower():
            self.display_script_error_message_box(error_msg=rtn)
        else:
            self.display_script_completed_message_box()
