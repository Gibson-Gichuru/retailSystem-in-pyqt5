from .appwidgets import cartTableView, userTableView,StockTableView
from .dataAccess import DataAccess

from .dialogs import addCreditorDialog, addUser, addProduct
from .passwordHelper import passwordHasher
from .styles import styleSheet

accessDatabase = DataAccess()

purchasedProductsTable = cartTableView()
registeredUserTable = userTableView()
stockTable = StockTableView()

ph = passwordHelper()

style = styleSheet

creditorDialog = addCreditorDialog