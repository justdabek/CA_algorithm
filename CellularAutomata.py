from Board import *

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CA_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from Image import *
from Board import *

import time

SIZE_WIDTH=100
SIZE_HEIGHT=100
SEEDS=200




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(557, 719)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(20, 20, 400, 400))
        self.Image.setText("")
        self.Image.setPixmap(QtGui.QPixmap("CA_img.png"))
        self.Image.setScaledContents(True)
        self.Image.setAlignment(QtCore.Qt.AlignCenter)
        self.Image.setWordWrap(False)
        self.Image.setObjectName("Image")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 460, 501, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.Play = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Play.setObjectName("Play")
        self.horizontalLayout.addWidget(self.Play)
        self.Play.setCheckable(True)
        self.Play.toggle()
        self.Play.clicked.connect(self.play_pause)

        self.Next = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Next.setObjectName("Next")
        self.horizontalLayout.addWidget(self.Next)
        self.Next.clicked.connect(self.next)

        self.Reset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Reset.setObjectName("Reset")
        self.horizontalLayout.addWidget(self.Reset)
        self.Reset.clicked.connect(self.reset)

        self.Dimensions = QtWidgets.QFrame(self.centralwidget)
        self.Dimensions.setGeometry(QtCore.QRect(20, 510, 111, 101))
        self.Dimensions.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Dimensions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Dimensions.setObjectName("Dimensions")

        self.X_edit = QtWidgets.QLineEdit(self.Dimensions)
        self.X_edit.setGeometry(QtCore.QRect(20, 40, 51, 20))
        self.X_edit.setObjectName("X_edit")
        self.X_edit.setText('5')

        self.Y_edit = QtWidgets.QLineEdit(self.Dimensions)
        self.Y_edit.setGeometry(QtCore.QRect(20, 70, 51, 20))
        self.Y_edit.setObjectName("Y_edit")
        self.Y_edit.setText('5')

        self.X = QtWidgets.QLabel(self.Dimensions)
        self.X.setGeometry(QtCore.QRect(10, 40, 16, 16))
        self.X.setObjectName("X")
        self.X_2 = QtWidgets.QLabel(self.Dimensions)
        self.X_2.setGeometry(QtCore.QRect(10, 70, 16, 16))
        self.X_2.setObjectName("X_2")

        self.Dimensions_2 = QtWidgets.QLabel(self.Dimensions)
        self.Dimensions_2.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.Dimensions_2.setObjectName("Dimensions_2")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 610, 111, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label.setObjectName("label")

        self.Seeds_edit = QtWidgets.QLineEdit(self.frame)
        self.Seeds_edit.setGeometry(QtCore.QRect(10, 30, 51, 20))
        self.Seeds_edit.setObjectName("Seeds_edit")
        self.Seeds_edit.setText('3')

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(130, 510, 181, 161))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.Method = QtWidgets.QLabel(self.frame_2)
        self.Method.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.Method.setObjectName("Method")

        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Moore")
        self.comboBox.addItem("Von Neumann")
        self.comboBox.addItem("Hexagonal left")
        self.comboBox.addItem("Hexagonal right")
        self.comboBox.addItem("Pentagonal left")
        self.comboBox.addItem("Pentagonal right")

        self.Inclusions = QtWidgets.QLabel(self.frame_2)
        self.Inclusions.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.Inclusions.setObjectName("Inclusions")

        self.Min_edit = QtWidgets.QLineEdit(self.frame_2)
        self.Min_edit.setGeometry(QtCore.QRect(40, 100, 51, 20))
        self.Min_edit.setObjectName("Min_edit")

        self.Max_edit = QtWidgets.QLineEdit(self.frame_2)
        self.Max_edit.setGeometry(QtCore.QRect(40, 130, 51, 20))
        self.Max_edit.setObjectName("Max_edit")

        self.Min = QtWidgets.QLabel(self.frame_2)
        self.Min.setGeometry(QtCore.QRect(10, 100, 31, 16))
        self.Min.setObjectName("Min")
        self.Max = QtWidgets.QLabel(self.frame_2)
        self.Max.setGeometry(QtCore.QRect(10, 130, 31, 16))
        self.Max.setObjectName("Max")

        self.Generate = QtWidgets.QPushButton(self.centralwidget)
        self.Generate.setGeometry(QtCore.QRect(330, 640, 191, 31))
        self.Generate.setObjectName("Generate")
        self.Generate.clicked.connect(self.generate)


        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(310, 510, 211, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.Import = QtWidgets.QPushButton(self.frame_3)
        self.Import.setGeometry(QtCore.QRect(30, 20, 75, 23))
        self.Import.setObjectName("Import")

        self.Export = QtWidgets.QPushButton(self.frame_3)
        self.Export.setGeometry(QtCore.QRect(120, 20, 75, 23))
        self.Export.setObjectName("Export")
        self.Export.clicked.connect(self.export)

        self.timer=QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.playstep)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.board=Board(200,200,20,MOORE_NEIGHBOURHOOD)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Play.setText(_translate("MainWindow", "Play/Pause"))
        self.Next.setText(_translate("MainWindow", "Next"))
        self.Reset.setText(_translate("MainWindow", "Reset"))
        self.X.setText(_translate("MainWindow", "X"))
        self.X_2.setText(_translate("MainWindow", "Y"))
        self.Dimensions_2.setText(_translate("MainWindow", "Dimensions"))
        self.label.setText(_translate("MainWindow", "Number of seeds"))
        self.Method.setText(_translate("MainWindow", "Method"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MOORE"))
        self.comboBox.setItemText(1, _translate("MainWindow", "VON NEUMANN"))
        self.comboBox.setItemText(2, _translate("MainWindow", "HEXAGONAL LEFT"))
        self.comboBox.setItemText(3, _translate("MainWindow", "HEXAGONAL RIGHT"))
        self.comboBox.setItemText(4, _translate("MainWindow", "PENTAGONAL LEFT"))
        self.comboBox.setItemText(5, _translate("MainWindow", "PENTAGONAL RIGHT"))
        self.Inclusions.setText(_translate("MainWindow", "Inclusions"))
        self.Min.setText(_translate("MainWindow", "Min"))
        self.Max.setText(_translate("MainWindow", "Max"))
        self.Generate.setText(_translate("MainWindow", "Generate"))
        self.Import.setText(_translate("MainWindow", "Import"))
        self.Export.setText(_translate("MainWindow", "Export"))

    def next(self):
        print("next")
        self.board.iteration()
        self.Image.setPixmap(QtGui.QPixmap("CA_img.png"))

    def play_pause(self):
        if self.Play.isChecked():
            self.timer.start()
        else:
            self.timer.stop()

    def playstep(self):
        empty=self.board.iteration()
        if(empty==0):
            self.timer.stop()
        self.refresh()

    def reset(self):
        img = Image.new('RGB', (100, 100))
        pixels = img.load()

        for j in range(0, 100):
            for i in range(0, 100):
                pixels[i, j] = colour_rule[0]
        img.save('CA_img.png')
        self.Image.setPixmap(QtGui.QPixmap("CA_img.png"))

    def combo_choose(self):
        temp = self.comboBox.currentText()
        if "MOORE" ==  temp:
            return MOORE_NEIGHBOURHOOD
        elif "VON NEUMANN" == temp:
            return VONNEUMANN_NEIGHBOURHOOD
        elif "HEXAGONAL LEFT" == temp:
            return HEXAGONAL_LEFT
        elif "HEXAGONAL RIGHT" == temp:
            return HEXAGONAL_RIGHT
        elif "PENTAGONAL LEFT" == temp:
            return PENTAGONAL_LEFT
        elif "PENTAGONAL RIGHT" == temp:
            return PENTAGONAL_RIGHT

    def generate(self):
        nrOfSeeds=self.Seeds_edit.text()
        X=self.X_edit.text()
        Y=self.Y_edit.text()
        Neighborhood=self.combo_choose()
        self.board=Board(int(X),int(Y),int(nrOfSeeds),Neighborhood)
        self.refresh()
        # self.reset()

    def export(self):
        self.board.writeToCSV()

    def refresh(self):
        self.board.updateBoard()
        self.Image.setPixmap(QtGui.QPixmap("CA_img.png"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#
