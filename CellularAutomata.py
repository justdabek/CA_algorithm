
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CA_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from Image import *
from PyQt5.QtGui import QImage, QColor

from Board import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(547, 778)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.phase=0

        self.img_png = QImage("CA_img.png")
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(50, 10, 430, 430))
        self.Image.setText("")
        self.Image.setPixmap(QtGui.QPixmap("CA_img.png"))
        self.Image.setScaledContents(True)
        self.Image.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.Image.setWordWrap(False)
        self.Image.setObjectName("Image")
        self.Image.mousePressEvent = self.onclick

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
        self.Dimensions.setGeometry(QtCore.QRect(20, 510, 111, 91))
        self.Dimensions.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Dimensions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Dimensions.setObjectName("Dimensions")

        self.X_edit = QtWidgets.QLineEdit(self.Dimensions)
        self.X_edit.setGeometry(QtCore.QRect(20, 20, 51, 20))
        self.X_edit.setObjectName("X_edit")
        self.X_edit.setText('100')

        self.Y_edit = QtWidgets.QLineEdit(self.Dimensions)
        self.Y_edit.setGeometry(QtCore.QRect(20, 50, 51, 20))
        self.Y_edit.setObjectName("Y_edit")
        self.Y_edit.setText('100')

        self.X = QtWidgets.QLabel(self.Dimensions)
        self.X.setGeometry(QtCore.QRect(10, 20, 16, 16))
        self.X.setObjectName("X")
        self.Y = QtWidgets.QLabel(self.Dimensions)
        self.Y.setGeometry(QtCore.QRect(10, 50, 16, 16))
        self.Y.setObjectName("Y")

        self.Dimensions_2 = QtWidgets.QLabel(self.Dimensions)
        self.Dimensions_2.setGeometry(QtCore.QRect(10, 0, 61, 16))
        self.Dimensions_2.setObjectName("Dimensions_2")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 590, 111, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.NrOfSeeds = QtWidgets.QLabel(self.frame)
        self.NrOfSeeds.setGeometry(QtCore.QRect(10, 0, 101, 16))
        self.NrOfSeeds.setObjectName("NrOfSeeds")

        self.Seeds_edit = QtWidgets.QLineEdit(self.frame)
        self.Seeds_edit.setGeometry(QtCore.QRect(10, 20, 51, 20))
        self.Seeds_edit.setObjectName("Seeds_edit")
        self.Seeds_edit.setText('30')

        self.NrOfInclusions = QtWidgets.QLabel(self.frame)
        self.NrOfInclusions.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.NrOfInclusions.setObjectName("NrOfInclusions")

        self.Inclusions_edit = QtWidgets.QLineEdit(self.frame)
        self.Inclusions_edit.setGeometry(QtCore.QRect(10, 60, 51, 20))
        self.Inclusions_edit.setObjectName("Inclusions_edit")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(130, 500, 181, 181))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.Method = QtWidgets.QLabel(self.frame_2)
        self.Method.setGeometry(QtCore.QRect(10, 0, 47, 13))
        self.Method.setObjectName("Method")

        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Moore")
        self.comboBox.addItem("Von Neumann")
        self.comboBox.addItem("Hexagonal left")
        self.comboBox.addItem("Hexagonal right")
        self.comboBox.addItem("Pentagonal left")
        self.comboBox.addItem("Pentagonal right")

        self.radioButton_Torus = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_Torus.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.radioButton_Torus.setObjectName("radioButton")
        self.radioButton_Torus.setChecked(True)
        self.radioButton_Border = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_Border.setGeometry(QtCore.QRect(70, 60, 82, 17))
        self.radioButton_Border.setObjectName("radioButton_2")

        self.Inclusions = QtWidgets.QLabel(self.frame_2)
        self.Inclusions.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.Inclusions.setObjectName("Inclusions - radius")

        self.Min_edit = QtWidgets.QLineEdit(self.frame_2)
        self.Min_edit.setGeometry(QtCore.QRect(50, 110, 51, 20))
        self.Min_edit.setObjectName("Min_edit")

        self.Max_edit = QtWidgets.QLineEdit(self.frame_2)
        self.Max_edit.setGeometry(QtCore.QRect(50, 150, 51, 20))
        self.Max_edit.setObjectName("Max_edit")

        self.Min = QtWidgets.QLabel(self.frame_2)
        self.Min.setGeometry(QtCore.QRect(10, 110, 31, 16))
        self.Min.setObjectName("Min")

        self.Max = QtWidgets.QLabel(self.frame_2)
        self.Max.setGeometry(QtCore.QRect(10, 150, 31, 16))
        self.Max.setObjectName("Max")

        self.Generate = QtWidgets.QPushButton(self.centralwidget)
        self.Generate.setGeometry(QtCore.QRect(310, 690, 201, 51))
        self.Generate.setObjectName("Generate")
        self.Generate.clicked.connect(self.generate)


        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(310, 510, 211, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.Import = QtWidgets.QPushButton(self.frame_3)
        self.Import.setGeometry(QtCore.QRect(10, 10, 91, 23))
        self.Import.setObjectName("Import")
        self.Import.clicked.connect(self.importCSV)

        self.Export = QtWidgets.QPushButton(self.frame_3)
        self.Export.setGeometry(QtCore.QRect(110, 10, 91, 23))
        self.Export.setObjectName("Export")
        self.Export.clicked.connect(self.exportCSV)

        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(310, 550, 211, 61))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        self.Probability_edit = QtWidgets.QLineEdit(self.frame_4)
        self.Probability_edit.setGeometry(QtCore.QRect(70, 0, 51, 20))
        self.Probability_edit.setObjectName("Probability_edit")
        self.Probability = QtWidgets.QLabel(self.frame_4)
        self.Probability.setGeometry(QtCore.QRect(10, 0, 61, 21))
        self.Probability.setObjectName("Probability")

        self.GBC = QtWidgets.QCheckBox(self.frame_4)
        self.GBC.setGeometry(QtCore.QRect(10, 30, 70, 17))
        self.GBC.setObjectName("checkBox")
        self.GBC.stateChanged.connect(self.GBCstate)

        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(310, 610, 211, 71))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")

        self.GetBoundries = QtWidgets.QPushButton(self.frame_5)
        self.GetBoundries.setGeometry(QtCore.QRect(10, 0, 91, 23))
        self.GetBoundries.setObjectName("GetBoundries")
        self.GetBoundries.clicked.connect(self.getBoundries)
        self.boundry_length = QtWidgets.QLabel(self.frame_5)
        self.boundry_length.setGeometry(QtCore.QRect(20, 30, 47, 13))
        self.boundry_length.setObjectName("boundry_length")
        self.mean_size = QtWidgets.QLabel(self.frame_5)
        self.mean_size.setGeometry(QtCore.QRect(20, 50, 121, 16))
        self.mean_size.setObjectName("mean_size")

        self.boundry_length_value = QtWidgets.QLabel(self.frame_5)
        self.boundry_length_value.setGeometry(QtCore.QRect(70, 30, 47, 13))
        self.boundry_length_value.setText("")
        self.boundry_length_value.setObjectName("boundry_length_value")

        self.mean_size_value = QtWidgets.QLabel(self.frame_5)
        self.mean_size_value.setGeometry(QtCore.QRect(140, 50, 51, 16))
        self.mean_size_value.setText("")
        self.mean_size_value.setObjectName("mean_size_value")

        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(20, 680, 281, 71))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.Substructures = QtWidgets.QPushButton(self.frame_6)
        self.Substructures.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.Substructures.setObjectName("Substructures")
        self.Substructures.clicked.connect(self.substructures)
        self.DualPhase = QtWidgets.QPushButton(self.frame_6)
        self.DualPhase.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.DualPhase.setObjectName("DualPhase")
        self.DualPhase.clicked.connect(self.dualPhase)
        self.Delete = QtWidgets.QCheckBox(self.frame_6)
        self.Delete.setGeometry(QtCore.QRect(110, 10, 70, 17))
        self.Delete.setObjectName("Delete")
        self.phase_label = QtWidgets.QLabel(self.frame_6)
        self.phase_label.setGeometry(QtCore.QRect(110, 40, 47, 13))
        self.phase_label.setObjectName("phase_label")
        self.phase_label_disp = QtWidgets.QLabel(self.frame_6)
        self.phase_label_disp.setGeometry(QtCore.QRect(150, 40, 47, 13))
        self.phase_label_disp.setObjectName("phase_label_disp")


        self.timer=QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.playstep)




        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.board=Board(200,200,20,MOORE_NEIGHBOURHOOD,True,(0,0),0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Play.setText(_translate("MainWindow", "Play/Pause"))
        self.Next.setText(_translate("MainWindow", "Next"))
        self.Reset.setText(_translate("MainWindow", "Reset"))
        self.X.setText(_translate("MainWindow", "X"))
        self.X_edit.setText(_translate("MainWindow","250"))
        self.Y.setText(_translate("MainWindow", "Y"))
        self.Y_edit.setText(_translate("MainWindow","250"))
        self.Dimensions_2.setText(_translate("MainWindow", "Dimensions"))
        self.NrOfSeeds.setText(_translate("MainWindow", "Number of seeds"))
        self.Seeds_edit.setText(_translate("MainWindow","200"))
        self.NrOfInclusions.setText(_translate("MainWindow", "Number of inclusions"))
        self.Inclusions_edit.setText(_translate("MainWindow","0"))
        self.Method.setText(_translate("MainWindow", "Method"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MOORE"))
        self.comboBox.setItemText(1, _translate("MainWindow", "VON NEUMANN"))
        self.comboBox.setItemText(2, _translate("MainWindow", "HEXAGONAL LEFT"))
        self.comboBox.setItemText(3, _translate("MainWindow", "HEXAGONAL RIGHT"))
        self.comboBox.setItemText(4, _translate("MainWindow", "PENTAGONAL LEFT"))
        self.comboBox.setItemText(5, _translate("MainWindow", "PENTAGONAL RIGHT"))
        self.GBC.setText(_translate("MainWindow", "GBC"))
        self.Probability.setText(_translate("MainWindow", "Probability"))



        self.Inclusions.setText(_translate("MainWindow", "Inclusions - radius"))
        self.Min_edit.setText(_translate("MainWindow", "1"))
        self.Max_edit.setText(_translate("MainWindow", "10"))
        self.Min.setText(_translate("MainWindow", "Min"))
        self.Max.setText(_translate("MainWindow", "Max"))
        self.radioButton_Torus.setText(_translate("MainWindow", "Torus"))
        self.radioButton_Border.setText(_translate("MainWindow", "Boundry"))
        self.Generate.setText(_translate("MainWindow", "Generate"))
        self.Import.setText(_translate("MainWindow", "Import"))
        self.Export.setText(_translate("MainWindow", "Export"))
        self.Probability_edit.setText(_translate("MainWindow", "50"))
        self.GetBoundries.setText(_translate("MainWindow", "Get boundaries"))
        self.boundry_length.setText(_translate("MainWindow", "Length:"))
        self.mean_size.setText(_translate("MainWindow", "Mean size of the grain:"))
        self.Substructures.setText(_translate("MainWindow", "Substructures"))
        self.DualPhase.setText(_translate("MainWindow", "Dual-Phase"))
        self.Delete.setText(_translate("MainWindow", "Delete"))
        self.phase_label.setText(_translate("MainWindow", "Phase:"))
        self.phase_label_disp.setText(_translate("MainWindow", " "))


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

        for i in range(0, 100):
            for j in range(0, 100):
                pixels[i, j] = color_rule[0]
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
        self.phase=0
        self.phase_label_disp.setText(str(self.phase))
        nrOfSeeds=self.Seeds_edit.text()
        X=self.X_edit.text()
        Y=self.Y_edit.text()
        Neighborhood=self.combo_choose()
        min_r_incl=self.Min_edit.text()
        max_r_incl=self.Max_edit.text()
        nrOfInclusions=self.Inclusions_edit.text()
        if(self.radioButton_Border.isChecked()):
            border=True
        else:
            border=False

        self.board=Board(int(X),int(Y),int(nrOfSeeds),Neighborhood,border,(int(min_r_incl),int(max_r_incl)),int(nrOfInclusions))
        if(self.GBC.isChecked()):
            self.board.setCurvature(True, int(self.Probability_edit.text()))
        else:
            self.board.setCurvature(False, 0)

        self.refresh()

    def substructures(self):
        self.board.addSeeds(int(self.Seeds_edit.text()),0)
        self.refresh()

    def dualPhase(self):
        self.phase+=1
        self.board.addSeeds(int(self.Seeds_edit.text()),self.phase)
        self.phase_label_disp.setText(str(self.phase))
        self.refresh()

    def exportCSV(self):
        self.board.writeToCSV()

    def importCSV(self):
        self.board.importFromCSV()
        self.refresh()

    def refresh(self):
        self.board.updateBoard()
        self.Image.setPixmap(QtGui.QPixmap("CA_img.png"))

    def GBCstate(self):
        if(self.GBC.isChecked()):
            self.comboBox.setCurrentText("MOORE")
            self.comboBox.setEnabled(False)
        else:
            self.comboBox.setEnabled(True)

    def getBoundries(self):
        length=self.board.markBoundries()
        size=int(self.board.dimX*self.board.dimY/self.board.seeds)
        self.boundry_length_value.setText(str(length))
        self.mean_size_value.setText(str(size))
        self.refresh()


    def onclick(self,event):
        print('you pressed', event.pos().x(), event.pos().y())
        x=event.pos().x()*self.board.dimX/430
        y=event.pos().y()*self.board.dimY/430
        self.img_png = QImage("CA_img.png")
        c=self.img_png.pixel(int(x),int(y))
        c_rgb = QColor(c).getRgb()
        if (self.Delete.isChecked()):
            self.board.removeSeed(c_rgb[:3])
            self.refresh()
        else:
            pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())