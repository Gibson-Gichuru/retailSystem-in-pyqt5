import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction)

from cashierPanel.cashierFuctionality import cashierFunctions

from adminPanel.adminPanel import adminPanelUi

from PyQt5.QtGui import QIcon

from PyQt5.QtCore import Qt

from utilities import style



class MainWindow(QMainWindow):

	def __init__(self):

		super().__init__()
		self.setWindowTitle("Sure Retails")
		self.setWindowIcon(QIcon("../images/windowIcon.png"))

		self.initiateApp()

		self.show()

	def initiateApp(self):

		self.showMaximized()
		self.centerWidget = cashierFunctions()
		self.setCentralWidget(self.centerWidget)
	


	def cashierMenu(self):

		creditPurchaseAction = QAction(self)
		creditPurchaseAction.setShortcut("Ctrl+Shift+C")
		creditPurchaseAction.triggered.connect(self.centerWidget.creditPurchase(self))


	def cashierPayout(self):

		pass


	def keyPressEvent(self, event):

		if event.key() == Qt.Key_Shift:

			self.centerWidget.creditPurchase(self)

		elif event.key() == Qt.Key_Space:

			print("credit transacions")
		


if __name__  == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	app.setStyleSheet(style)
	sys.exit(app.exec_())