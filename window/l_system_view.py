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
from l_system import *

class L_SystemView(QWidget):
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
            
            buttonsLayout.addWidget(self.create_button("科赫曲线"))
            buttonsLayout.addWidget(self.create_button("科赫雪花"))
            buttonsLayout.addWidget(self.create_button("谢尔宾斯基三角"))
            buttonsLayout.addWidget(self.create_button("谢尔宾斯基方毯"))
            buttonsLayout.addWidget(self.create_button("二次科赫岛"))
            buttonsLayout.addWidget(self.create_button("Pentigree分形"))
            buttonsLayout.addWidget(self.create_button("Peano L曲线"))
            buttonsLayout.addWidget(self.create_button("Peano R曲线"))
            buttonsLayout.addWidget(self.create_button("龙曲线"))
            buttonsLayout.addWidget(self.create_button("希尔伯特曲线"))
            buttonsLayout.addWidget(self.create_button("树"))
            buttonsLayout.addWidget(self.create_button("年龄树"))
            buttonsLayout.addWidget(self.create_button("鹦鹉螺"))
            buttonsLayout.addWidget(self.create_button("随机树"))

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
            self.fractal = None

            self.mytimer = QTimer(self)
            self.mytimer.timeout.connect(self.draw)
            self.mytimer.start(10)
            pass

      def draw(self) :
            if self.fractal == None:
                  return
            
            if self.curves == None:
                  self.result = self.fractal.axiom
                  self.curves = self.fractal.turtle.run(self.result)
                  self.line = GLLinePlotItem()
                  self.lines.append(self.line)
                  self.glWidget.addItem(self.line)
                  self.curve = []

            else:
                  if self.curve_id == len(self.curves) - 1:
                        if self.point_id == len(self.curves[self.curve_id]):    #升阶
                              self.order += 1
                              self.point_id = 0
                              self.curve_id = 0
                              self.scale *= self.ratio
                              self.result = self.fractal.system.produce(self.result)
                              self.curves = self.fractal.turtle.run(self.result)
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

      def begin_draw(self , fractal : L_SystemFractal , name : string , ratio : float):
            self.fractal = fractal
            self.name = name
            self.ratio = ratio
            self.curves = None

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
            if name == "科赫曲线":
                self.begin_draw(create_koch_curve() , "科赫曲线" , 3)
            elif name == "科赫雪花":
                self.begin_draw(create_koch_snowflake() , "科赫雪花" , 3)
            elif name == "谢尔宾斯基三角":
                self.begin_draw(create_sierpinski_triangle() , "谢尔宾斯基三角" , 3)
            elif name == "谢尔宾斯基方毯":
                self.begin_draw(create_sierpinski_carpet() , "谢尔宾斯基方毯" , 3)
            elif name == "二次科赫岛":
                self.begin_draw(create_second_koch_island() , "二次科赫岛" , 4)
            elif name == "Pentigree分形":
                self.begin_draw(create_pentigree() , "Pentigree分形" , 3)
            elif name == "Peano L曲线":
                self.begin_draw(create_peano_curve_l() , "Peano L曲线" , 3)
            elif name == "Peano R曲线":
                self.begin_draw(create_peano_curve_r() , "Peano R曲线" , 3)
            elif name == "龙曲线":
                self.begin_draw(create_dragon_curve() , "龙曲线" , 1)
            elif name == "希尔伯特曲线":
                self.begin_draw(create_hilbert_curve() , "希尔伯特曲线" , 2)
            elif name == "树":
                self.begin_draw(L_SystemFractal( Turtle(1,np.pi / 6), L_System([Production("f" , "f[-f]f[+f]f")]) , "+++f") , "树" , 3)
            elif name == "年龄树":
                self.begin_draw(L_SystemFractal( Turtle(1,np.pi / 4 , s = 0.5), L_System([Production("f" , "g[+f]-f")]) , "++f") , "年龄树" , 1)
            elif name == "鹦鹉螺":
                self.begin_draw(L_SystemFractal( Turtle(1,np.pi / 9 , s = 1), L_System([Production("f" , "h+h+h+h+h+h+") , Production("h" , "[g+g+g+g[---h-x]+++++g]") , Production("x" , "[g+g+g+g[---x]+++++g++++++++g]")]) , "ffff") , "鹦鹉螺" , 1.5)
            elif name == "随机树":
                self.begin_draw(L_SystemFractal( Turtle(1,np.pi / 8), L_System([Production("f" , "f[-f]f[+f]f" , p = 0.3333) , Production("f" , "f[-f]f[+f[-f]]" , p = 0.3333) , Production("f" , "ff+[+f-f-f]-[-f+f+f]" , p = 1)]) , "++++f") , "随机树" , 3)
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
