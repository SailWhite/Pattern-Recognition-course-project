# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\sailw\Desktop\PR\PRPJ\test\MLE.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MLE(object):
    def setupUi(self, MLE):
        MLE.setObjectName("MLE")
        MLE.resize(490, 253)
        self.widget = QtWidgets.QWidget(MLE)
        self.widget.setGeometry(QtCore.QRect(11, 11, 461, 235))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioNormal = QtWidgets.QRadioButton(self.widget)
        self.radioNormal.setChecked(True)
        self.radioNormal.setObjectName("radioNormal")
        self.verticalLayout.addWidget(self.radioNormal)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.radioUniform = QtWidgets.QRadioButton(self.widget)
        self.radioUniform.setObjectName("radioUniform")
        self.verticalLayout.addWidget(self.radioUniform)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.radioCustom = QtWidgets.QRadioButton(self.widget)
        self.radioCustom.setObjectName("radioCustom")
        self.verticalLayout.addWidget(self.radioCustom)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineTheta = QtWidgets.QLineEdit(self.widget)
        self.lineTheta.setObjectName("lineTheta")
        self.horizontalLayout.addWidget(self.lineTheta)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.linePx = QtWidgets.QLineEdit(self.widget)
        self.linePx.setObjectName("linePx")
        self.horizontalLayout_2.addWidget(self.linePx)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MLE)
        self.buttonBox.accepted.connect(MLE.accept)
        self.buttonBox.rejected.connect(MLE.reject)
        QtCore.QMetaObject.connectSlotsByName(MLE)

    def retranslateUi(self, MLE):
        _translate = QtCore.QCoreApplication.translate
        MLE.setWindowTitle(_translate("MLE", "MLE"))
        self.radioNormal.setText(_translate("MLE", "Normal"))
        self.radioUniform.setText(_translate("MLE", "Uniform"))
        self.radioCustom.setText(_translate("MLE", "Custom"))
        self.label.setText(_translate("MLE", "θ="))
        self.lineTheta.setText(_translate("MLE", "[[exec(\'globals()[\"miu\"]=sum(d)/len(d)\'),miu][1],sqrt(sum((x-miu)*(x-miu) for x in d)/len(d))]"))
        self.label_2.setText(_translate("MLE", "p(x)="))
        self.linePx.setText(_translate("MLE", "exp(-(x-θ[0])*(x-θ[0])/(2*θ[1]*θ[1]))/(sqrt(2*π)*θ[1])"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MLE = QtWidgets.QDialog()
    ui = Ui_MLE()
    ui.setupUi(MLE)
    MLE.show()
    sys.exit(app.exec_())

