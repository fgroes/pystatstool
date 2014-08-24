import sys
import pandas as pd
from PySide import QtGui
from table import DataTableWidget


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('pystatstool')
        dt = DataTableWidget(self)
        data = pd.read_table('iris.txt', sep=';')
        dt.setData(data)
        dt.update()
        self.setCentralWidget(dt)
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()