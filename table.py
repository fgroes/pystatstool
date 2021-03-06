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
                return self._table.index[int(index)]
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
        self.init_ui()

    def init_ui(self):
        tableModel = TableModel()
        self._table_view = QtGui.QTableView()
        self._table_view.setModel(tableModel)
        vbox = QtGui.QVBoxLayout(self)
        vbox.addWidget(self._table_view)
        self.show()

    def set_data(self, data):
        table_model = TableModel()
        table_model.setTable(data)
        self._table_view.setModel(table_model)
