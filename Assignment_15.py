product = 'Laptop'
price = 75000.5
discount = 10

print(f"(f-string): Product:{product} | Price:{price:.2f} | Discount:{discount}% ")

print(".format():", "Product:{} | Price:{:.2f} | Discount:{}% ".format(product, price, discount) )

print("(% operator):","Product:%s | Price:%.2f | Discount:%d%%" % (product,price,discount))
