import sys
from PyQt5.QtWidgets import *
from pyqtgraph.opengl import *

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'myproject/l-system'))
from l_system import *
from l_system_view import *
from parameter_l_system_view import *
from ifs_view import *

class MainWindow(QMainWindow): 
   def __init__(self, parent=None):
      super().__init__(parent)
      self.setWindowTitle("分形几何学习")

      tabs = QTabWidget()
      tab1 = L_SystemView()
      tabs.addTab(tab1, 'L-系统')
      tab2 = Parameter_L_SystemView()
      tabs.addTab(tab2, '参数L-系统')
      tab3 = IFSView()
      tabs.addTab(tab3, 'IFS系统')

      self.setCentralWidget(tabs)
      tabs.setStyleSheet("""
            QTabBar::tab {
                width: 80px;    /* 设置选项卡宽度 */
                height: 20px;    /* 设置选项卡高度 */
                min-width: 80px; /* 设置选项卡最小宽度 */
                max-width: 120px; /* 设置选项卡最大宽度 */
                margin: 2px;     /* 设置选项卡边距 */
                padding: 5px;    /* 设置选项卡内边距 */
            }
        """)

##  ============窗体测试程序 ============================
if  __name__ == "__main__": 
      app = QApplication(sys.argv)
      form = MainWindow() 
      form.resize(600,600)
      form.show()
      # form.showMaximized()
      sys.exit(app.exec_())

