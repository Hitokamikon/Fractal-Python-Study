import sys
import string
from PyQt5.QtWidgets import *
from pyqtgraph.opengl import *
from fractal_view import *

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'myproject/Newton Iteration'))
from newton_iteration import *

class NewtonIterationView(FractalView):
      def __init__(self) -> None:
            super().__init__()

            self.buttonsLayout.addWidget(self.create_button("z³-1"))

            self.points = list()
            self.scatter = GLScatterPlotItem()
            self.glWidget.addItem(self.scatter)
            self.a = None
            self.interval = 0.01
            pass

      def draw(self) :
            if self.a == None:
                return
            value = newton_iteration_judge(self.a , self.c , self.N , self.epsilon)
            if value == self.N:
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

      def begin_draw(self ,  a : list[complex] , N : int , epsilon : float , name : string):
            self.name = name
            self.a = a
            self.c = complex(0,0)
            self.N = N
            self.epsilon = epsilon
            self.points.clear()
            pass

      def begin_draw2(self ,  name : string):
            if name == "z³-1":
                self.begin_draw([complex(-1,0) , complex(0,0) , complex(0,0) , complex(1,0)] , 9 , 0.00001 , "z³-1")
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
