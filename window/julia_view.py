import sys
import string
from PyQt5.QtWidgets import *
from pyqtgraph.opengl import *
from fractal_view import *

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'myproject/Julia'))
from julia import *

class JuliaView(FractalView):
      def __init__(self) -> None:
            super().__init__()

            self.buttonsLayout.addWidget(self.create_button("1"))
            self.buttonsLayout.addWidget(self.create_button("2"))
            
            self.points = list()
            self.scatter = GLScatterPlotItem()
            self.glWidget.addItem(self.scatter)
            self.c = None
            self.interval = 0.01
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
