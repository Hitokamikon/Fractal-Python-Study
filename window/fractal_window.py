import sys, math , threading
import time
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtChart import QChartView,QChart,QLineSeries,QValueAxis
from PyQt5.QtCore import QTimer

class QmyMainWindow(QMainWindow): 
   def __init__(self, parent=None):
      super().__init__(parent)
      self.setWindowTitle("分形几何学习")

      tabs = QTabWidget()
      tab1 = QWidget()
      tabs.addTab(tab1, 'L-系统')
      tab1.layout = QVBoxLayout()
      tab1.setLayout(tab1.layout)
      self.setCentralWidget(tabs)
      
##创建chart和chartView
      self.chart = QChart()               #创建 chart
      self.chart.setTitle("L-系统")
      chartView=QChartView(self)     #创建 chartView
      chartView.setChart(self.chart)      #chart添加到chartView
      tab1.layout.addWidget(chartView)
##创建曲线序列
      self.series0 = QLineSeries()
      self.series0.setName("Sin曲线")
      self.chart.addSeries(self.series0)       #序列添加到图表
##序列添加数值
      self.time=0
##创建坐标轴
      self.axisX = QValueAxis()      #x轴
      self.axisX.setRange(0, 10)     #设置坐标轴范围
      self.axisX.setTitleText("time(secs)")    #轴标题
      axisY = QValueAxis()      #y轴
      axisY.setRange(-2, 2)
      axisY.setTitleText("value")
##为序列设置坐标轴
      self.chart.setAxisX(self.axisX, self.series0)    #为序列series0设置坐标轴
      self.chart.setAxisY(axisY, self.series0)

      self.mytimer = QTimer(self)
      self.mytimer.timeout.connect(self.draw)
      self.mytimer.start(10)

   def draw(self) : 
      self.time += 0.01
      y1 = math.cos(self.time)
      self.series0.append(self.time,y1)
      self.axisX.setRange(0, self.time)     #设置坐标轴范围
      # self.chart.setAxisX(self.axisX, self.series0)    #为序列series0设置坐标轴
      pass

##  ============窗体测试程序 ============================
if  __name__ == "__main__": 
   app = QApplication(sys.argv)
   form = QmyMainWindow() 
   form.showMaximized()
   sys.exit(app.exec_())

