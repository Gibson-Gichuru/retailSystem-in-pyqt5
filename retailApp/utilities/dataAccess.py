# Data Manupulation module

from database import (data, Users, userRole, productCategory,
	products,paymentMethod, ReceptBook, Creditor)



class DataAccess:

	

	def getProduct(self, givenProductCode):

		product = data.session.query(products.productCode,
			products.productName, products.productDescription,
			products.productPrice, products.productQuantity,productCategory.categoryVat, 
			productCategory.categoryDiscount)

		product = product.join(productCategory)

		product = product.filter(products.productCode == givenProductCode)

		product = product.first()

		if product != None:

			return product

		else:
			
			return None


	def makePurchase(self, purchaseMethod, total, date, productDetails):

		purchaseMode = self.getPurchaseMode(purchaseMethod)

		if purchaseMode != None:

			product = ReceptBook(purchaseAmount = total, dateOfPurchase = date)
			product.payment = purchaseMode

			self.databaseCommit(product)
			self.updateProductRecords(productDetails)


			return product

		else:
			pass
		

	def getPurchaseMode(self, purchaseModeName):

		purchaseMode = data.session.query(paymentMethod)

		purchaseMode = purchaseMode.filter(paymentMethod.paymentMethodName == purchaseModeName)

		purchaseMode = purchaseMode.first()

		return purchaseMode

	def databaseCommit(self, item):

		data.session.add(item)
		data.session.commit()

	def updateProductRecords(self, productDetails):

		for details in productDetails:

			code = list(details.keys())[0]

			productUpdate = data.session.query(products).filter(products.productCode == code)

			productUpdate = productUpdate.first()

			productUpdate.productQuantity -= details[code]

			data.session.commit()


	def registerCredior(self, Id, firstname, secondName,amount,purchaseMethod,
	 DOP, dueDate, productDetails):

		receptId = self.makePurchase(purchaseMethod, amount, DOP, productDetails)

		creditor = Creditor(creditorId = Id, creditorFirstName = firstname, 
			creditorSecondName = secondName, dateDuePayment = dueDate)

		creditor.recept = receptId

		self.databaseCommit(creditor)

	def checkCreditor(self, idNumber):

		
		creditor = data.session.query(Creditor)

		creditor = creditor.filter(Creditor.creditorId == idNumber)

		creditor = creditor.first()

		if creditor == None:

			return False

		else:
			
			return True


	def getProducts(self):

		item = data.session.query(products)

		item = item.all()

		return item

	def getUserRole(self):

		userRoles = data.session.query(userRole.roleName)

		userRoles = userRoles.all()

		return [role for role in userRoles]


	def getUser(self, givenUserID):

		registeredUser = data.session.query(Users)
		registeredUser = registeredUser.filter(Users.userIdNumber == givenUserID)

		registeredUser = registeredUser.first()

		if registeredUser == None:

			return False

		else:
			
			return True


	def registerUser(self):
		
		pass
		

