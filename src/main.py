# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_AboutWindow
import sys
import os

__version__ = "β-0.1"
__channel__ = "beta"

def getThemedBox():
    msg = QMessageBox()
    msg.setWindowTitle("Turing")
    msg.setStyle(DEFAULT_STYLE)
    msg.setWindowIcon(QIcon("image/icon.png"))
    center_widget(msg, window)
    return msg

class myMainWindow(QMainWindow):
    def closeEvent(self, event):
        if False:
            event.accept()
            return
        msg = getThemedBox()
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.setText("Voulez-vous vraiment quitter ?\nToutes les modifications non sauvegardées seront perdues.")
        center_widget(msg, self)
        event.ignore()
        if msg.exec_() == QMessageBox.Yes:
            event.accept()

def center_widget(wgt, host):
    if not host:
        host = wgt.parent()

    if host:
        wgt.move(host.geometry().center() - wgt.rect().center())
    else:
        wgt.move(app.desktop().screenGeometry().center() - wgt.rect().center())

def getact(name):
    return getattr(ui, "action" + name)

def refresh():
    refresh_buttons_status()

def refresh_buttons_status():
    active_code = False
    for c in [
        "Save",
        "SaveAs",
        "Close",
        "Print",
        "Find",
        "Replace",
        "SelectAll",
        "Run",
        "Step",
        "ConvertToPython",
        "ConvertToPseudocode"
    ]:
        getact(c).setEnabled(active_code)


def handler_AboutTuring():
    about = QDialog()
    about_ui = Ui_AboutWindow()
    about_ui.setupUi(about)
    about.setFixedSize(about.size())
    txt = about_ui.textEdit_about.toHtml().replace("{version}", __version__).replace("{channel}", __channel__)
    about_ui.textEdit_about.setHtml(txt)
    center_widget(about, window)
    about.exec_()

def handler_ShowToolbar():
    if ui.toolBar.isVisible():
        ui.toolBar.hide()
    else:
        ui.toolBar.show()

def handler_ShowToolbarText():
    if ui.toolBar.toolButtonStyle() == Qt.ToolButtonTextUnderIcon:
        ui.toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
    else:
        ui.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

def initActions():
    for c in dir(ui):
        if c.startswith("action"):
            name = "handler_" + c[6:]
            if name in globals():
                getattr(ui, c).triggered.connect(globals()[name])

def initUi():
    global window, ui
    window = myMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    ui.tabWidget.tabBar().tabButton(0, QTabBar.RightSide).resize(0, 0)
    initActions()
    refresh()
    window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    DEFAULT_STYLE = QStyleFactory.create(app.style().objectName())
    if os.name == "nt":
        font = QFont("Segoe UI", 9)
        app.setFont(font)
    initUi()

    exitCode = app.exec_()
    sys.exit(exitCode)