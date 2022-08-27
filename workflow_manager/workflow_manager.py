import os
from abc import abstractmethod
from typing import Callable

from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QColorDialog, QFontDialog


class WorkflowManager(QMainWindow):
    def __init__(self, ui, app_name="WorkflowManager", statusbar="App designed by v3services", pos_x=0, pos_y=0,
                 height=1200, width=800, about="App designed by v3services"):
        super().__init__()
        print("Start WorkflowManager().__init__()")
        self._app_name = app_name
        self._about = about

        # Load UI
        self.ui = ui  # Generated from QtDesigner
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
    def connect_buttons(self):
        """ Connects UI buttons the the callback function."""
        self.ui.actionAbout.triggered.connect(self.display_about_message_box)

    @abstractmethod
    def validate_inputs(self, **kwargs) -> bool:
        """ Validation on required inputs. ie. Ensure file exists, ensure value is int, etc. """
        return True

    def _get_file_name(self, file_filter=None, initial_filter=None):
        # file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter=initial_filter
        )
        return response[0]

    def _get_file_names(self, file_filter=None, initial_filter=None):
        response = QFileDialog.getOpenFileNames(
            parent=self,
            caption='Select files',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter=initial_filter
        )
        return response[0]

    @staticmethod
    def _get_color() -> str:
        return QColorDialog().getColor()

    def _get_color_name(self, color: QColor = None):
        if not color:
            color = self._get_color()
        return color.name()

    @staticmethod
    def _get_font() -> QFont:
        font, valid = QFontDialog.getFont()
        if valid:
            return font
        raise FileNotFoundError("Font Not Found.")

    def _get_font_name(self, font: QFont = None):
        if not font:
            font = self._get_font()
        return font.toString().split(',')[0]

    def _get_directory(self):
        return QFileDialog.getExistingDirectory(self, caption='Select a folder')

    def _get_save_file_name(self, initial_file_name='save.txt', file_filter=None, initial_filter=None):
        response = QFileDialog.getSaveFileName(
            parent=self,
            caption='Save to file',
            directory=initial_file_name,
            filter=file_filter,
            initialFilter=initial_filter
        )
        return response[0]

    def print_to_output(self, text: str):
        text = f"\n{text}" if self.ui.actionPlainTextEdit.toPlainText() else text
        return self.ui.actionPlainTextEdit.appendPlainText(text)

    def display_script_completed_message_box(self):
        return QMessageBox().information(self, "Completed!", "The script successfully completed!")

    def display_script_error_message_box(self, error_msg: str):
        return QMessageBox().critical(self, "Script Error!", error_msg)

    def display_about_message_box(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("")
        dlg.setIcon(QMessageBox.Information)
        dlg.setText(self._about)
        dlg.exec()

    def inputs_are_valid(self, **kwargs):
        if rtn := self.validate_inputs(**kwargs):
            text = f'Invalid inputs. Please double check all inputs.\n{rtn}'
            self.print_to_output(text)
            QMessageBox().warning(self, "Invalid inputs!", text)
            return False
        return True

    def run_action_script(self, script_cls: Callable, **kwargs):
        # Run Script
        self.print_to_output('Running script...')
        settings = '\n'.join([f"  - {k}: {v}" for k, v in kwargs.items()])
        self.print_to_output(f'SETTINGS: \n{settings}')

        rtn = script_cls().run(**kwargs)
        self.print_to_output(f"OUTPUT: {rtn}")

        # Completion Tasks
        if "error:" in rtn.lower():
            self.display_script_error_message_box(error_msg=rtn)
        else:
            self.display_script_completed_message_box()
