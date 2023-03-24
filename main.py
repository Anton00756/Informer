import sys
from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import *
from compiled_ui.main_window import Ui_MainWindow
from disk_form import DiskForm
# from plyer import notification
#
# notification.notify(message='Программа выполнена успешно', app_name='script', title='Готово', timeout=10)


# python -m PyQt6.uic.pyuic -x raw_ui/main_window.ui -o compiled_ui/main_window.py
# python -m PyQt6.uic.pyuic -x raw_ui/disk_die.ui -o compiled_ui/disk_die.py


class LinksWindow(QMainWindow):
    def __init__(self):
        super(LinksWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings = QtCore.QSettings("T-Corp.", "DiskChecker")
        if self.settings.value("WindowSize") is not None:
            self.resize(self.settings.value("WindowSize"))
        # self.settings.setValue("WindowSize", )
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
        self.setCentralWidget(self.ui.tableWidget)
        self.setMinimumWidth(250)
        DiskForm.google_icon = QtGui.QIcon(QtGui.QPixmap("images/google.png"))
        DiskForm.yandex_icon = QtGui.QIcon(QtGui.QPixmap("images/yandex.png"))
        DiskForm.close_icon = QtGui.QIcon(QtGui.QPixmap("images/close.png"))
        self.ui.tableWidget.setRowCount(4)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.tableWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)

        for i in range(3):
            self.ui.tableWidget.setCellWidget(i, 0, DiskForm())
            self.ui.tableWidget.setRowHeight(i, 50)
        self.ui.tableWidget.setRowHeight(self.ui.tableWidget.rowCount() - 1, 50)
        self.ui.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap("images/icon.ico")))
        self.ui.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.ui.tableWidget.setCellWidget(self.ui.tableWidget.rowCount() - 1, 0, self.ui.pushButton)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.settings.setValue("WindowSize", a0.size())


app = QApplication([])
application = LinksWindow()
application.show()
sys.exit(app.exec())
