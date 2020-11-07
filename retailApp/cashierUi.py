from PyQt5.QtWidgets import (QApplication,QWidget, QHBoxLayout, QVBoxLayout,
	QFrame, QLineEdit, QPushButton, QLabel, QTextEdit, QTableView,
	QAbstractItemView, QGroupBox)

from PyQt5.QtGui import QIcon,  QFont

from PyQt5.QtCore import Qt,QSize

from styles import styleSheet
class CashierGui(QWidget):

	def __init__(self):

		super().__init__()

		self.initiateUi()

	def initiateUi(self):

		mainWindowLayout = QVBoxLayout()
	
		self.setLayout(mainWindowLayout)

		font = QFont()
		font.setBold(True)
		font.setPointSize(36)
		font.setWeight(75)

		self.headerFrame = QFrame()
		self.headerFrame.setFrameShape(QFrame.StyledPanel)
		self.headerFrame.setFrameShadow(QFrame.Plain)

		headerLayout = QHBoxLayout()

		self.headerFrame.setLayout(headerLayout)

		windowIcon = QPushButton()
		windowIcon.setFlat(True)

		windowIcon.setIcon(QIcon("../images/cash-register.png"))
		windowIcon.setIconSize(QSize(50, 50))

		windowHeaderLabel = QLabel("Cashier Panel")
		windowHeaderLabel.setFont(font)
		windowHeaderLabel.setAlignment(Qt.AlignCenter)

		self.loginStatus = QPushButton(" Gibson")
		self.loginStatus.setIcon(QIcon("../images/id-card.png"))
		self.loginStatus.setFlat(True)
		self.loginStatus.setStyleSheet("color:green")
		self.loginStatus.setIconSize(QSize(50,50))

		headerLayout.addWidget(windowIcon)
		headerLayout.addWidget(windowHeaderLabel)
		headerLayout.addWidget(self.loginStatus)

		#Add windget spacing to the header frame#
		headerLayout.setStretch(0,1)
		headerLayout.setStretch(1,4)
		headerLayout.setStretch(2,1)

		#add header to the mainLayout

		mainWindowLayout.addWidget(self.headerFrame)

		self.bodyFrame = QFrame()
		self.bodyFrame.setFrameShape(QFrame.NoFrame)
		self.bodyFrame.setFrameShadow(QFrame.Plain)

		mainWindowLayout.addWidget(self.bodyFrame)

		bodyFrameLayout = QHBoxLayout()

		self.bodyFrame.setLayout(bodyFrameLayout)

		self.productEntryFrame = QFrame()
		self.productEntryFrame.setFrameShape(QFrame.NoFrame)
		self.productEntryFrame.setFrameShadow(QFrame.Plain)

		self.productEntryFrameLayout = QVBoxLayout()

		self.productEntryFrame.setLayout(self.productEntryFrameLayout)

		currentProductView = QHBoxLayout()

		self.currentProductName = QLineEdit()
		self.currentProductName.setPlaceholderText("Product Name")
		self.currentProductName.setAlignment(Qt.AlignCenter)
		self.currentProductName.setEnabled(False)

		self.currentProductDescription = QLineEdit()
		self.currentProductDescription.setPlaceholderText("Product Description")
		self.currentProductDescription.setAlignment(Qt.AlignCenter)
		self.currentProductDescription.setEnabled(False)

		self.currentProductPrice = QLineEdit()
		self.currentProductPrice.setPlaceholderText("Price")
		self.currentProductPrice.setAlignment(Qt.AlignCenter)
		self.currentProductPrice.setEnabled(False)

		currentProductView.addWidget(self.currentProductName)
		currentProductView.addWidget(self.currentProductDescription)
		currentProductView.addWidget(self.currentProductPrice)

		currentProductView.setStretch(0,1)
		currentProductView.setStretch(1,5)
		currentProductView.setStretch(2,1)


		# add the view section to the product Entry Frame

		self.productEntryFrameLayout.addLayout(currentProductView)
		self.productEntryFrameLayout.setStretch(0,1)
		self.productEntryFrameLayout.setStretch(1,1)
		self.productEntryFrameLayout.setStretch(2,5)
		self.productEntryFrameLayout.setStretch(3,1)


		# product entry section


		productEntryLayout = QHBoxLayout()

		self.productCode = QLineEdit()
		self.productCode.setPlaceholderText("Product Code")
		self.productCode.setAlignment(Qt.AlignCenter)

		self.productQty = QLineEdit()
		self.productQty.setPlaceholderText("Quantity")
		self.productQty.setAlignment(Qt.AlignCenter)

		self.productVatView = QLineEdit()
		self.productVatView.setPlaceholderText("VAT")
		self.productVatView.setEnabled(False)
		self.productVatView.setAlignment(Qt.AlignCenter)

		self.productDiscount = QLineEdit()
		self.productDiscount.setPlaceholderText("Discount")
		self.productDiscount.setEnabled(False)
		self.productDiscount.setAlignment(Qt.AlignCenter)

		self.productUnitPrice = QLineEdit()
		self.productUnitPrice.setPlaceholderText("Unit Price")
		self.productUnitPrice.setEnabled(False)
		self.productUnitPrice.setAlignment(Qt.AlignCenter)

		self.productTotalPrice = QLineEdit()
		self.productTotalPrice.setStyleSheet("color:rgb(255,0,0);")
		self.productTotalPrice.setPlaceholderText("Total Price")
		self.productTotalPrice.setEnabled(False)
		self.productTotalPrice.setAlignment(Qt.AlignCenter)

		productEntryLayout.addWidget(self.productQty)
		productEntryLayout.addWidget(self.productCode)
		productEntryLayout.addWidget(self.productVatView)
		productEntryLayout.addWidget(self.productDiscount)
		productEntryLayout.addWidget(self.productUnitPrice)
		productEntryLayout.addWidget(self.productTotalPrice)

		self.productEntryFrameLayout.addLayout(productEntryLayout)

		self.cartTable = QTableView()
		self.cartTable.setFrameShape(QFrame.StyledPanel)
		self.cartTable.setFrameShadow(QFrame.Plain)
		self.cartTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.cartTable.setSelectionMode(QAbstractItemView.SingleSelection)
		self.cartTable.verticalHeader().setVisible(False)

		self.productEntryFrameLayout.addWidget(self.cartTable)

		font.setPointSize(16)

		payoutGroup = QGroupBox()
		payoutGroup.setFlat(True)
		payoutGroup.setFont(font)

		payoutGroup.setTitle("Payment")

		groupLayout = QHBoxLayout()

		payoutGroup.setLayout(groupLayout)

		self.cashPayment = QPushButton(" CashPayment")
		self.cashPayment.setObjectName("paymentButton")
		self.cashPayment.setFont(font)
		self.cashPayment.setIcon(QIcon("../images/cash.png"))
		self.cashPayment.setIconSize(QSize(30,30))

		self.creditPayment = QPushButton(" CreditPayment")
		self.creditPayment.setObjectName("paymentButton")
		self.creditPayment.setFont(font)
		self.creditPayment.setIcon(QIcon("../images/credit.png"))
		self.creditPayment.setIconSize(QSize(30,30))

		groupLayout.addWidget(self.cashPayment)
		groupLayout.addWidget(self.creditPayment)

		self.productEntryFrameLayout.addWidget(payoutGroup)

		self.receptFrame = QFrame()
		self.receptFrame.setFrameShape(QFrame.NoFrame)
		self.receptFrame.setFrameShadow(QFrame.Plain)

		self.recept = QTextEdit()
		self.recept.setEnabled(False)
		self.recept.setFrameShape(QFrame.StyledPanel)
		self.recept.setFrameShadow(QFrame.Plain)

		receptFrameLayout = QVBoxLayout()
		receptFrameLayout.setSpacing(23)
		receptFrameLayout.setContentsMargins(0,9,0,0)

		receptFrameLayout.addWidget(self.recept)

		self.receptFrame.setLayout(receptFrameLayout)

		font.setPointSize(26)

		self.totalPayoutLabel = QLabel("0.0")
		#self.totalPayoutLabel.adjustSize()
		self.totalPayoutLabel.setAlignment(Qt.AlignCenter)
		self.totalPayoutLabel.setObjectName("payoutLabel")
		self.totalPayoutLabel.setFont(font)

		receptFrameLayout.addWidget(self.totalPayoutLabel)

		bodyFrameLayout.addWidget(self.productEntryFrame)
		bodyFrameLayout.addWidget(self.receptFrame)
		bodyFrameLayout.setStretch(0,5)
		bodyFrameLayout.setStretch(1,2)

		mainWindowLayout.setStretch(0,1)
		mainWindowLayout.setStretch(1,5)
		mainWindowLayout.setContentsMargins(0,0,0,0)
		mainWindowLayout.setSpacing(0)

		self.setTabOrder(self.productQty, self.productCode)
		self.setTabOrder(self.productCode, self.cashPayment)
		self.setTabOrder(self.cashPayment, self.creditPayment)
		self.setTabOrder(self.creditPayment, self.loginStatus)


