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
        self.initMenus()
        self._dataTable = DataTableWidget(self)
        self.setCentralWidget(self._dataTable)
        self.show()

    def initMenus(self):
        menu = self.menuBar()
        fileMenu = menu.addMenu('&File')
        importTxtAction = QtGui.QAction('&Import txt', self)
        importTxtAction.triggered.connect(self.importTxt)
        fileMenu.addAction(importTxtAction)
        statisticsMenu = menu.addMenu('&Statistics')
        plotMenu = menu.addMenu('&Plot')

    def importTxt(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self,
            'Open text file',
            '/home/fritz/Code/Python/statistics/StatisticsTool/pystatstool',
            'Text files (*.txt *.csv)')
        data = pd.read_table(fileName[0], sep=';')
        self._dataTable.setData(data)



def main():
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()