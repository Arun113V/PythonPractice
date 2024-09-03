'''fruits = ["orange" , "mango", "pineapple"]
fruits.insert(1,"banana")
fruits.append(["guava", "berries"])
fruits.extend(["tomato", "kiwi"])
fruits[4]="apricot"
fruits.pop()
fruits.remove('orange')
print(fruits.index('mango'))
print(fruits)

#people = {"john" : 20, "Tim": 30, "David": 40}
people = dict(
    John=20,
    David=30
)
people["Tim"] = 40
print(people.get("Dad"))

products = ["phone", "tablet", "laptop", "journal"]
print(f"current list of items{products}")
remove_item = input("Enter the product to remove into list:\t")
products.remove(remove_item)
print(products)

products = ["phone", "tablet", "laptop", "journal"]
print(f"current list of items{products}")
add_item = input("Enter the product to add into list:\t")
add_after = input(f"After which product do you want to place {add_item} ")
index = products.index(add_after)
products.insert(index+1,add_item)
print(f"current list of items{products}")

products = {'phone' : 100, 'tablet':200, 'laptop':300, 'journal':400}
print(products)
product_item = input("Enter the product to be added")
product_item_price = input("Enter the price of the product")
products[product_item]=product_item_price
print(products)

products = {'phone' : 100, 'tablet':200, 'laptop':300, 'journal':400}
print(products)
product_item = input("Enter the product to be deleted")
del products[product_item]
print(products)

products = {'phone' : 100, 'tablet':200, 'laptop':300, 'journal':400}
print(products)
product_item = input("Enter the product to be updated")
product_updated_price = input("Enter the price of the product")
products[product_item] = product_updated_price
print(products)
'''