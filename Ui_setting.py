# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\sailw\Desktop\PR\PRPJ\test\setting.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_setting(object):
    def setupUi(self, setting):
        setting.setObjectName("setting")
        setting.resize(334, 174)
        self.widget = QtWidgets.QWidget(setting)
        self.widget.setGeometry(QtCore.QRect(20, 20, 291, 133))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkDwD = QtWidgets.QCheckBox(self.widget)
        self.checkDwD.setChecked(True)
        self.checkDwD.setObjectName("checkDwD")
        self.verticalLayout.addWidget(self.checkDwD)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineStepD = QtWidgets.QLineEdit(self.widget)
        self.lineStepD.setObjectName("lineStepD")
        self.horizontalLayout.addWidget(self.lineStepD)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(setting)
        self.buttonBox.accepted.connect(setting.accept)
        self.buttonBox.rejected.connect(setting.reject)
        QtCore.QMetaObject.connectSlotsByName(setting)

    def retranslateUi(self, setting):
        _translate = QtCore.QCoreApplication.translate
        setting.setWindowTitle(_translate("setting", "Setting"))
        self.checkDwD.setText(_translate("setting", "Do not draw PDF while dragging"))
        self.label.setText(_translate("setting", "dx=(xb-xa)/"))
        self.lineStepD.setText(_translate("setting", "1000"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setting = QtWidgets.QDialog()
    ui = Ui_setting()
    ui.setupUi(setting)
    setting.show()
    sys.exit(app.exec_())

