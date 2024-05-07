import sys
import string
from PyQt5.QtWidgets import *
from pyqtgraph.opengl import *
from fractal_view import *

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'myproject/Mandelbrot'))
from mandelbrot import *

class MandelbrotView(FractalView):
      def __init__(self) -> None:
            super().__init__()

            self.buttonsLayout.addWidget(self.create_button("25"))

            self.points = list()
            self.scatter = GLScatterPlotItem()
            self.glWidget.addItem(self.scatter)
            self.c = None
            self.interval = 0.01
            pass

      def draw(self) :
            if self.c == None:
                return
            julia = mandelbrot_set_judge(self.N , self.c)
            if julia == self.N:
                self.points.append((0 , self.c.real , self.c.imag))
                self.scatter.setData(pos = self.points , size = 2)

            if self.c.imag - self.c.real >= 0:
                if self.c.imag + self.c.real >= 0:
                    self.c += complex(self.interval,0)
                else:
                    self.c += complex(0,self.interval)
            else:
                if self.c.imag + self.c.real >= 0:
                    self.c -= complex(0,self.interval)
                else:
                    self.c -= complex(self.interval,0)
                
            pass

      def begin_draw(self , N : int , name : string):
            self.name = name
            self.N = N
            self.c = complex(0,0)
            self.points.clear()
            pass

      def begin_draw2(self , name : string):
            if name == "25":
                self.begin_draw(25 , "25")
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
