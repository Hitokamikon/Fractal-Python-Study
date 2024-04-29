import sys
import string
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QWidget
import pyqtgraph as pg
from pyqtgraph.opengl import *

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'myproject/l-system'))
from parameter_l_system import *

class Parameter_L_SystemView(QWidget):
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

            self.lines = list[GLLinePlotItem]()
            self.system = None

            self.mytimer = QTimer(self)
            self.mytimer.timeout.connect(self.draw)
            self.mytimer.start(10)
            pass

      def draw(self) :
            if self.system == None:
                  return
            
            if self.curves == None:
                  self.result = self.axiom
                  self.curves = self.turtle.run(self.result)
                  self.line = GLLinePlotItem()
                  self.lines.append(self.line)
                  self.glWidget.addItem(self.line)
                  self.curve = []

            else:
                  if self.curve_id == len(self.curves) - 1:
                        if self.point_id == len(self.curves[self.curve_id]):    #升阶
                              self.turtle = ParameterTurtle(1 , np.pi / 2.1)
                              self.order += 1
                              self.point_id = 0
                              self.curve_id = 0
                              self.scale *= self.ratio
                              self.result = self.system.produce(self.result)
                              self.curves = self.turtle.run(self.result)
                              self.line = GLLinePlotItem()
                              self.lines.append(self.line)
                              self.glWidget.addItem(self.line)
                              self.curve = []
                        else:
                              point = self.curves[self.curve_id][self.point_id]
                              self.point_id += 1
                              self.curve.append((self.order * 5 , point[0] * 10 / self.scale , point[1] * 10 / self.scale))
                              self.line.setData(pos = self.curve)
                  else:
                        if self.point_id == len(self.curves[self.curve_id]):
                              self.curve_id += 1
                              self.point_id = 0
                              self.line = GLLinePlotItem()
                              self.lines.append(self.line)
                              self.glWidget.addItem(self.line)
                              self.curve = []
                        else:
                              point = self.curves[self.curve_id][self.point_id]
                              self.point_id += 1
                              self.curve.append((self.order * 5 , point[0] * 10 / self.scale , point[1] * 10 / self.scale))
                              self.line.setData(pos = self.curve)
                        pass
            pass

      def begin_draw(self , system : Parameter_L_System, axiom : list[Parameter] , name : string , ratio : float):
            self.system = system
            self.axiom = axiom
            self.name = name
            self.ratio = ratio
            self.curves = None
            self.turtle = ParameterTurtle(1 , np.pi / 2.1)

            self.point_id = 0
            self.curve_id = 0
            self.order = 1
            self.scale = 1
            

            for line in self.lines :
                 self.glWidget.removeItem(line)
                 pass
            self.lines.clear()
            pass

      def begin_draw2(self , name : string):
            if name == "1":
                self.begin_draw(Parameter_L_System([ParameterProduction(Parameter("f" , [1]) , lambda parameter : True , [
                    lambda p : Parameter("f" , [p.paras[0]]) , 
                    lambda p : Parameter("+" , []) , 
                    lambda p : Parameter("f" , [p.paras[0] * 2]) , 
                    lambda p : Parameter("-" , []) , 
                    lambda p : Parameter("-" , []) , 
                    lambda p : Parameter("f" , [p.paras[0] * 2]) , 
                    lambda p : Parameter("+" , []) , 
                    lambda p : Parameter("f" , [p.paras[0] * 4]) , 
                    ])]) , [Parameter("f" , [1])] , "1" , 1)
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
      
