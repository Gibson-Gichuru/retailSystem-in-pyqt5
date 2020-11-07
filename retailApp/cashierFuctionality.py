from cashierUi import CashierGui

from PyQt5.QtWidgets import (QHeaderView)

from PyQt5.QtGui import QStandardItemModel, QStandardItem


class cashierFunctions(CashierGui):

	def __init__(self):

		super().__init__()

		self.initiateFunctionality()

	def initiateFunctionality(self):

		self.productCode.returnPressed.connect(self.getProduct)
		self.productQty.returnPressed.connect(self.getProduct)

		self.cashPayment.clicked.connect(self.makePurchase)
		self.creditPayment.clicked.connect(self.makePurchase)

		self.setUpTable()

	def getProduct(self):

		pass

	def makePurchase(self):

		pass


	def setUpTable(self):

		columns = ["Product Code","Product Name", "Product Description",
		"Unit Price", "Total Price"]

		self.tableModel = QStandardItemModel()

		self.cartTable.setModel(self.tableModel)

		self.tableModel.setHorizontalHeaderLabels(columns)

		header = self.cartTable.horizontalHeader()

		header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
		header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
		header.setSectionResizeMode(2, QHeaderView.Stretch)
		header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
		header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
	



	

