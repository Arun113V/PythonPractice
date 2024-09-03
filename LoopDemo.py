products = [
    {"name": "Smartphone", "price":500, "description": "A handheld device used for communication and browsing the internet." },
    {"name": "Laptop", "price": 1000, "description": " A portable computer that is easy to carry around"},
    {"name": "Head Phones", "price": 50, "description": "A pair of earphones worn over the head to listen the music"},
    {"name": "Smart Watch", "price": 300, "description" : "A wearable devices used for fitness tracking and to receive notification"},
    {"name": "Bluetooth Speaker", "price": 100, "description": "A portable speaker that connects wirelesly to device using Bluetooth technology"}
    ]

cart = []

while True:
    choice = input("Do you want to continue shopping :\t")
    if choice == "yes":
        print("Here is the list of products to select the items")
        for index, product in enumerate(products):
            print(f"{index} : {product['name']} : {product['price']} : {product['description']}")
        product_id = int(input("Select the product id to add the item:\t"))
        if products[product_id] in cart:
            products[product_id]['quantity'] += 1
        else:
            products[product_id]['quantity'] = 1
            cart.append(products[product_id])
        total = 0
        print(f"The list of products in cart is :")
        for product in cart:
            print(f"{product['name']} : {product['price']} : {product['quantity']}")
            total += product['price'] * product['quantity']
        print(f"Cart total is : ${total}")
    else:
        break
    print(f"Thank you, total cart contents are : {cart}")