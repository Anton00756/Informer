import sys
from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import *
from compiled_ui.main_window import Ui_MainWindow
from disk_form import DiskForm
# from sqlitedict import SqliteDict
#
#
# def save(key, value, cache_file="data.sqlite3"):
#     try:
#         with SqliteDict(cache_file) as base_dict:
#             base_dict[key] = value
#             base_dict.commit()
#     except Exception as ex:
#         print("Error during storing data (Possibly unsupported):", ex)
#
#
# def load(key, cache_file="data.sqlite3"):
#     try:
#         with SqliteDict(cache_file) as base_dict:
#             value = base_dict[key]
#         return value
#     except Exception as ex:
#         print("Error during loading data:", ex)

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
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.tableWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)

        disks = self.settings.value('disks', [])
        self.ui.tableWidget.setRowCount(len(disks) + 1)
        for (index, disk) in enumerate(disks):
            new_disk = DiskForm(index, disk[0], disk[1], disk[2])
            new_disk.delete_row.connect(self.delete_disk)
            self.ui.tableWidget.setCellWidget(index, 0, new_disk)
        # for i in range(3):
        #     self.ui.tableWidget.setCellWidget(i, 0, DiskForm())
        #     self.ui.tableWidget.setRowHeight(i, 50)
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.ui.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap("images/add.jpg")))
        self.ui.pushButton.setIconSize(QtCore.QSize(40, 40))
        add_widget = QWidget()
        layout = QHBoxLayout(add_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui.pushButton)
        self.ui.tableWidget.setCellWidget(self.ui.tableWidget.rowCount() - 1, 0, add_widget)
        self.ui.pushButton.clicked.connect(self.add_new_disk_form)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.settings.setValue("WindowSize", a0.size())

    def add_new_disk_form(self):
        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount() - 1)
        new_disk = DiskForm(self.ui.tableWidget.rowCount() - 2)
        new_disk.delete_row.connect(self.delete_disk)
        self.ui.tableWidget.setCellWidget(self.ui.tableWidget.rowCount() - 2, 0, new_disk)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        disks = []
        for i in range(self.ui.tableWidget.rowCount() - 1):
            disks.append(self.ui.tableWidget.cellWidget(i, 0).to_file())
        self.settings.setValue('disks', disks)

    def delete_disk(self, index):
        for i in range(index + 1, self.ui.tableWidget.rowCount() - 1):
            self.ui.tableWidget.cellWidget(i, 0).index -= 1
        self.ui.tableWidget.removeRow(index)


app = QApplication([])
application = LinksWindow()
application.show()
sys.exit(app.exec())
