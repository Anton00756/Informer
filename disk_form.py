from PyQt6 import QtCore, QtGui, QtWidgets
from compiled_ui.disk_die import Ui_Form


class DiskForm(QtWidgets.QWidget):
    yandex_icon = None
    google_icon = None
    close_icon = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.setIcon(DiskForm.google_icon)
        self.ui.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.ui.pushButton.setMinimumSize(35, 35)
        self.ui.pushButton.setMaximumSize(35, 35)
        self.ui.pushButton_2.setIcon(DiskForm.close_icon)
        self.ui.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.ui.pushButton_2.setMinimumSize(25, 25)
        self.ui.pushButton_2.setMaximumSize(25, 25)
        self.ui.checkBox.setMinimumSize(30, 30)
        self.ui.checkBox.setMaximumSize(30, 30)
        self.setMinimumWidth(200)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground, True)
