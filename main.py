from all_models import Customer, Product


if __name__ == "__main__":
    #create customers
    c1 = Customer('hosein','123','Hosein','hosein@mail.com')
    c2 = Customer('ali','456','Ali','ali@mail.com')
    c3 = Customer (
        email = 'reza@mail.com',
        fullname = 'Reza',
        password = '789',
        username = 'reza'
    )

    #create Products
    p1 = Product(1,'Product #1') # True -> price 0 🖇
    p2 = Product(2,'Product #1', 1000)
    p3 = Product(3, 'Product #1', 1000 , 'some description about product!')

   # 🔺 we cant call Class with method
   # Product.is_free() it is wrong

   # ✅ call object we built base on Class
   # then call method

#p1,... obj can call atribute (upc) and call method (is_free())


print('Check password for c1: ',c1.check_password('1375'))
print('---')
print('Check password for c1: ',c1.check_password('123'))
