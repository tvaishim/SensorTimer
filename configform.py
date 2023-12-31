# Form implementation generated from reading ui file 'configform.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 208)
        self.mqttServer = QtWidgets.QLineEdit(parent=Dialog)
        self.mqttServer.setGeometry(QtCore.QRect(90, 15, 214, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mqttServer.setFont(font)
        self.mqttServer.setObjectName("mqttServer")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 47, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.mqttTopic = QtWidgets.QLineEdit(parent=Dialog)
        self.mqttTopic.setGeometry(QtCore.QRect(90, 90, 291, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mqttTopic.setFont(font)
        self.mqttTopic.setObjectName("mqttTopic")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(32, 52, 47, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.mqttPort = QtWidgets.QLineEdit(parent=Dialog)
        self.mqttPort.setGeometry(QtCore.QRect(314, 15, 66, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mqttPort.setFont(font)
        self.mqttPort.setObjectName("mqttPort")
        self.mqttPassword = QtWidgets.QLineEdit(parent=Dialog)
        self.mqttPassword.setGeometry(QtCore.QRect(240, 52, 140, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mqttPassword.setFont(font)
        self.mqttPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.mqttPassword.setObjectName("mqttPassword")
        self.mqttUser = QtWidgets.QLineEdit(parent=Dialog)
        self.mqttUser.setGeometry(QtCore.QRect(90, 52, 140, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mqttUser.setFont(font)
        self.mqttUser.setObjectName("mqttUser")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(21, 15, 60, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.btnOK = QtWidgets.QPushButton(parent=Dialog)
        self.btnOK.setGeometry(QtCore.QRect(193, 169, 90, 30))
        self.btnOK.setObjectName("btnOK")
        self.btnCancel = QtWidgets.QPushButton(parent=Dialog)
        self.btnCancel.setGeometry(QtCore.QRect(291, 169, 90, 30))
        self.btnCancel.setObjectName("btnCancel")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(22, 128, 54, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.mqttExpire = QtWidgets.QLineEdit(parent=Dialog)
        self.mqttExpire.setGeometry(QtCore.QRect(90, 128, 116, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mqttExpire.setFont(font)
        self.mqttExpire.setObjectName("mqttExpire")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.mqttServer.setPlaceholderText(_translate("Dialog", "Server"))
        self.label_3.setText(_translate("Dialog", "Topic:"))
        self.mqttTopic.setPlaceholderText(_translate("Dialog", "Topic"))
        self.label_2.setText(_translate("Dialog", "User:"))
        self.mqttPort.setPlaceholderText(_translate("Dialog", "Port"))
        self.mqttPassword.setPlaceholderText(_translate("Dialog", "Password"))
        self.mqttUser.setPlaceholderText(_translate("Dialog", "User"))
        self.label.setText(_translate("Dialog", "Server:"))
        self.btnOK.setText(_translate("Dialog", "OK"))
        self.btnCancel.setText(_translate("Dialog", "Cancel"))
        self.label_4.setText(_translate("Dialog", "Expire:"))
        self.mqttExpire.setPlaceholderText(_translate("Dialog", "Expire after"))
