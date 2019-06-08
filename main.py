# -*- coding: utf-8 -*-

import math
import sys
from gc import collect

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets

import mainwindow


# Class main form
class xolm(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ringView.rotate(180)
        self.graf_init()
        self.verticalLayout_2.addWidget(self.static_canvas)
        self.verticalLayout_2.addWidget(NavigationToolbar(self.static_canvas, self))
        self.h = 0.0005
        self.angle = 0
        self.ring = []
        self.deb = []

        self.buildButton.clicked.connect(self.buildButton_clicked)
        self.plusAngleButton.clicked.connect(self.plusAngleButton_clicked)
        self.clearGrafButton.clicked.connect(self.clearGrafButton_clicked)
        self.minusAngleButton.clicked.connect(self.minusAngleButton_clicked)

        bg = self.palette().window().color()
        cl = (bg.redF(), bg.greenF(), bg.blueF())

        self.fig = Figure(edgecolor = cl, facecolor = cl)
        self.canvas = FigureCanvas(self.fig)
        self.fig.clear()
        self.canvas.draw()

    def resizeEvent(self, event):
        self.ringDebTable.setColumnWidth(0, self.width() / 9)
        self.ringDebTable.setColumnWidth(1, self.width() / 8)
        self.ringDebTable.setColumnWidth(2, self.width() / 7)

    def graf_init(self):
        plt.close("all")
        self.graf = plt.figure()
        self.static_canvas = FigureCanvas(self.graf)
        self.new_dot = None
        plt.grid()

    def buildButton_clicked(self):
        self.angle = 0
        self.count = self.countRingSpinBox.value()
        # Gap from -pi to pi
        x = [x * self.h for x in range(-int(math.pi / self.h), int(math.pi / self.h))]
        y = []

        for X in x:
            summa = []
            for j in range(0, self.count):
                summa.append((self.count - j) / self.count * math.cos((j + 1)**(self.timeSpinBox.value() / 2) * X))
            y.append(sum(summa))
            summa.clear()

        self.xy_list = tuple(zip(x, y))
        plt.plot(x, y, linewidth=2)
        self.static_canvas.draw()

        min_y = min(y)
        max_y = max(y)
        self.maxLine.setText(str(round(min_y, 8)))
        self.minLine.setText(str(round(max_y, 8)))
        self.minMaxLine.setText(str(round((max_y / min_y), 8)))

        self.ring.clear()
        self.deb.clear()

        for i in range(0, self.count):
            self.ring.append(self.ringRadiusSpinBox.value() / (i + 1))
            self.deb.append(self.ringRadiusSpinBox.value() * (4 * (self.count - i) / ((i + 1)**2 * (self.count + 1)**2))**(1 / 3))

        self.ringDebTable.setRowCount(self.count + 1)
        count_row_tw = self.ringDebTable.rowCount()

        # Filling the table with calculations
        for row in range(0, count_row_tw - 1):
            ring_QTableWidgetItem = QtWidgets.QTableWidgetItem(str(round(float(self.ring[row]), 5)))
            deb_QTableWidgetItem = QtWidgets.QTableWidgetItem(str(round(float(self.deb[row]), 5)))
            average_QTableWidgetItem = QtWidgets.QTableWidgetItem(str(-(row - self.count) / self.count))
            self.ringDebTable.setItem(row, 0, ring_QTableWidgetItem)
            self.ringDebTable.setItem(row, 1, deb_QTableWidgetItem)
            self.ringDebTable.setItem(row, 2, average_QTableWidgetItem)

        self.new_PalletScene_paint()


    def plusAngleButton_clicked(self):
        if len(self.ring) > 0:
            self.angle = (self.angle + 5) % 360
            self.new_PalletScene_paint()
            self.paint_new_dot()


    def minusAngleButton_clicked(self):
        if len(self.ring) > 0:
            self.angle = (self.angle - 5) % 360
            self.new_PalletScene_paint()
            self.paint_new_dot()


    def clearGrafButton_clicked(self):
        self.graf.clf()
        if self.new_dot:
            for x in self.new_dot:
                x.remove()
        self.ring.clear()
        self.deb.clear()
        self.xy_list = []
        collect()
        plt.grid()
        self.static_canvas.draw()
        self.angle = 0


    def paint_new_dot(self):
        if self.new_dot:
            self.new_dot.pop(0).remove()
        radian_angle = math.radians(self.angle) - math.pi
        for X, Y, in self.xy_list:
            if abs(X - radian_angle) < 0.01:
                self.new_dot = plt.plot(X, Y, 'o', color=(0, 0, 0))
                self.static_canvas.draw()
                return


    def new_PalletScene_paint(self):
        PalletScene = QtWidgets.QGraphicsScene(0, 0, self.ringView.width(), self.ringView.height())
        self.ringView.setScene(PalletScene)
        self.ringView.setRenderHint(QtGui.QPainter.Antialiasing)
        if len(self.ring) > 0:
            scale = 200 / self.ring[0]
            x = y = 10
            # if 1: # if self.checkBox.isChecked():
            for i in range(0, self.count):
                PalletScene.addEllipse(x, y, self.ring[i] * scale, self.ring[i] * scale)
                PalletScene.addEllipse(x + scale * self.ring[0], y, self.ring[i] * scale, self.ring[i] * scale)
                if i != self.count - 1:
                    x += (scale * (self.ring[i] - self.ring[i + 1]) / 2)
                    y += self.ring[i] * scale

            x = y = 10 + scale * (self.ring[0] - self.deb[0]) / 2
            local_angle = self.angle
            for i in range(0, self.count):
                local_angle = -local_angle
                ge_item = QtWidgets.QGraphicsEllipseItem()
                ge_item.setStartAngle((i + 1) * (local_angle + 180) * 16)
                ge_item.setSpanAngle(2880)
                ge_item.setRect(x, y, self.deb[i] * scale, self.deb[i] * scale)
                ge_item.setPen(QtGui.QPen(QtGui.QColor(255, 0, 0), 1, QtCore.Qt.SolidLine))
                ge_item.setBrush(QtGui.QBrush(QtGui.QColor(255, 0, 0), QtCore.Qt.DiagCrossPattern))
                PalletScene.addItem(ge_item)
                if i != self.count - 1:
                    x += (self.deb[i] * scale - self.deb[i + 1] * scale) / 2
                    y += self.deb[i] * scale + (self.ring[i] * scale - self.deb[i] * scale) / 2 + (self.ring[i + 1] * scale - self.deb[i + 1] * scale) / 2

            x = 10 + scale * self.ring[0] + (self.ring[0] * scale - self.deb[0] * scale) / 2
            y = 10 + (self.ring[0] * scale - self.deb[0] * scale) / 2
            local_angle = self.angle
            for i in range(0, self.count):
                local_angle = -local_angle
                ge_item = QtWidgets.QGraphicsEllipseItem()
                ge_item.setStartAngle((i + 1) * -(local_angle + 180) * 16)
                ge_item.setSpanAngle(2880)
                ge_item.setRect(x, y, self.deb[i] * scale, self.deb[i] * scale)
                ge_item.setPen(QtGui.QPen(QtGui.QColor(255, 0, 0), 1, QtCore.Qt.SolidLine))
                ge_item.setBrush(QtGui.QBrush(QtGui.QColor(255, 0, 0), QtCore.Qt.DiagCrossPattern))
                PalletScene.addItem(ge_item)
                if i != self.count - 1:
                    x += (self.deb[i] * scale - self.deb[i + 1] * scale) / 2
                    y += self.deb[i] * scale + (self.ring[i] * scale - self.deb[i] * scale) / 2 + (self.ring[i + 1] * scale - self.deb[i + 1] * scale) / 2
            # else:

        PalletScene.setSceneRect(PalletScene.itemsBoundingRect())
        self.ringView.fitInView(PalletScene.sceneRect(), QtCore.Qt.KeepAspectRatio)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = xolm()
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
