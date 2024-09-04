
class Product:

    def __init__(self,name,price):
        self.name = name
        self.price = price
    def discounted_price(self,discount):
        self.price = self.price - self.price* discount/100
        return self.price

p1 = Product("Iphone", 700)
p1.name
before_discount_p1 = p1.price
p1.discounted_price(20)
after_discount_p1 = p1.price

p2 = Product("Ipad", 500)
p2.name
before_discount_p2 = p2.price
p2.discounted_price(10)
after_discount_p2 = p2.price
print(f"original price of {p1.name} is {before_discount_p1} and the discounted price is {after_discount_p1}")
print(f"original price of {p2.name} is {before_discount_p2} and the discounted price is {after_discount_p2}")

