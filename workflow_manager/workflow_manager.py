import os
from abc import abstractmethod
from pathlib import Path
from typing import Any, Callable

from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import (QColorDialog, QFileDialog, QFontDialog,
                             QMainWindow, QMessageBox)

from workflow_manager.action_script import ActionScript

CWD = os.getcwd()


class WorkflowManager(QMainWindow):
    def __init__(
        self,
        ui: 'Ui_MainWindow',
        app_name: str = "WorkflowManager",
        statusbar: str = "App designed by v3services",
        pos_x: int = 0,
        pos_y: int = 0,
        height: int = 1200,
        width: int = 800,
        about: str = "App designed by v3services",
    ) -> None:
        super().__init__()
        print("Start WorkflowManager().__init__()")
        self._app_name = app_name
        self._about = about

        # Load UI
        self.ui = ui  # Generated from QtDesigner ## pylint: disable=invalid-name
        self.ui.setupUi(self)

        # Customize Window
        self.setWindowTitle(self._app_name)
        self.ui.headerAppName.setText(self._app_name)
        self.statusBar().showMessage(statusbar)
        self.setGeometry(pos_x, pos_y, width, height)

        # Connections
        self.connect_buttons()

        # Show
        self.show()

    @abstractmethod
    def connect_buttons(self) -> None:
        """Connects UI buttons the the callback function."""
        self.ui.actionAbout.triggered.connect(self.display_about_message_box)  # type: ignore

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
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select a file",
            directory=directory,
            filter=file_filter,
            initialFilter=initial_filter,
        )
        return response[0]

    def _get_file_names(
        self,
        file_filter: str = "",
        initial_filter: str = "",
        directory: str = CWD,
    ) -> list[str]:
        response = QFileDialog.getOpenFileNames(
            parent=self,
            caption="Select files",
            directory=directory,
            filter=file_filter,
            initialFilter=initial_filter,
        )
        return response[0]

    @staticmethod
    def _get_color() -> QColor:
        return QColorDialog().getColor()

    def _get_color_name(self, color: QColor | None = None) -> str:
        if not color:
            color = self._get_color()
        return color.name()

    @staticmethod
    def _get_font() -> QFont:
        font, valid = QFontDialog.getFont()
        if valid:
            return font
        raise FileNotFoundError("Font Not Found.")

    def _get_font_name(self, font: QFont | None = None) -> str:
        if not font:
            font = self._get_font()
        return font.toString().split(",")[0]

    def _get_directory(self, directory: str = CWD) -> str:
        return QFileDialog.getExistingDirectory(
            self, caption="Select a folder", directory=directory
        )

    def _get_save_file_name(
        self,
        initial_file_name: str = "save.txt",
        file_filter: str = "",
        initial_filter: str = "",
        directory: str = CWD,
    ) -> str:
        directory_path = Path(directory)
        initial_file_path = directory_path / initial_file_name

        response = QFileDialog.getSaveFileName(
            parent=self,
            caption="Save to file",
            directory=str(initial_file_path),
            filter=file_filter,
            initialFilter=initial_filter,
        )
        return response[0]

    def print_to_output(self, text: str) -> None:
        text = f"\n{text}" if self.ui.actionPlainTextEdit.toPlainText() else text
        return self.ui.actionPlainTextEdit.appendPlainText(text)

    def display_script_completed_message_box(self) -> QMessageBox.StandardButton:
        return QMessageBox().information(self, "Completed!", "The script successfully completed!")

    def display_script_error_message_box(self, error_msg: str) -> QMessageBox.StandardButton:
        return QMessageBox().critical(self, "Script Error!", error_msg)

    def display_about_message_box(self) -> None:
        dlg = QMessageBox(self)
        dlg.setWindowTitle("")
        dlg.setIcon(QMessageBox.Information)  # type: ignore
        dlg.setText(self._about)
        dlg.exec()

    def inputs_are_valid(self, **kwargs: object) -> bool:
        if rtn := self.validate_inputs(**kwargs):
            text = f"Invalid inputs. Please double check all inputs.\n{rtn}"
            self.print_to_output(text)
            QMessageBox().warning(self, "Invalid inputs!", text)
            return False
        return True

    def run_action_script(self, script_cls: Callable[..., ActionScript], **kwargs: object) -> None:
        # Run Script
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
