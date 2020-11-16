# Data Manupulation module

from database.Models.models import (data, Users, userRole, productCategory,
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

