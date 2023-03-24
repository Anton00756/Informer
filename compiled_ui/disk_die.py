# Form implementation generated from reading ui file 'raw_ui/disk_die.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 50)
        Form.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(100,0,0);\n"
"    border-radius: 8px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                      stop: 0 #00aaff, stop: 1 rgb(100,255,100));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                      stop: 0 rgb(100,255,100), stop: 1 #00aaff);\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(100,0,0);\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background-color: rgb(100,255,100);\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.checkBox = QtWidgets.QCheckBox(parent=Form)
        self.checkBox.setStyleSheet("QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    background-color: qradialgradient(spread:pad, \n"
"                            cx:0.5,\n"
"                            cy:0.5,\n"
"                            radius:0.9,\n"
"                            fx:0.5,\n"
"                            fy:0.5,\n"
"                            stop:0 rgb(255, 0, 0), \n"
"                            stop:1 rgb(125, 0, 0));\n"
"    border-radius: 10px;\n"
"    border: 2px solid rgb(100,0,0);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: qradialgradient(spread:pad, \n"
"                            cx:0.5,\n"
"                            cy:0.5,\n"
"                            radius:0.9,\n"
"                            fx:0.5,\n"
"                            fy:0.5,\n"
"                            stop:0 rgba(0, 255, 0, 255), \n"
"                            stop:1 rgba(0, 64, 0, 255));\n"
"}")
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(255,0,0);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "URL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
