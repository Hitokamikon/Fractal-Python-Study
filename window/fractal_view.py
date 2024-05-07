import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt
from pyqtgraph.opengl import *

class FractalView(QWidget):
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

            self.buttonsLayout = QVBoxLayout()
            self.buttonsLayout.setAlignment(Qt.AlignTop)

            buttons = QWidget()
            buttons.setLayout(self.buttonsLayout)
            scroll_area.setWidget(buttons)

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

            self.timer = QTimer(self)
            self.timer.timeout.connect(self.draw)
            self.timer.start(10)
            pass

      def draw(self) :
            pass
