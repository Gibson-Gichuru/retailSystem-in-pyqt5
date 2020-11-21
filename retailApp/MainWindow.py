import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow)

from cashierPanel.cashierFuctionality import cashierFunctions

from PyQt5.QtGui import QIcon

from styles import styleSheet


class MainWindow(QMainWindow):

	def __init__(self):

		super().__init__()
		self.setWindowTitle("Sure Retails")
		self.setWindowIcon(QIcon("../images/windowIcon.png"))

		self.initiateApp()
		self.show()

	def initiateApp(self):

		self.showMaximized()

		self.setCentralWidget(cashierFunctions())

	


if __name__  == "__main__":

	app = QApplication(sys.argv)
	window = MainWindow()
	app.setStyleSheet(styleSheet)
	sys.exit(app.exec_())