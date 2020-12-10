from PyQt5.QtWidgets import (QVBoxLayout, QFrame, QPushButton, QWidget,
	QLabel, QHBoxLayout, QGroupBox, QLineEdit,QHeaderView)


from PyQt5.QtGui import (QIcon, QFont, QStandardItemModel, QStandardItem)

from PyQt5.QtCore import Qt, QSize

from utilities import (registeredUserTable, stockTable, accessDatabase,
	addUser, ph)


class tabBluePrint(QWidget):

	def __init__(self):

		super().__init__()

		self.initiateUi()


	def initiateUi(self):

		font = QFont()
		font.setBold(True)
		font.setPointSize(16)
		font.setWeight(50)

		mainLayout = QHBoxLayout()

		self.setLayout(mainLayout)

		optionFrame = QFrame()

		optionFrame.setFrameShape(QFrame.StyledPanel)
		optionFrame.setFrameShadow(QFrame.Plain)

		optionFrameLayout = QVBoxLayout()

		optionFrame.setLayout(optionFrameLayout)

		self.searchGroupBox = QGroupBox()
		self.searchGroupBox.setFlat(True)
		self.searchGroupBox.setFont(font)
		
		searchGroupBoxLayout = QHBoxLayout()

		self.searchGroupBox.setLayout(searchGroupBoxLayout)

		self.searchLineEdit = QLineEdit()

		self.searchButton = QPushButton()
		self.searchButton.setObjectName("searchButton")
		self.searchButton.setIcon(QIcon("../images/search.png"))

		searchGroupBoxLayout.addWidget(self.searchLineEdit)
		searchGroupBoxLayout.addWidget(self.searchButton)

		searchGroupBoxLayout.setStretch(0,3)
		searchGroupBoxLayout.setStretch(2,4)


		optionFrameLayout.addWidget(self.searchGroupBox)

		self.optionButtonGroupBox = QGroupBox()
		self.optionButtonGroupBox.setFlat(True)
		self.optionButtonGroupBox.setFont(font)

		optionButtonGroupBoxLayout = QVBoxLayout()

		self.optionButtonGroupBox.setLayout(optionButtonGroupBoxLayout)

		self.addButton = QPushButton()
		self.addButton.setObjectName("optionButton")

		self.editButton = QPushButton()
		self.editButton.setObjectName("optionButton")

		self.deleteButton = QPushButton()
		self.deleteButton.setObjectName("optionButton")

		optionButtonGroupBoxLayout.addWidget(self.addButton)
		optionButtonGroupBoxLayout.addWidget(self.editButton)
		optionButtonGroupBoxLayout.addWidget(self.deleteButton)

		optionFrameLayout.addWidget(self.optionButtonGroupBox)

		optionFrameLayout.setStretch(0,1)
		optionFrameLayout.setStretch(1,4)

		tableViewFrame = QFrame()
		tableViewFrame.setFrameShape(QFrame.StyledPanel)
		tableViewFrame.setFrameShadow(QFrame.Plain)

		self.tableViewLayout = QVBoxLayout()

		tableViewFrame.setLayout(self.tableViewLayout)

		mainLayout.addWidget(optionFrame)
		mainLayout.addWidget(tableViewFrame)

		mainLayout.setStretch(0,2)
		mainLayout.setStretch(1,4)




class userTab(tabBluePrint):

	def __init__(self):

		super().__init__()

		self.setUpUserTab()
		self.setUpTableView()


	def setUpUserTab(self):

		self.searchGroupBox.setTitle("Search by Username")
		self.optionButtonGroupBox.setTitle("User Manage Options")
		self.addButton.setText("New user")
		self.addButton.setIcon(QIcon("../images/database.png"))
		self.addButton.setIconSize(QSize(40,40))
		self.addButton.clicked.connect(self.addNewUser)

		self.editButton.setText("Edit User")
		self.editButton.setIcon(QIcon("../images/edit.png"))
		self.editButton.setIconSize(QSize(40,40))

		self.deleteButton.setText("Delete User")
		self.deleteButton.setIcon(QIcon("../images/delete.png"))
		self.deleteButton.setIconSize(QSize(40,40))

		self.userTable = registeredUserTable

		self.tableViewLayout.addWidget(self.userTable)





	def setUpTableView(self):

		self.userTableModel = QStandardItemModel()

		self.userTable.setModel(self.userTableModel)

		columns = ["User Name", "User Email", "User Role", "User PassWord Hash"]

		self.userTableModel.setHorizontalHeaderLabels(columns)

		header = self.userTable.horizontalHeader()

		header.setSectionResizeMode(0, QHeaderView.Stretch)
		header.setSectionResizeMode(1, QHeaderView.Stretch)
		header.setSectionResizeMode(2, QHeaderView.Stretch)
		header.setSectionResizeMode(3, QHeaderView.Stretch)


	def updateTableView(self):

		pass

	def addNewUser(self):

		self.userDialog = addUser(self)

		self.userDialog.exec_()


class stockTab(tabBluePrint):

	def __init__(self):

		super().__init__()

		self.setUpStockTab()
		self.setupTableView()
		self.updateProductTableView()


	def setUpStockTab(self):

		self.searchGroupBox.setTitle("Search by Product Code")
		self.optionButtonGroupBox.setTitle("Stock Manage Options")
		self.addButton.setText("New Product")
		self.addButton.setIcon(QIcon("../images/database.png"))
		self.addButton.setIconSize(QSize(40,40))
		self.addButton.clicked.connect(self.addStock)

		self.editButton.setText("Edit Stock")
		self.editButton.setIcon(QIcon("../images/edit.png"))
		self.editButton.setIconSize(QSize(40,40))

		self.deleteButton.setText("Delete Stock")
		self.deleteButton.setIcon(QIcon("../images/delete.png"))
		self.deleteButton.setIconSize(QSize(40,40))

		self.stockTable = stockTable

		self.tableViewLayout.addWidget(self.stockTable)

	def setupTableView(self):

		self.stockTableModel = QStandardItemModel()

		self.stockTable.setModel(self.stockTableModel)

		columns = ["Product Code", "Product Name", 
		"Product Description", "Price", "Category", "Quantity"]

		self.stockTableModel.setHorizontalHeaderLabels(columns)

		header = self.stockTable.horizontalHeader()

		header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
		header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
		header.setSectionResizeMode(2, QHeaderView.Stretch)
		header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
		header.setSectionResizeMode(4, QHeaderView.Stretch)
		header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
		


	def prepareProductForView(self):

		products = accessDatabase.getProducts()

		productsAvailable = []

		for items in products:

			details = [items.productCode, items.productName,
			items.productDescription, items.productPrice, items.productCategory,
			items.productQuantity]

			productsAvailable.append(details)



		return productsAvailable


	def updateProductTableView(self):

		products = self.prepareProductForView()

		self.stockTableModel.setRowCount(len(products))

		for row in range(len(products)):

			for columns in range(len(products[row])):

				item = QStandardItem(str(products[row][columns]))

				self.stockTableModel.setItem(row, columns, item)


	def addStock(self):

		pass



class cashFlowTab(QWidget):

	def __init__(self):

		super().__init__()

		self.setUpCashTab()


	def setUpCashTab(self):

		pass