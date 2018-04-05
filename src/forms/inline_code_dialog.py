# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from forms.ui_inline_code import Ui_InlineCodeDialog
from forms.inline_code_editor import InlineCodeEditor
from util.widgets import center_widget

translate = QCoreApplication.translate

class InlineCodeDialog(QDialog):
    def __init__(self, parent, origcode=""):
        super().__init__()
        self.ui = Ui_InlineCodeDialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        center_widget(self, parent)
        self.editor = InlineCodeEditor(self)
        self.editor.set_text(origcode)
        self.ui.verticalLayout.addWidget(self.editor)
        self.editor.submitted.connect(self.accept)

    def run(self):
        self.exec_()
        return self.editor.get_text()
