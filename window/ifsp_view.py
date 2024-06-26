import sys
import string
from PyQt5.QtWidgets import *
from pyqtgraph.opengl import *
from fractal_view import *

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'myproject/IFS'))
from ifsp2d import *

class IFSPView(FractalView):
      def __init__(self) -> None:
            super().__init__()
            
            self.buttonsLayout.addWidget(self.create_button("谢尔宾斯基三角"))
            self.buttonsLayout.addWidget(self.create_button("Box分形"))
            self.buttonsLayout.addWidget(self.create_button("分形蕨"))
            self.buttonsLayout.addWidget(self.create_button("枫叶"))

            self.points = list()
            self.scatter = GLScatterPlotItem()
            self.glWidget.addItem(self.scatter)
            self.ifsp = None
            pass

      def draw(self) :
            if self.ifsp == None:
                return
            self.result = self.ifsp.process_point(self.result)
            self.points.append((0 , self.result.x * 10 , self.result.y * 10))
            self.scatter.setData(pos = self.points , size = 2)
            pass

      def begin_draw(self , ifsp : IFSP2d , result : Point2D , name : string):
            self.ifsp = ifsp
            self.name = name
            self.result = result
            self.points.clear()
            self.points.append((0 , result.x * 10 , result.y * 10))
            self.scatter.setData(pos = self.points , size = 2)
            pass

      def begin_draw2(self , name : string):
            if name == "谢尔宾斯基三角":
                self.begin_draw(IFSP2d([(0.3333 , AffineTransform2d(0.5 , 0 , 0 , 0.5 , 0 , 0)) , 
                    (0.3333 , AffineTransform2d(0.5 , 0 , 0 , 0.5 , 0.5 , 0)) , 
                    (0.3335 , AffineTransform2d(0.5 , 0 , 0 , 0.5 , 0.5 , 0.5))
                    ]) , Point2D(0.75 , 0.25) , "谢尔宾斯基三角")
            if name == "Box分形":
                self.begin_draw(IFSP2d([(0.2 , AffineTransform2d(0.333 , 0 , 0 , 0.333 , 0 , 0)) , 
                    (0.2 , AffineTransform2d(0.333 , 0 , 0 , 0.333 , 0.666 , 0)) , 
                    (0.2 , AffineTransform2d(0.333 , 0 , 0 , 0.333 , 0.333 , 0.333)),
                    (0.2 , AffineTransform2d(0.333 , 0 , 0 , 0.333 , 0 , 0.666)),
                    (0.2 , AffineTransform2d(0.333 , 0 , 0 , 0.333 , 0.666 , 0.666)),
                    ]) , Point2D(0.75 , 0.25) , "Box分形")
            if name == "分形蕨":
                self.begin_draw(IFSP2d([(0.01 , AffineTransform2d(0 , 0 , 0 , 0.16 , 0 , 0)) , 
                    (0.85 , AffineTransform2d(0.85 , 0.1 , -0.05 , 0.85 , 0 , 0.6)) , 
                    (0.07 , AffineTransform2d(-0.2 , 0.26 , 0.23 , 0.22 , 0 , 0.6)),
                    (0.07 , AffineTransform2d(0.21 , -0.25 , 0.25 , 0.21 , 0 , 0.44)),
                    ]) , Point2D(0.75 , 0.25) , "分形蕨")
            if name == "枫叶":
                self.begin_draw(IFSP2d([(0.1 , AffineTransform2d(0.14 , 0.01 , 0 , 0.51 , -0.08 , -1.31)) , 
                    (0.35 , AffineTransform2d(0.43 , 0.52 , -0.45 , 0.5 , 1.49 , -0.75)) , 
                    (0.35 , AffineTransform2d(0.45 , -0.49 , 0.47 , 0.47 , -1.62 , -0.74)),
                    (1 , AffineTransform2d(0.49 , 0 , 0 , 0.51 , 0.02 , 1.62)),
                    ]) , Point2D(0.75 , 0.25) , "枫叶")
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
