import sys
from PyQt5.QtWidgets import *
from pyqtgraph.opengl import *

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'myproject/l-system'))
from l_system import *
from l_system_view import *

class MainWindow(QMainWindow): 
   def __init__(self, parent=None):
      super().__init__(parent)
      self.setWindowTitle("分形几何学习")

      tabs = QTabWidget()
      tab1 = L_SystemView()
      tabs.addTab(tab1, 'L-系统')
      self.setCentralWidget(tabs)
      

##  ============窗体测试程序 ============================
if  __name__ == "__main__": 
      app = QApplication(sys.argv)
      form = MainWindow() 
      form.resize(500,500)
      form.show()
      # form.showMaximized()
      sys.exit(app.exec_())

