from .cashierUi import CashierGui

from PyQt5.QtWidgets import (QHeaderView,QMessageBox,QTableWidgetItem)

from PyQt5.QtGui import (QStandardItemModel, QStandardItem)

from .cart import Cart

from dataAccess import DataAccess 

from dialogs import addCreditorDialog

accessData = DataAccess()

class cashierFunctions(CashierGui):

	
	def __init__(self):

		super().__init__()

		self.initiateFunctionality()

		self.productCart = Cart()


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

			QMessageBox.warning(self,"InputError",
				"Quantity Input Must Be a Whole Number")

			self.productCode.clear()
			self.productQty.clear()
			

	def validateProduct(self, code ,qty):

		product = accessData.getProduct(code)

		if product == None:

			QMessageBox.warning(self,"Product Error",
				"Product Record Not Found")

		else:


			if product.productQuantity > qty:


				self.productCart.prepareCart(product, qty, code)

				self.populateProductViewFields(product, qty)
				self.updateTableView()

			else:

				QMessageBox.warning(self, "Stock Error", 
					"Out Of Stock", QMessageBox.Ok, QMessageBox.Ok)


	def makePurchase(self):

		if len(self.productCart) == 0:

			QMessageBox.warning(self, "Transaction Error", 
				"The cart is empty", QMessageBox.Ok, QMessageBox.Ok)

		else:

			sender = self.sender()
			paymentMethod = sender.text()
			totals = self.productCart.calculateTotal()

			if paymentMethod == "CashPayment":

				pass

			else:

				pass

	def populateProductViewFields(self, productObject, Qty):

		self.currentProductName.setText(productObject.productName)
		self.currentProductDescription.setText(productObject.productDescription)
		self.currentProductPrice.setText(str(productObject.productPrice))

		details = self.productCart.calculateCost(productObject.categoryVat,
				productObject.categoryDiscount,
				productObject.productPrice, Qty)

		self.productVatView.setText(str(details[0]))
		self.productDiscount.setText(str(details[1]))
		self.productUnitPrice.setText(str(details[2]))
		self.productTotalPrice.setText(str(details[3]))

		self.totalPayoutLabel.setText(str(self.productCart.calculateTotal()))
	
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


	def updateTableView(self):

		productDetails = self.prepareProductDetails()

		self.tableModel.setRowCount(len(productDetails))

		for row in range(len(productDetails)):

			for column in range(len(productDetails[row])):

				item = QStandardItem(str(productDetails[row][column]))

				self.tableModel.setItem(row, column, item)


	def prepareProductDetails(self):

		details = []

		for items in self.productCart:

			for detail in items:

				details.append(items.get(detail))


		return details


