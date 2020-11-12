from PyQt5.QtWidgets import (QFrame,QTableView,QAbstractItemView, QMenu)

class tableBluePrint(QTableView):

	def __init__(self):

		super().__init__()

		self.tableProperties()

	def tableProperties(self):

		self.setFrameShape(QFrame.StyledPanel)
		self.setFrameShadow(QFrame.Plain)
		self.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.setSelectionMode(QAbstractItemView.SingleSelection)
		self.verticalHeader().setVisible(False)


class cartTableView(tableBluePrint):

	def __init__(self):

		super().__init__()


	def contextMenuEvent(self, event):

		menu = QMenu(self)

		action = menu.addAction("Remove Product")

		menu.exec_(event.globalPos())