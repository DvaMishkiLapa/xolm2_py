import sys
import math
from random import randint
from PyQt5 import QtWidgets, QtGui, QtChart, QtCore
import mainwindow

class xolm(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.graphicsView.rotate(180)

        self.chart = QtChart.QChart()
        self.chartView = QtChart.QChartView(self.chart)
        self.horizontalLayout.addWidget(self.chartView)

        self.h = 0.005

        self.angle = 0
        self.ring = []
        self.deb = []

        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        self.pushButton_3.clicked.connect(self.pushButton_3_clicked)
        self.pushButton_4.clicked.connect(self.pushButton_4_clicked)


    def pushButton_clicked(self):
        self.count = self.spinBox.value()
        x = [x * self.h for x in range(-int(math.pi / self.h), int(math.pi / self.h))]
        y = []

        self.series = QtChart.QLineSeries()
        i = 0
        for X in x:
            summa = []
            for j in range(0, self.count):
                summa.append((self.count - j) / self.count * math.cos((j + 1)**(self.doubleSpinBox.value() / 2) * X))
            y.append(sum(summa))
            summa.clear()
            self.series.append(x[i], y[-1])
            i += 1

        pen = QtGui.QPen()
        pen.setWidthF(1.2)
        pen.setBrush(QtGui.QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        self.series.setPen(pen)

        self.horizontalLayout.itemAt(1).widget().setParent(None)
        self.horizontalLayout.addWidget(self.chartView)

        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.series.setName("k = " + str(self.spinBox.value()) + ", \nr = " + str(int(self.doubleSpinBox_2.value())))
        self.chart.legend().setAlignment(QtCore.Qt.AlignBottom)
        self.chartView.setRenderHint(QtGui.QPainter.Antialiasing)

        min_y = min(y)
        max_y = max(y)

        self.lineEdit.setText(str(max_y))
        self.lineEdit_2.setText(str(min_y))
        self.lineEdit_3.setText(str(max_y / min_y))

        self.ring.clear()
        self.deb.clear()

        for i in range(0, self.count):
            self.ring.append(self.doubleSpinBox_2.value() / (i + 1))
            self.deb.append(self.doubleSpinBox_2.value() * (4 * (self.count - i) / ((i + 1)**2 * (self.count + 1)**2 ))**(1/3))

        self.tableWidget.setRowCount(self.count+1)
        self.tableWidget.setColumnCount(3)
        count_row_tw = self.tableWidget.rowCount()
        count_col_tw = self.tableWidget.columnCount()
        for row in range(0, count_row_tw):
            for col in range(0, count_col_tw):
                new_QTableWidgetItem = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(row, col, new_QTableWidgetItem)

        for row in range(0, count_row_tw-1):
            new1_QTableWidgetItem = QtWidgets.QTableWidgetItem(str(self.ring[row]))
            new2_QTableWidgetItem = QtWidgets.QTableWidgetItem(str(self.deb[row]))
            new3_QTableWidgetItem = QtWidgets.QTableWidgetItem(str(-(row - self.count) / self.count))
            self.tableWidget.setItem(row, 0, new1_QTableWidgetItem)
            self.tableWidget.setItem(row, 1, new2_QTableWidgetItem)
            self.tableWidget.setItem(row, 2, new3_QTableWidgetItem)

        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        name_table = ["Радиус\nколеса", "Радиус\nдебаланса", "Коэффициент"]
        self.tableWidget.setHorizontalHeaderLabels(name_table)

        self.new_PalletScene_paint()


    def pushButton_2_clicked(self):
        if len(self.ring) > 0:
            self.angle += 4
            self.new_PalletScene_paint()


    def pushButton_3_clicked(self):
        self.chart.removeAllSeries()


    def pushButton_4_clicked(self):
        if len(self.ring) > 0:
            self.angle -= 4
            self.new_PalletScene_paint()


    def new_PalletScene_paint(self):
        PalletScene = QtWidgets.QGraphicsScene(0, 0, self.graphicsView.width(), self.graphicsView.height())
        self.graphicsView.setScene(PalletScene)
        self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)
        if len(self.ring) > 0:
            scale = 200 / self.ring[0]
            x = y = 10
            # if 1: # if self.checkBox.isChecked():
            for i in range(0, self.count):
                PalletScene.addEllipse(x, y, self.ring[i]*scale, self.ring[i]*scale)
                # x += scale * self.ring[0]
                PalletScene.addEllipse(x + scale * self.ring[0], y, self.ring[i]*scale, self.ring[i]*scale)
                # x -= scale * self.ring[0]
                if i != self.count - 1:
                    x += (scale * (self.ring[i] - self.ring[i+1]) / 2)
                    y += self.ring[i] * scale

            x = y = 10 + scale * (self.ring[0] - self.deb[0]) / 2
            local_angle = self.angle
            for i in range(0, self.count):
                local_angle = -local_angle
                ge_item = QtWidgets.QGraphicsEllipseItem()
                ge_item.setStartAngle((i + 1) * local_angle * 16)
                ge_item.setSpanAngle(2880)
                ge_item.setRect(x, y, self.deb[i]*scale, self.deb[i]*scale)
                ge_item.setPen(QtGui.QPen(QtGui.QColor(255,0,0), 1, QtCore.Qt.SolidLine))
                ge_item.setBrush(QtGui.QBrush(QtGui.QColor(255,0,0), QtCore.Qt.DiagCrossPattern))
                PalletScene.addItem(ge_item)
                if i != self.count-1:
                    x += (self.deb[i] * scale - self.deb[i+1] * scale) / 2
                    y += self.deb[i] * scale + (self.ring[i] * scale - self.deb[i] * scale) / 2 + (self.ring[i+1] * scale - self.deb[i+1] * scale) / 2

            x = 10 + scale * self.ring[0] + (self.ring[0] * scale - self.deb[0] * scale) / 2
            y = 10 + (self.ring[0] * scale - self.deb[0] * scale) / 2
            local_angle = self.angle
            for i in range(0, self.count):
                local_angle = -local_angle
                ge_item = QtWidgets.QGraphicsEllipseItem()
                ge_item.setStartAngle((i + 1) * -local_angle * 16)
                ge_item.setSpanAngle(2880)
                ge_item.setRect(x, y, self.deb[i]*scale, self.deb[i]*scale)
                ge_item.setPen(QtGui.QPen(QtGui.QColor(255,0,0), 1, QtCore.Qt.SolidLine))
                ge_item.setBrush(QtGui.QBrush(QtGui.QColor(255,0,0), QtCore.Qt.DiagCrossPattern))
                PalletScene.addItem(ge_item)
                if i != self.count-1:
                    x += (self.deb[i] * scale - self.deb[i+1] * scale) / 2
                    y += self.deb[i] * scale + (self.ring[i] * scale - self.deb[i] * scale) / 2 + (self.ring[i+1] * scale - self.deb[i+1] * scale) / 2
            # else:

        PalletScene.setSceneRect(PalletScene.itemsBoundingRect())
        self.graphicsView.fitInView(PalletScene.sceneRect(), QtCore.Qt.KeepAspectRatio)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = xolm()
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main()