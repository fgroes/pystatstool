import sys
import pandas as pd
from PySide import QtGui
from table import DataTableWidget


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.init_ui()
        self._data_tables = {}

    def init_ui(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('pystatstool')
        self.init_menus()
        self._table_views = CentralWidget(self)
        self.setCentralWidget(self._table_views)
        self.show()

    def init_menus(self):
        menu = self.menuBar()
        file_menu = menu.addMenu('&File')
        import_txt_action = QtGui.QAction('&Import txt', self)
        import_txt_action.triggered.connect(self._import_txt)
        file_menu.addAction(import_txt_action)
        statistics_menu = menu.addMenu('&Statistics')
        describe_action = QtGui.QAction('&Describe', self)
        describe_action.triggered.connect(self._describe)
        statistics_menu.addAction(describe_action)
        plot_menu = menu.addMenu('&Plot')

    def _add_table(self, table_name, table):
        if table_name in self._data_tables:
            print('reloading table not implemented')
        else:
            self._data_tables[table_name] = table
            self._table_views.add_data_table(table_name, table)

    def _import_txt(self):
        file_name = QtGui.QFileDialog.getOpenFileName(self,
            'Open text file',
            '/home/fritz/Code/Python/statistics/StatisticsTool/pystatstool',
            'Text files (*.txt *.csv)')
        data = pd.read_table(file_name[0], sep=';')
        self._add_table(file_name[0], data)

    def _describe(self):
        table_name = self._table_views.current_table_name()
        description = self._data_tables[table_name].describe()
        new_table_name = 'description: {0}'.format(table_name)
        self._add_table(new_table_name, description)


class CentralWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        vbox = QtGui.QVBoxLayout()
        self._tables = Tables(self)
        vbox.addWidget(self._tables)
        self.setLayout(vbox)

    def add_data_table(self, label, data):
        self._tables.add_data_table(label, data)

    def current_table_name(self):
        return self._tables.current_table_name()


class Tables(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Tables, self).__init__(parent)
        self.init_ui()
        self._table_idxs = {}

    def init_ui(self):
        self._table_combo = QtGui.QComboBox(self)
        self._table_combo.currentIndexChanged.connect(self._table_selected)
        self._stacked_tables = QtGui.QStackedWidget(self)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self._table_combo)
        layout.addWidget(self._stacked_tables)
        self.setLayout(layout)

    def add_data_table(self, label, data):
        if label in self._table_idxs:
            print('reloading table not implemented')
        else:
            data_table = DataTableWidget(self)
            data_table.set_data(data)
            table_idx = self._stacked_tables.addWidget(data_table)
            self._table_idxs[label] = table_idx
            self._table_combo.addItem(label)
            combo_idx = self._table_combo.findText(label)
            self._table_combo.setCurrentIndex(combo_idx)

    def _table_selected(self, index):
        table_name = self._table_combo.itemText(index)
        idx = self._table_idxs[table_name]
        self._stacked_tables.setCurrentIndex(idx)

    def current_table_name(self):
        return self._table_combo.currentText()


def main():
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()