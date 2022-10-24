# Form implementation generated from reading ui file '/media/martokk/FILES/dev/frameworks/workflow_manager_example/assets/ui/pyqt5_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(611, 620)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStatusTip("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header = QtWidgets.QVBoxLayout()
        self.header.setSpacing(6)
        self.header.setObjectName("header")
        self.header_2 = QtWidgets.QHBoxLayout()
        self.header_2.setObjectName("header_2")
        spacerItem = QtWidgets.QSpacerItem(
            40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.header_2.addItem(spacerItem)
        self.header_icon = QtWidgets.QLabel(self.centralwidget)
        self.header_icon.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_icon.sizePolicy().hasHeightForWidth())
        self.header_icon.setSizePolicy(sizePolicy)
        self.header_icon.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.header_icon.setScaledContents(True)
        self.header_icon.setWordWrap(False)
        self.header_icon.setObjectName("header_icon")
        self.header_2.addWidget(self.header_icon)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.header_2.addWidget(self.label)
        self.header_app_name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.header_app_name.setFont(font)
        self.header_app_name.setObjectName("header_app_name")
        self.header_2.addWidget(self.header_app_name)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.header_2.addItem(spacerItem1)
        self.header.addLayout(self.header_2)
        self.verticalLayout_2.addLayout(self.header)
        self.horizontalLine = QtWidgets.QFrame(self.centralwidget)
        self.horizontalLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontalLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalLine.setObjectName("horizontalLine")
        self.verticalLayout_2.addWidget(self.horizontalLine)
        self.body = QtWidgets.QWidget(self.centralwidget)
        self.body.setObjectName("body")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.body)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.run_script = QtWidgets.QGroupBox(self.body)
        self.run_script.setObjectName("run_script")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.run_script)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.run_script_grid_layout = QtWidgets.QGridLayout()
        self.run_script_grid_layout.setObjectName("run_script_grid_layout")
        self.line1_line_edit = QtWidgets.QLineEdit(self.run_script)
        self.line1_line_edit.setObjectName("line1_line_edit")
        self.run_script_grid_layout.addWidget(self.line1_line_edit, 0, 2, 1, 1)
        self.line2_browse_button = QtWidgets.QPushButton(self.run_script)
        icon = QtGui.QIcon.fromTheme("document-open")
        self.line2_browse_button.setIcon(icon)
        self.line2_browse_button.setObjectName("line2_browse_button")
        self.run_script_grid_layout.addWidget(self.line2_browse_button, 1, 3, 1, 1)
        self.line2_line_edit = QtWidgets.QLineEdit(self.run_script)
        self.line2_line_edit.setObjectName("line2_line_edit")
        self.run_script_grid_layout.addWidget(self.line2_line_edit, 1, 2, 1, 1)
        self.run_script_button = QtWidgets.QPushButton(self.run_script)
        icon = QtGui.QIcon.fromTheme("text-x-script")
        self.run_script_button.setIcon(icon)
        self.run_script_button.setObjectName("run_script_button")
        self.run_script_grid_layout.addWidget(self.run_script_button, 3, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.run_script_grid_layout.addItem(spacerItem2, 3, 2, 1, 1)
        self.line1_browse_button = QtWidgets.QPushButton(self.run_script)
        icon = QtGui.QIcon.fromTheme("document-open")
        self.line1_browse_button.setIcon(icon)
        self.line1_browse_button.setObjectName("line1_browse_button")
        self.run_script_grid_layout.addWidget(self.line1_browse_button, 0, 3, 1, 1)
        self.line1_label = QtWidgets.QLabel(self.run_script)
        self.line1_label.setObjectName("line1_label")
        self.run_script_grid_layout.addWidget(self.line1_label, 0, 1, 1, 1)
        self.line2_label = QtWidgets.QLabel(self.run_script)
        self.line2_label.setObjectName("line2_label")
        self.run_script_grid_layout.addWidget(self.line2_label, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.run_script_grid_layout.addItem(spacerItem3, 2, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.run_script_grid_layout)
        self.verticalLayout_4.addWidget(self.run_script)
        self.script_output = QtWidgets.QGroupBox(self.body)
        self.script_output.setObjectName("script_output")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.script_output)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.script_output_text_edit = QtWidgets.QPlainTextEdit(self.script_output)
        self.script_output_text_edit.setObjectName("script_output_text_edit")
        self.horizontalLayout.addWidget(self.script_output_text_edit)
        self.verticalLayout_4.addWidget(self.script_output)
        self.verticalLayout_2.addWidget(self.body)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 611, 19))
        self.menubar.setObjectName("menubar")
        self.about_menu = QtWidgets.QMenu(self.menubar)
        self.about_menu.setObjectName("about_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMain = QtWidgets.QAction(MainWindow)
        self.actionMain.setObjectName("actionMain")
        self.about_action = QtWidgets.QAction(MainWindow)
        self.about_action.setObjectName("about_action")
        self.actionCustom = QtWidgets.QAction(MainWindow)
        self.actionCustom.setObjectName("actionCustom")
        self.about_menu.addAction(self.about_action)
        self.menubar.addAction(self.about_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header_icon.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><img src=":/resources/icon" height="64" width="64" /></p></body></html>',
            )
        )
        self.header_app_name.setText(_translate("MainWindow", "xxxxxxxxxx"))
        self.run_script.setTitle(_translate("MainWindow", "Run Script"))
        self.line2_browse_button.setText(_translate("MainWindow", "Browse"))
        self.run_script_button.setText(_translate("MainWindow", "Run Script"))
        self.line1_browse_button.setText(_translate("MainWindow", "Browse"))
        self.line1_label.setText(_translate("MainWindow", "line1Label"))
        self.line2_label.setText(_translate("MainWindow", "line2Label"))
        self.script_output.setTitle(_translate("MainWindow", "Script Output:"))
        self.about_menu.setTitle(_translate("MainWindow", "About"))
        self.actionMain.setText(_translate("MainWindow", "Main"))
        self.about_action.setText(_translate("MainWindow", "About"))
        self.actionCustom.setText(_translate("MainWindow", "Get more custom scripts..."))


import resources_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())