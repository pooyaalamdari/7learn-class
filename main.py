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
    p2 = Product(1,'Product #1', 1000)
    p3 = Product(1, 'Product #1', 1000 , 'some description about product!')

