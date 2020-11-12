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


