from sqlalchemy import (Table, Column , Integer, 
	String, create_engine, ForeignKey, Numeric, Date)
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker, relationship, backref

base = declarative_base()

engine = create_engine(
	"mysql+pymysql://gib_dev:pass1234@localhost/retailSystem")

class DatabaseAccess:

	def __init__(self):

		self.Session = sessionmaker(bind = engine)

		self.session = self.Session()

data = DatabaseAccess()


class userRole(base):

	__tablename__ = "userRole"

	roleId = Column(Integer(), primary_key = True)
	roleName = Column(String(40), nullable = False)


class Users(base):

	__tablename__ = "users"

	username = Column(String(50), primary_key = True)
	usernameEmail = Column(String(200), nullable = False)
	usernamePhoneNumber = Column(String(40), nullable = False)
	usernamePassSalt = Column(String(30), nullable = False)
	usernamePassHash = Column(String(300), nullable = False)
	userRole = Column(Integer(), ForeignKey("userRole.roleId"), nullable = False)

	role = relationship("userRole", backref = backref("users",
		order_by = username))


class productCategory(base):

	__tablename__ = "Category"

	categoryId = Column(Integer(), primary_key = True)
	categoryName = Column(String(40), nullable = False)
	categoryVat = Column(Numeric(2,1), nullable = False, default = 0.0)
	categoryDiscount = Column(Numeric(2,1), nullable = False, default = 0.0)


class products(base):

	__tablename__ = "Products"

	productCode = Column(String(30), primary_key = True)
	productName = Column(String(60), nullable = False)
	productDescription = Column(String(200))
	productPrice = Column(Numeric(4,2), nullable = False)
	productCategory = Column(Integer(), ForeignKey("Category.categoryId"))
	productQuantity = Column(Integer())

	category = relationship("productCategory",backref = backref("Products",order_by = productCode))


class paymentMethod(base):

	__tablename__ = "paymentMethod"

	paymentMethodId = Column(Integer(), primary_key = True)
	paymentMethodName = Column(String(50), nullable = False)


class ReceptBook(base):

	__tablename__ = "ReceptBook"

	receptId = Column(Integer(), primary_key = True)
	purchaseAmount = Column(Numeric(6,2), nullable = False)
	purchaseType = Column(Integer(), ForeignKey("paymentMethod.paymentMethodId"))

	dateOfPurchase = Column(Date(), nullable = False)

	payment = relationship("paymentMethod", backref = backref("ReceptBook"),
		order_by = receptId)


class Creditor(base):

	__tablename__ = "Creditor"

	creditorId = Column(String(30), primary_key = True)
	creditorFirstName = Column(String(50), nullable = False)
	creditorSecondName = Column(String(50), nullable = False)
	receptId = Column(Integer(), ForeignKey("ReceptBook.receptId"))
	dateDuePayment = Column(Date(), nullable = False)

	recept = relationship("ReceptBook", backref = backref("Creditor", 
		order_by = creditorId))


