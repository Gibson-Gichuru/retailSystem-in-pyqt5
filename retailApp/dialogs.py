from PyQt5.QtWidgets import (QDialog, QLineEdit, QPushButton, QVBoxLayout,
	QHBoxLayout)


from PyQt5.QtGui import QIcon,  QFont

from PyQt5.QtCore import Qt,QSize


class addCreditorDialog(QDialog):

	def __init__(self):

		super().__init__()

		self.setUpGui()


	def setUpGui(self):

		mainDialogLayout = QVBoxLayout()

		self.setLayout(mainDialogLayout)

		headerlayout = QHBoxLayout()

		headerIcon = QPushButton()

		headerIcon.setIcon(QIcon("../images/credit.png"))
		headerIcon.setIconSize(QSize(60, 60))

		#add header spacer item
		headerlayout.addWidget(headerIcon)
		# add header spacer item

		mainDialogLayout.addLayout(headerlayout)

		outerInputLayout = QHBoxLayout()
		outerInputLayout.setSpacing(10)
		outerInputLayout.setContentsMargins(20, 0, 20, 0)

		inputLayout1 = QVBoxLayout()
		inputLayout1.setSpacing(10)

		inputLayout2 = QVBoxLayout()
		inputLayout2.setSpacing(10)

		outerInputLayout.addLayout(inputLayout1)
		outerInputLayout.addLayout(inputLayout2)

		self.creditorPhonenumber = QLineEdit()
		self.creditorPhonenumber.setAlignment(Qt.alignCenter)

		self.creditorIdNumber = QLineEdit()
		self.creditorIdNumber.setAlignment(Qt.alignCenter)

		self.creditorFirstName = QLineEdit()
		self.creditorFirstName.setAlignment(Qt.alignCenter)

		self.creditorsecondName = QLineEdit()
		self.creditorsecondName.setAlignment(Qt.alignCenter)

		self.creditorAmountDue = QLineEdit()
		self.creditorAmountDue.setAlignment(Qt.alignCenter)

		inputLayout1.addWidget(self.creditorPhonenumber)
		inputLayout2.addWidget(self.creditorIdNumber)
		inputLayout1.addWidget(self.creditorFirstName)
		inputLayout2.addWidget(self.creditorsecondName)
		inputLayout1.addWidget(self.creditorAmountDue)

		#datewidget item
		inputLayout2.addWidget(self.creditorPhonenumber)

		mainDialogLayout.addLayout(outerInputLayout)

		buttonLayout = QHBoxLayout()
		buttonLayout.setContentsMargins(20,0,20,0)

		self.registerCreditorButton = QPushButton("registerCreditor")
		self.registerCreditorButton.setObjcetName("registerCreditorButton")

		self.registerCreditorButton.clicked.connect(self.registerCreditor)

		buttonLayout.addWidget(self.registerCreditorButton)

		mainDialogLayout.addLayout(buttonLayout)

		mainDialogLayout.setStretch(0,2)
		mainDialogLayout.setStretch(1,4)
		mainDialogLayout.setStretch(2,1)

	def registerCreditor(self):

		pass


class userProductRegBluePrint:

	pass