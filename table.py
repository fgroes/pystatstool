from PySide import QtCore, QtGui


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, parent=None):
        super(TableModel, self).__init__(parent)
        self._table = None

    def setTable(self, table):
        self._table = table
#        self.headerDataChanged(QtCore.Qt.Horizontal, 0, self.columnCount)

    def rowCount(self, parent=None):
        try:
            return self._table.shape[0]
        except:
            return 0

    def columnCount(self, parent=None):
        try:
            return self._table.shape[1]
        except:
            return 0

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None
        try:
            i = index.row()
            j = index.column()
            data = self._table.iloc[i, j]
            return str(data)
        except:
            return None

    def headerData(self, index, orientation, role=None):
        try:
            if role != QtCore.Qt.DisplayRole:
                return None
            if orientation == QtCore.Qt.Horizontal:
                return self._table.columns[int(index)]
            elif orientation == QtCore.Qt.Vertical:
                return index + 1
            else:
                return None
        except:
            return None


class TableView(QtGui.QTableView):

    def __init__(self, parent=None):
        super(TableModel, self).__init__(parent)


class DataTableWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        self._parent = parent
        super(DataTableWidget, self).__init__(self._parent)
        self.initUI()

    def setData(self, data):
        tableModel = TableModel()
        tableModel.setTable(data)
        self._tableView.setModel(tableModel)
        print('this is it', tableModel.headerData(0, QtCore.Qt.Horizontal))

    def initUI(self):
        tableModel = TableModel()
        self._tableView = QtGui.QTableView()
        self._tableView.setModel(tableModel)
        vbox = QtGui.QVBoxLayout(self)
        vbox.addWidget(self._tableView)
        self.show()
