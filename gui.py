import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from ui.main_window import Ui_MainWindow


class GUI:
    def __init__(self):
        # Setting up GUI
        self.app = QApplication()

        self.window = QMainWindow()
        self.window.setFixedSize(self.window.size())

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

    def start(self):
        self.window.show()
        sys.exit(self.app.exec())
