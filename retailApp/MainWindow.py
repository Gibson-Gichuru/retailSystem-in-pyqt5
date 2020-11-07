import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow)

from cashierFuctionality import cashierFunctions

from styles import styleSheet


class MainWindow(QMainWindow):

	def __init__(self):

		super().__init__()

		self.initiateApp()

	def initiateApp(self):

		self.show()

		self.showMaximized()

		self.setCentralWidget(cashierFunctions())


if __name__  == "__main__":

	app = QApplication(sys.argv)
	app.setStyleSheet(styleSheet)
	window = MainWindow()
	sys.exit(app.exec_())


