# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from forms.ui_alg_func import Ui_AlgoFuncStmt
from util.code import is_id
from util.widgets import center_widget, msg_box_error

translate = QCoreApplication.translate


class AlgoFuncStmt(QDialog):
    def __init__(self, parent, origcode=("", ())):
        super().__init__(parent)
        self.ui = Ui_AlgoFuncStmt()
        self.ui.setupUi(self)
        self.setFixedWidth(self.width())
        self.adjustSize()
        self.setFixedSize(self.size())
        self.ui.txtFunction.setText(origcode[0])
        self.ui.txtArguments.setText(", ".join(origcode[1]))
        center_widget(self, parent)

    def done(self, res):
        if res == QDialog.Accepted:
            lst = [x.strip() for x in [self.ui.txtFunction.text()] + self.ui.txtArguments.text().split(",")]

            for name in lst:
                if not is_id(name):
                    box = msg_box_error(translate("Algo", "Invalid name: {name}").format(name=name), parent=self)
                    box.exec_()
                    return

            self.func = lst[0]
            self.args = lst[1:]

            self.ok = True

        super(AlgoFuncStmt, self).done(res)

    def run(self):
        return self.exec_() == QDialog.Accepted and self.ok
