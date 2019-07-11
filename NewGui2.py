from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 771, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.label_3.hide()
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.hide()
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setRange(4,6)
        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.pushButton_41 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_41.setObjectName("pushButton_41")
        self.gridLayout.addWidget(self.pushButton_41, 1, 4, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 80, 500, 400))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_17 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_17.setText("")
        self.pushButton_17.hide()
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_2.addWidget(self.pushButton_17, 0, 4, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 3, 1, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 3, 2, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_2.addWidget(self.pushButton_16, 3, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_18.setText("")
        self.pushButton_18.hide()
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_2.addWidget(self.pushButton_18, 1, 4, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_20.setText("")
        self.pushButton_20.hide()
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_2.addWidget(self.pushButton_20, 3, 4, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.pushButton_13, 3, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 3, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_21.setText("")
        self.pushButton_21.hide()
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_2.addWidget(self.pushButton_21, 4, 0, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_22.setText("")
        self.pushButton_22.hide()
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_2.addWidget(self.pushButton_22, 4, 1, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_23.setText("")
        self.pushButton_23.hide()
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_2.addWidget(self.pushButton_23, 4, 2, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_24.setText("")
        self.pushButton_24.hide()
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_2.addWidget(self.pushButton_24, 4, 3, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_25.setText("")
        self.pushButton_25.hide()
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_2.addWidget(self.pushButton_25, 4, 4, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_26.setText("")
        self.pushButton_26.hide()
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_2.addWidget(self.pushButton_26, 0, 5, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_27.setText("")
        self.pushButton_27.hide()
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_2.addWidget(self.pushButton_27, 1, 5, 1, 1)
        self.pushButton_28 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_28.setText("")
        self.pushButton_28.hide()
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout_2.addWidget(self.pushButton_28, 2, 5, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_19.setText("")
        self.pushButton_19.hide()
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_2.addWidget(self.pushButton_19, 2, 4, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_29.setText("")
        self.pushButton_29.hide()
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_2.addWidget(self.pushButton_29, 3, 5, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_30.setText("")
        self.pushButton_30.hide()
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_2.addWidget(self.pushButton_30, 4, 5, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 1, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 2, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 2, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 2, 3, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_31.setText("")
        self.pushButton_31.hide()
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout_2.addWidget(self.pushButton_31, 5, 0, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_32.setText("")
        self.pushButton_32.hide()
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout_2.addWidget(self.pushButton_32, 5, 1, 1, 1)
        self.pushButton_33 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_33.setText("")
        self.pushButton_33.hide()
        self.pushButton_33.setObjectName("pushButton_33")
        self.gridLayout_2.addWidget(self.pushButton_33, 5, 2, 1, 1)
        self.pushButton_34 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_34.setText("")
        self.pushButton_34.hide()
        self.pushButton_34.setObjectName("pushButton_34")
        self.gridLayout_2.addWidget(self.pushButton_34, 5, 3, 1, 1)
        self.pushButton_35 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_35.setText("")
        self.pushButton_35.hide()
        self.pushButton_35.setObjectName("pushButton_35")
        self.gridLayout_2.addWidget(self.pushButton_35, 5, 4, 1, 1)
        self.pushButton_36 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_36.setText("")
        self.pushButton_36.hide()
        self.pushButton_36.setObjectName("pushButton_36")
        self.gridLayout_2.addWidget(self.pushButton_36, 5, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setText("")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 2, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(530, 80, 251, 401))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 500, 771, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_40 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_40.setObjectName("pushButton_40")
        self.horizontalLayout.addWidget(self.pushButton_40)
        self.pushButton_39 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_39.setObjectName("pushButton_39")
        self.horizontalLayout.addWidget(self.pushButton_39)
        self.pushButton_38 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_38.setObjectName("pushButton_38")
        self.horizontalLayout.addWidget(self.pushButton_38)
        self.pushButton_37 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_37.setObjectName("pushButton_37")
        self.horizontalLayout.addWidget(self.pushButton_37)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.buttonBoard = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5,
                            self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9, self.pushButton_10, 
                            self.pushButton_11, self.pushButton_12, self.pushButton_13, self.pushButton_14, self.pushButton_15, 
                            self.pushButton_16, self.pushButton_17, self.pushButton_18, self.pushButton_19, self.pushButton_20, 
                            self.pushButton_21, self.pushButton_22, self.pushButton_23, self.pushButton_24, self.pushButton_25, 
                            self.pushButton_26, self.pushButton_27, self.pushButton_28, self.pushButton_29, self.pushButton_30, 
                            self.pushButton_31, self.pushButton_32, self.pushButton_33, self.pushButton_34, self.pushButton_35,
                            self.pushButton_36]

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Size:"))
        self.label_2.setText(_translate("MainWindow", "Custom:"))
        self.label_3.setText(_translate("MainWindow", "(enter all letters as one string)"))
        self.pushButton_41.setText(_translate("MainWindow", "Generate"))
        self.pushButton_40.setText(_translate("MainWindow", "Run"))
        self.pushButton_39.setText(_translate("MainWindow", "Stop"))
        self.pushButton_38.setText(_translate("MainWindow", "New Board"))
        self.pushButton_37.setText(_translate("MainWindow", "Exit"))

        self.spinBox.valueChanged.connect(lambda: self.updateBoard(self.spinBox.value()))
        self.checkBox.stateChanged.connect(lambda: self.updateCustom())

    def updateBoard(self, n):
        for i in self.buttonBoard:
            i.hide()
        for i in range(n**2):
            self.buttonBoard[i].show()

    def updateCustom(self):
        if self.checkBox.isChecked():
            self.lineEdit.show()
            self.label_3.show()
        else:
            self.lineEdit.hide()
            self.label_3.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

