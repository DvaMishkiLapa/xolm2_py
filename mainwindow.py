# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1260, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("font: 11pt \"Segoe UI\";")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 400))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_5.setHorizontalSpacing(6)
        self.gridLayout_5.setVerticalSpacing(2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 1, 2, 1, 1)
        self.maxLine = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxLine.sizePolicy().hasHeightForWidth())
        self.maxLine.setSizePolicy(sizePolicy)
        self.maxLine.setObjectName("maxLine")
        self.gridLayout_5.addWidget(self.maxLine, 2, 0, 1, 1)
        self.minLine = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minLine.sizePolicy().hasHeightForWidth())
        self.minLine.setSizePolicy(sizePolicy)
        self.minLine.setObjectName("minLine")
        self.gridLayout_5.addWidget(self.minLine, 2, 1, 1, 1)
        self.minMaxLine = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minMaxLine.sizePolicy().hasHeightForWidth())
        self.minMaxLine.setSizePolicy(sizePolicy)
        self.minMaxLine.setObjectName("minMaxLine")
        self.gridLayout_5.addWidget(self.minMaxLine, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 1, 0, 1, 1)
        self.ringDebTable = QtWidgets.QTableWidget(self.groupBox_3)
        self.ringDebTable.setGridStyle(QtCore.Qt.SolidLine)
        self.ringDebTable.setObjectName("ringDebTable")
        self.ringDebTable.setColumnCount(3)
        self.ringDebTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ringDebTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ringDebTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ringDebTable.setHorizontalHeaderItem(2, item)
        self.ringDebTable.horizontalHeader().setDefaultSectionSize(130)
        self.gridLayout_5.addWidget(self.ringDebTable, 0, 0, 1, 3)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(320, 175))
        self.groupBox.setMaximumSize(QtCore.QSize(320, 125))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(3, 11, 3, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.countRingSpinBox = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.countRingSpinBox.sizePolicy().hasHeightForWidth())
        self.countRingSpinBox.setSizePolicy(sizePolicy)
        self.countRingSpinBox.setMinimum(1)
        self.countRingSpinBox.setProperty("value", 7)
        self.countRingSpinBox.setObjectName("countRingSpinBox")
        self.gridLayout_2.addWidget(self.countRingSpinBox, 1, 1, 1, 1)
        self.timeSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeSpinBox.sizePolicy().hasHeightForWidth())
        self.timeSpinBox.setSizePolicy(sizePolicy)
        self.timeSpinBox.setProperty("value", 2.0)
        self.timeSpinBox.setObjectName("timeSpinBox")
        self.gridLayout_2.addWidget(self.timeSpinBox, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(320, 120))
        self.groupBox_2.setMaximumSize(QtCore.QSize(320, 95))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setContentsMargins(3, 11, 3, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radiuLlabel = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radiuLlabel.sizePolicy().hasHeightForWidth())
        self.radiuLlabel.setSizePolicy(sizePolicy)
        self.radiuLlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.radiuLlabel.setObjectName("radiuLlabel")
        self.gridLayout_3.addWidget(self.radiuLlabel, 0, 0, 1, 1)
        self.stepLabel = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepLabel.sizePolicy().hasHeightForWidth())
        self.stepLabel.setSizePolicy(sizePolicy)
        self.stepLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stepLabel.setObjectName("stepLabel")
        self.gridLayout_3.addWidget(self.stepLabel, 0, 1, 1, 1)
        self.ringRadiusSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.ringRadiusSpinBox.setDecimals(5)
        self.ringRadiusSpinBox.setMaximum(1000.0)
        self.ringRadiusSpinBox.setProperty("value", 200.0)
        self.ringRadiusSpinBox.setObjectName("ringRadiusSpinBox")
        self.gridLayout_3.addWidget(self.ringRadiusSpinBox, 1, 0, 1, 1)
        self.stepSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.stepSpinBox.setEnabled(False)
        self.stepSpinBox.setObjectName("stepSpinBox")
        self.gridLayout_3.addWidget(self.stepSpinBox, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(320, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(320, 16777215))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setContentsMargins(3, 11, 3, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.clearGrafButton = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearGrafButton.sizePolicy().hasHeightForWidth())
        self.clearGrafButton.setSizePolicy(sizePolicy)
        self.clearGrafButton.setObjectName("clearGrafButton")
        self.gridLayout_4.addWidget(self.clearGrafButton, 1, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox.setEnabled(False)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_4.addWidget(self.checkBox, 0, 0, 1, 2)
        self.minusAngleButton = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minusAngleButton.sizePolicy().hasHeightForWidth())
        self.minusAngleButton.setSizePolicy(sizePolicy)
        self.minusAngleButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.minusAngleButton.setAutoRepeat(True)
        self.minusAngleButton.setAutoRepeatInterval(50)
        self.minusAngleButton.setObjectName("minusAngleButton")
        self.gridLayout_4.addWidget(self.minusAngleButton, 1, 2, 1, 1)
        self.buildButton = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buildButton.sizePolicy().hasHeightForWidth())
        self.buildButton.setSizePolicy(sizePolicy)
        self.buildButton.setObjectName("buildButton")
        self.gridLayout_4.addWidget(self.buildButton, 1, 0, 1, 1)
        self.plusAngleButton = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plusAngleButton.sizePolicy().hasHeightForWidth())
        self.plusAngleButton.setSizePolicy(sizePolicy)
        self.plusAngleButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.plusAngleButton.setAutoRepeat(True)
        self.plusAngleButton.setAutoRepeatInterval(50)
        self.plusAngleButton.setObjectName("plusAngleButton")
        self.gridLayout_4.addWidget(self.plusAngleButton, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ringView = QtWidgets.QGraphicsView(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ringView.sizePolicy().hasHeightForWidth())
        self.ringView.setSizePolicy(sizePolicy)
        self.ringView.setMinimumSize(QtCore.QSize(450, 0))
        self.ringView.setMaximumSize(QtCore.QSize(400, 16777215))
        self.ringView.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.ringView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ringView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ringView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ringView.setObjectName("ringView")
        self.verticalLayout_3.addWidget(self.ringView)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "xolm2_py"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Результаты"))
        self.label_7.setText(_translate("MainWindow", "min"))
        self.label_8.setText(_translate("MainWindow", "max/min"))
        self.label_6.setText(_translate("MainWindow", "max"))
        item = self.ringDebTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Радиус колеса"))
        item = self.ringDebTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Радиус дебаланса"))
        item = self.ringDebTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Коэффициент"))
        self.groupBox.setTitle(_translate("MainWindow", "Параметры функции"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Количество звеньев</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Время действия (α)</p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Радиус колеса"))
        self.radiuLlabel.setText(_translate("MainWindow", "Начальный радиус"))
        self.stepLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Шаг уменьшения<br/>радиуса</p></body></html>"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Построение"))
        self.clearGrafButton.setText(_translate("MainWindow", "Очистить"))
        self.checkBox.setText(_translate("MainWindow", "Зубчатая передача"))
        self.minusAngleButton.setText(_translate("MainWindow", "<<"))
        self.buildButton.setText(_translate("MainWindow", "Построить"))
        self.plusAngleButton.setText(_translate("MainWindow", ">>"))

