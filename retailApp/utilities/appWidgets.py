from PyQt5.QtWidgets import (QFrame,QTableView,QAbstractItemView, QMenu, QAction)

from PyQt5.QtGui import QIcon

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

		self.removeProductAction = QAction()
		self.clearCartAction = QAction()
	def contextMenuEvent(self, event):

		menu = QMenu(self)

		self.removeProductAction.setText("Remove Product")
		self.removeProductAction.setIcon(QIcon("../images/remove.png"))

		self.clearCartAction.setText("Clear Cart")
		self.clearCartAction.setIcon(QIcon("../images/Clearcart.png"))

		menu.addAction(self.removeProductAction)
		menu.addAction(self.clearCartAction)

		menu.exec_(event.globalPos())



class userTableView(tableBluePrint):

	def __init__(self):

		super().__init__()


		self.removeUserAction = QAction()
		self.EditUserAction = QAction()
		self.DeleteUserAction = QAction()
	def contextMenuEvent(self, event):

		menu = QMenu(self)

		self.EditUserAction.setText("Edit User Details")
		self.EditUserAction.setIcon(QIcon("../images/edit.png"))

		self.DeleteUserAction.setText("Delete Cart")
		self.DeleteUserAction.setIcon(QIcon("../images/delete.png"))


		menu.addAction(self.EditUserAction)
		menu.addAction(self.DeleteUserAction)

		menu.exec_(event.globalPos())



class StockTableView(tableBluePrint):

	def __init__(self):

		super().__init__()


		self.removeProductAction = QAction()
		self.EditProductAction = QAction()
		self.DeleteProductAction = QAction()
	def contextMenuEvent(self, event):

		menu = QMenu(self)

		self.removeProductAction.setText("Remove Product")
		self.removeProductAction.setIcon(QIcon("../images/remove.png"))

		self.EditProductAction.setText("Edit Product Details")
		self.EditProductAction.setIcon(QIcon("../images/edit.png"))

		menu.addAction(self.removeProductAction)
		menu.addAction(self.EditProductAction)
		
		

		menu.exec_(event.globalPos())



	