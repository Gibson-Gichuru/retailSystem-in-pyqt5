# contains all the product Purchase functionality

class Cart(list):

	def __init__(self):

		super().__init__()


	def prepareCart(self, productObject, Qty, productCode):

		

		# check if the cart has registered products

		if len(self) > 0:

			if keyValidator(productCode):

				self.updateCart(Qty, productCode)

			else:

				self.registerProduct(productObject)

		else:
			
			self.registerProduct(productObject, productCode)

	def updateCart(self,Qty, productCode):

		for product in self:

			update = product.get(productCode)

			# update the productQuantity and the total price

	def keyValidator(self, productcode):

		keyHolder = []

		for products in self:

			key = products.keys()[0]

			keyHolder.append(key)

		return productcode in keyHolder

	def registerProduct(self, productObject, productCode):

		productValues = {}

		cost = calculateCost(productObject.categoryVat,
			categotyDiscount,productPrice, Qty)

		productDetails = [productObject.productCode,
		productObject.productName,productObject.productDescription,
		cost[3], cost[4]]

		productValues.update({productCode: productDetails})

		self.append(productValues)
		

	def calculateCost(self, vat, discount, QPrice, Qty):

		ResultVat = round(vat * Qprice, 2)

		ResultDiscount = round(discount * QPrice, 2)

		unitPrice = (QPrice - ResultDiscount) + ResultVat

		totalPrice = round(Qty * unitPrice, 2)

		return [ResultVat, ResultDiscount, unitPrice, totalPrice]


