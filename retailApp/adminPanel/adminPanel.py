from PyQt5.QtWidgets import (QVBoxLayout, QFrame, QPushButton, QWidget,
	QLabel, QHBoxLayout, QTabWidget)


from PyQt5.QtGui import QIcon, QPixmap, QFont

from PyQt5.QtCore import Qt, QSize

from adminPanel.tabWidgets import userTab, stockTab,cashFlowTab


class adminPanelUi(QWidget):

	def __init__(self):

		super().__init__()

		self.initiateUI()


	def initiateUI(self):

		mainLayout = QVBoxLayout()

		self.setLayout(mainLayout)

		headerFrame = QFrame()
		headerFrame.setFrameShape(QFrame.StyledPanel)
		headerFrame.setFrameShadow(QFrame.Plain)

		headerLayout = QHBoxLayout()

		headerIcon = QPushButton()
		headerIcon.setFlat(True)
		headerIcon.setIcon(QIcon("../images/shield.png"))
		headerIcon.setIconSize(QSize(60, 60))

		font = QFont()
		font.setBold(True)
		font.setPointSize(36)
		font.setWeight(75)

		headerLabel = QLabel("Admin Panel")
		headerLabel.setAlignment(Qt.AlignCenter)
		headerLabel.setFont(font)

		loginStatus = QPushButton()
		loginStatus.setFlat(True)
		loginStatus.setIcon(QIcon("../images/id-card.png"))
		loginStatus.setIconSize(QSize(30, 30))

		headerLayout.addWidget(headerIcon)
		headerLayout.addWidget(headerLabel)
		headerLayout.addWidget(loginStatus)

		headerLayout.setStretch(0,1)
		headerLayout.setStretch(1,5)
		headerLayout.setStretch(2,1)

		headerFrame.setLayout(headerLayout)

		mainLayout.addWidget(headerFrame)

		bodyFrame = QFrame()
		bodyFrame.setFrameShape(QFrame.StyledPanel)
		bodyFrame.setFrameShadow(QFrame.Plain)

		bodyLayout = QVBoxLayout()

		bodyFrame.setLayout(bodyLayout)

		self.bodyTab = QTabWidget()
		self.bodyTab.setDocumentMode(True)
		self.bodyTab.setIconSize(QSize(30, 30))

		bodyLayout.addWidget(self.bodyTab)

		self.bodyTabSetUp()

		mainLayout.addWidget(bodyFrame)


		mainLayout.setStretch(0,1)
		mainLayout.setStretch(1,6)


		self.setTabOrder(loginStatus, self.bodyTab)
		self.setTabOrder(self.bodyTab, headerIcon)


	def bodyTabSetUp(self):

		self.user_tab = userTab()

		userIcon = QIcon()

		userIcon.addPixmap(QPixmap("../images/user.png"), 
			QIcon.Normal, QIcon.Off)

		self.bodyTab.addTab(self.user_tab, userIcon, "User Management")


		self.stock_tab = stockTab()

		stockIcon = QIcon()

		stockIcon.addPixmap(QPixmap("../images/list.png"), 
			QIcon.Normal, QIcon.Off)

		self.bodyTab.addTab(self.stock_tab, stockIcon, "Stock Management")


		self.cash_tab = cashFlowTab()

		cashIcon = QIcon()

		cashIcon.addPixmap(QPixmap("../images/manageCash.png"), 
			QIcon.Normal, QIcon.Off)

		self.bodyTab.addTab(self.cash_tab, cashIcon, "Cash Management")









