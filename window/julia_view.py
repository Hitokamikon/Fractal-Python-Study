import sys
import string
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QWidget
import pyqtgraph as pg
from pyqtgraph.opengl import *
import numpy as np

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'myproject/Julia'))
from julia import *

class JuliaView(QWidget):
      def __init__(self) -> None:
            super().__init__()
            self.layout = QHBoxLayout()
            self.setLayout(self.layout)

      ##创建左侧按钮栏

            vLayout = QVBoxLayout()
            self.layout.addLayout(vLayout)
            vLayout.setAlignment(Qt.AlignTop)

            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setFixedWidth(250)
            vLayout.addWidget(scroll_area)

            buttonsLayout = QVBoxLayout()
            buttonsLayout.setAlignment(Qt.AlignTop)

            buttons = QWidget()
            buttons.setLayout(buttonsLayout)
            scroll_area.setWidget(buttons)
            
            buttonsLayout.addWidget(self.create_button("1"))
            buttonsLayout.addWidget(self.create_button("2"))


            self.glWidget = GLViewWidget()
            self.glWidget.setBackgroundColor(0,0,0)
            self.layout.addWidget(self.glWidget)

      ## 创建坐标轴
            self.xgrid = GLGridItem()
            self.ygrid = GLGridItem()
            self.zgrid = GLGridItem()
            self.glWidget.addItem(self.xgrid)
            self.glWidget.addItem(self.ygrid)
            self.glWidget.addItem(self.zgrid)

            self.xgrid.rotate(90, 0, 1, 0)
            self.ygrid.rotate(90, 1, 0, 0)

            self.xgrid.scale(1, 1, 1)
            self.ygrid.scale(1, 1, 1)
            self.zgrid.scale(1, 1, 1)

            self.points = list()
            self.scatter = GLScatterPlotItem()
            self.glWidget.addItem(self.scatter)
            self.c = None
            self.interval = 0.01

            self.mytimer = QTimer(self)
            self.mytimer.timeout.connect(self.draw)
            self.mytimer.start(10)
            pass

      def draw(self) :
            if self.c == None:
                return
            julia = fill_julia_set_judge(self.N , self.c , self.point)
            if julia == self.N:
                self.points.append((0 , self.point.real , self.point.imag))
                self.scatter.setData(pos = self.points , size = 2)

            if self.point.imag - self.point.real >= 0:
                if self.point.imag + self.point.real >= 0:
                    self.point += complex(self.interval,0)
                else:
                    self.point += complex(0,self.interval)
            else:
                if self.point.imag + self.point.real >= 0:
                    self.point -= complex(0,self.interval)
                else:
                    self.point -= complex(self.interval,0)
                
            pass

      def begin_draw(self , c : complex , N : int , name : string):
            self.c = c
            self.name = name
            self.N = N
            self.point = complex(0,0)
            self.points.clear()
            pass

      def begin_draw2(self , name : string):
            if name == "1":
                self.begin_draw(complex(-0.95 , 0.1) , 25 , "1")
            if name == "2":
                self.begin_draw(complex(-0.14 , 0.72) , 25 , "2")
            pass
    
      def create_button(self , text : string) -> QPushButton: 
            button = QPushButton()
            button.setText(text)
            button.setFixedWidth(200)
            button.setFixedHeight(50)
            font = button.font()
            font.setPixelSize(20)
            button.setFont(font)
            button.clicked.connect(lambda : self.begin_draw2(text))
            return button
