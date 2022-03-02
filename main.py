from PySide2.QtWidgets import QApplication

from ui_main import Ui_TabWidget

class MainWindow(Ui_TabWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_TabWidget()
        self.ui.Btn_autotest.clicked.connect(self.Btn_autotest)

    def f_btn_autotest(self):
        pass
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app = QApplication()
    gui = MainWindow()
    app.ui.show(gui)
    app.exec_()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
