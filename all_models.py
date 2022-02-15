class Customer:
    def __init__(self,username,password,fullname,email):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email
        self.wallet_amount = 0

class Product:

    def __init__(self,upc,name,price=0,description=''):
        self.upc = upc
        self.name = name
        self.price = price
        self.description = description
