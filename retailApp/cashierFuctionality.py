from cashierUi import CashierGui

from PyQt5.QtWidgets import (QHeaderView,QMessageBox)

from PyQt5.QtGui import (QStandardItemModel, QStandardItem)

from cart import Cart

from dataAccess import DataAccess 

accessData = DataAccess()

class cashierFunctions(CashierGui):

	productCart = Cart()

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

		code = self.productCode.text()

		qty = self.productQty.text()

		try:

			convertedQty = int(qty)

			self.validateProduct(code, convertedQty)
			self.productCode.clear()
			self.productQty.clear()

		except ValueError:

			QMessageBox.information(self,"InputError",
				"Quantity Input Must Be a Whole Number")

			self.productCode.clear()
			self.productQty.clear()
			

	def validateProduct(self, code ,qty):

		product = accessData.getProduct(code)

		if product == None:

			QMessageBox.information(self,"Product Error",
				"Product Record Not Found")

		else:

			cashierFunctions.productCart.prepareCart(product, qty, code)
			self.populateProductViewFields(product)

		#print(cashierFunctions.productCart)

	def makePurchase(self):

		pass

	def populateProductViewFields(self, productObject):

		self.currentProductName.setText(productObject.productName)
		self.currentProductDescription.setText(productObject.productDescription)
		self.currentProductPrice.setText(str(productObject.productPrice))
		


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

	