from PyQt6 import QtCore, QtGui, QtWidgets
from compiled_ui.disk_die import Ui_Form
from webbrowser import open_new_tab
from requests import get


class DiskForm(QtWidgets.QWidget):
    yandex_icon = None
    google_icon = None
    close_icon = None
    delete_row = QtCore.pyqtSignal(int)

    def __init__(self, index, disk_type=True, url="", state=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.index = index
        self.is_google = disk_type
        if disk_type:
            self.ui.pushButton.setIcon(DiskForm.google_icon)
        else:
            self.ui.pushButton.setIcon(DiskForm.yandex_icon)
        self.ui.lineEdit.setText(url)
        self.ui.checkBox.setChecked(state)
        self.layout().setContentsMargins(5, 0, 5, 0)
        font = self.ui.lineEdit.font()
        font.setPointSize(13)
        self.ui.lineEdit.setFont(font)
        self.ui.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.ui.pushButton.setMinimumSize(35, 35)
        self.ui.pushButton.setMaximumSize(35, 35)
        self.ui.pushButton_2.setIcon(DiskForm.close_icon)
        self.ui.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.ui.pushButton_2.setMinimumSize(25, 25)
        self.ui.pushButton_2.setMaximumSize(25, 25)
        self.ui.checkBox.setMinimumSize(40, 35)
        self.ui.checkBox.setMaximumSize(40, 35)
        self.setMinimumWidth(200)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground, True)
        self.ui.pushButton.clicked.connect(self.open_link)
        self.ui.pushButton_2.clicked.connect(self.delete_disk)
        self.ui.checkBox.clicked.connect(self.change_state)

    def open_link(self):
        open_new_tab(self.ui.lineEdit.text().strip())

    def change_state(self):
        if self.ui.checkBox.isChecked():
            response = get(self.ui.lineEdit.text().strip())
            if response.status_code >= 400:
                self.ui.checkBox.setChecked(False)
                QtWidgets.QMessageBox.critical(self, 'Ошибка!', 'Некорректная ссылка!')

    def delete_disk(self):
        self.setParent(None)
        self.delete_row.emit(self.index)

    def contextMenuEvent(self, event):
        self.is_google = not self.is_google
        if self.is_google:
            self.ui.pushButton.setIcon(DiskForm.google_icon)
        else:
            self.ui.pushButton.setIcon(DiskForm.yandex_icon)

    def to_file(self):
        return [self.is_google, self.ui.lineEdit.text().strip(), self.ui.checkBox.isChecked()]
