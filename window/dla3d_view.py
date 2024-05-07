import sys
import string
from PyQt5.QtWidgets import *
from pyqtgraph.opengl import *
from fractal_view import *

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'myproject/DLA'))
from dla3d import *

class DLA3dView(FractalView):
      def __init__(self) -> None:
            super().__init__()

            self.buttonsLayout.addWidget(self.create_button("DLA"))

            self.points = list()
            self.colors = list()
            self.scatter = GLScatterPlotItem()
            self.glWidget.addItem(self.scatter)
            self.dla = None
            pass

      def draw(self) :
            if self.dla == None:
                return
            self.dla.run()
            self.points.clear()
            self.colors.clear()
            self.points.append((self.dla.practicle[0] , self.dla.practicle[1] , self.dla.practicle[2]))
            self.colors.append((1,0,0,1))

            for p in self.dla.seeds:
                  self.points.append((p[0] , p[1] , p[2]))
                  self.colors.append((1,1,1,1))

            self.scatter.setData(pos = self.points)

      def begin_draw(self , dla : DLA3d , name : string):
            self.dla = dla
            self.name = name
            
            self.points.clear()
            self.scatter.setData(pos = [])
            pass

      def begin_draw2(self , name : string):
            if name == "DLA":
                dla = DLA3d(5)
                self.begin_draw(dla , "DLA")
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
