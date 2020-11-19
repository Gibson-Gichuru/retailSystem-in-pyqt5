from PyQt5.QtWidgets import (QDialog, QLineEdit, QPushButton, QVBoxLayout,
	QHBoxLayout, QSpacerItem, QSizePolicy, QDateEdit, 
	QMessageBox)


from PyQt5.QtGui import QIcon,  QFont

from PyQt5.QtCore import Qt,QSize,QDate

from dataAccess import DataAccess

access = DataAccess()


class addCreditorDialog(QDialog):

	def __init__(self, parent, totals, DOP, paymentMethod, productDetails):

		super().__init__(parent)

		self.setFixedSize(520, 320)
		self.setWindowTitle("Creditor")
		#self.setAttribute(Qt.WA_DeleteOnClose)
		self.productTotals = totals
		self.dateOfPurchase  = DOP

		self.modeOfPayment = paymentMethod

		self.details = productDetails

		self.setUpGui()

	def setUpGui(self):

		mainDialogLayout = QVBoxLayout()

		self.setLayout(mainDialogLayout)

		headerlayout = QHBoxLayout()

		headerIcon = QPushButton()

		headerIcon.setIcon(QIcon("../images/credit.png"))
		headerIcon.setIconSize(QSize(60, 60))
		headerIcon.setFlat(True)

		#add header spacer item
		headerSpace = QSpacerItem(40, 20,QSizePolicy.Expanding, QSizePolicy.Minimum)
		headerlayout.addItem(headerSpace)
		headerlayout.addWidget(headerIcon)
		headerlayout.addItem(headerSpace)
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
		self.creditorPhonenumber.setAlignment(Qt.AlignCenter)
		self.creditorPhonenumber.setPlaceholderText("Phone number")

		self.creditorIdNumber = QLineEdit()
		self.creditorIdNumber.setAlignment(Qt.AlignCenter)
		self.creditorIdNumber.setPlaceholderText("Id Number")

		self.creditorFirstName = QLineEdit()
		self.creditorFirstName.setAlignment(Qt.AlignCenter)
		self.creditorFirstName.setPlaceholderText("First Name")

		self.creditorsecondName = QLineEdit()
		self.creditorsecondName.setAlignment(Qt.AlignCenter)
		self.creditorsecondName.setPlaceholderText("Second Name")

		self.creditorAmountDue = QLineEdit()
		self.creditorAmountDue.setAlignment(Qt.AlignCenter)
		self.creditorAmountDue.setPlaceholderText("Due Amount")
		self.creditorAmountDue.setEnabled(False)
		self.creditorAmountDue.setText(str(self.productTotals))

		self.date = QDateEdit()
		self.date.setDate(QDate.currentDate())

		inputLayout1.addWidget(self.creditorPhonenumber)
		inputLayout2.addWidget(self.creditorIdNumber)
		inputLayout1.addWidget(self.creditorFirstName)
		inputLayout2.addWidget(self.creditorsecondName)
		inputLayout1.addWidget(self.creditorAmountDue)
	
		#datewidget item
		inputLayout2.addWidget(self.date)

		mainDialogLayout.addLayout(outerInputLayout)

		buttonLayout = QHBoxLayout()
		buttonLayout.setContentsMargins(20,0,20,0)

		self.registerCreditorButton = QPushButton("registerCreditor")
		self.registerCreditorButton.setObjectName("registerCreditorButton")

		self.registerCreditorButton.clicked.connect(self.registerCreditor)

		buttonLayout.addWidget(self.registerCreditorButton)

		mainDialogLayout.addLayout(buttonLayout)

		mainDialogLayout.setStretch(0,2)
		mainDialogLayout.setStretch(1,4)
		mainDialogLayout.setStretch(2,1)

	def registerCreditor(self):

		id = self.creditorIdNumber.text()
		fname = self.creditorFirstName.text()
		sname = self.creditorsecondName.text()

		dueDate = self.date.date().toPyDate()


		# check if the creditor exists 

		creditor = access.checkCreditor(self.creditorIdNumber.text())

		if creditor == True:

			QMessageBox.information(self, "Record Found", 
				"Creditor with the given Id Number exists",QMessageBox.Ok,
				QMessageBox.Ok)

		else:

			access.registerCredior(id, fname, sname, 
				self.productTotals, self.modeOfPayment,self.dateOfPurchase, 
				dueDate,self.details);

			self.accept()
		# if the exist the prompt the user to use other alternative ways
		#else register the creditor

	

	def closeEvent(self, event):

		answer = QMessageBox.question(self, "Quit", 
			"Are you sure you dont want to proceed", QMessageBox.Ok | QMessageBox.Cancel,
			QMessageBox.Ok)

		if answer == QMessageBox.Ok:

			event.accept()

		else:
			
			event.ignore()
		



class userProductRegBluePrint:

	pass


