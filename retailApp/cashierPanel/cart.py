# contains all the product Purchase functionality

class Cart(list):

	def __init__(self):

		super().__init__()


	def prepareCart(self, productObject, Qty, productCode):

		

		# check if the cart has registered products

		if len(self) > 0:

			if self.keyValidator(productCode):

				self.updateCart(Qty, productCode)

			else:

				self.registerProduct(productObject, productCode, Qty)

		else:
			
			self.registerProduct(productObject, productCode, Qty)

	def updateCart(self,Qty, productCode):

		for product in self:

			update = product.get(productCode)

			if update != None:

				update[3] += update[2] * Qty

				print(update[3])

	def keyValidator(self, productcode):

		keyHolder = []

		for products in self:

			key = list(products.keys())[0]

			keyHolder.append(key)

		return productcode in keyHolder

	def registerProduct(self, productObject, productCode, Qty):

		productValues = {}

		cost = self.calculateCost(productObject.categoryVat,
			productObject.categoryDiscount,
			productObject.productPrice, Qty)

		productDetails = [productObject.productName,productObject.productDescription,
		cost[2], cost[3]]

		productValues.update({productCode: productDetails})

		self.append(productValues)
		

	def calculateCost(self, vat, discount, QPrice, Qty):

		ResultVat = round((vat/100) * QPrice, 2)

		ResultDiscount = round((discount/100) * QPrice, 2)

		unitPrice = (QPrice - ResultDiscount) + ResultVat

		totalPrice = round(Qty * unitPrice, 2)

		return [ResultVat, ResultDiscount, unitPrice, totalPrice]


