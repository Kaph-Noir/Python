# not yet
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class SimpleWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Simple Window")
        self.setGeometry(300, 300, 300, 400)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = SimpleWindow()
    myWindow.show()
    app.exec_()