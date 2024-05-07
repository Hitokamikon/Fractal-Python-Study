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
from ifsp_view import *
from julia_view import *
from mandelbrot_view import *
from newton_iteration_view import *

class MainWindow(QMainWindow): 
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("分形几何学习")

        tabs = QTabWidget()
        self.tabs = []

        tab1 = L_SystemView()
        tabs.addTab(tab1, 'L-系统')
        self.tabs.append(tab1)

        tab2 = Parameter_L_SystemView()
        tabs.addTab(tab2, '参数L-系统')
        self.tabs.append(tab2)

        tab3 = IFSView()
        tabs.addTab(tab3, 'IFS系统')
        self.tabs.append(tab3)

        tab4 = IFSPView()
        tabs.addTab(tab4, '概率IFS系统')
        self.tabs.append(tab4)

        tab5 = JuliaView()
        tabs.addTab(tab5, 'Julia集')
        self.tabs.append(tab5)

        tab6 = MandelbrotView()
        tabs.addTab(tab6, 'Mandelbrot集')
        self.tabs.append(tab6)

        tab7 = NewtonIterationView()
        tabs.addTab(tab7, '牛顿迭代')
        self.tabs.append(tab7)

        tabs.currentChanged.connect(self.tab_changed)
        self.tab_changed(0)

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
        pass

    def tab_changed(self , index):
        i = 0
        while i < len(self.tabs):
            if i == index:
                self.tabs[i].timer.start()
            else:
                self.tabs[i].timer.stop()
            i += 1

            pass
        pass

##  ============窗体测试程序 ============================
if  __name__ == "__main__": 
      app = QApplication(sys.argv)
      form = MainWindow() 
      form.resize(600,600)
      form.show()
      # form.showMaximized()
      sys.exit(app.exec_())

