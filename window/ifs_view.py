import sys
import string
from PyQt5.QtWidgets import *
from pyqtgraph.opengl import *
from fractal_view import *

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'myproject/IFS'))
from ifs2d import *

class IFSView(FractalView):
      def __init__(self) -> None:
            super().__init__()
            
            self.buttonsLayout.addWidget(self.create_button("1"))

            self.points = list()
            self.scatter = GLScatterPlotItem()
            self.glWidget.addItem(self.scatter)
            self.ifs = None
            pass

      def draw(self) :
            if self.ifs == None:
                return
            if self.point_id == len(self.result) - 1:
                if self.omega_id == len(self.ifs.omegas):
                    self.result = self.new_result.copy()
                    self.point_id = 0
                    self.omega_id = 0
                    self.order += 1
                    pass
                else:
                    point = self.ifs.omegas[self.omega_id].transform(self.result[-1])
                    self.new_result.append(point)
                    self.points.append((self.order * 5 , point.x  * 10 , point.y * 10))
                    self.scatter.setData(pos = self.points , size = 2)
                    self.omega_id += 1
                    pass
            else:
                if self.omega_id == len(self.ifs.omegas):
                    self.point_id += 1
                    self.omega_id = 0
                    pass
                else:
                    point = self.ifs.omegas[self.omega_id].transform(self.result[self.point_id])
                    self.new_result.append(point)
                    self.points.append((self.order * 5 , point.x * 10 , point.y * 10))
                    self.scatter.setData(pos = self.points , size = 2)
                    self.omega_id += 1
                    self.point_id += 1
                    pass
            pass

      def begin_draw(self , ifs : IFS2d , result : list[Point2D] , name : string):
            self.ifs = ifs
            self.name = name
            self.result = result
            self.new_result = []
            self.order = 0
            self.point_id = 0
            self.omega_id = 0
            self.points.clear()
            self.scatter.setData(pos = [])
            pass

      def begin_draw2(self , name : string):
            if name == "1":
                self.begin_draw(IFS2d([AffineTransform2d(0.5 , 0 , 0 , 0.5 , 0 , 0) , AffineTransform2d(0.5 , 0 , 0 , 0.5 , 0.5 , 0) , AffineTransform2d(0.5 , 0 , 0 , 0.5 , 0.5 , 0.5)]) , [Point2D(0.75 , 0.25)] , "1")
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
