def product_info(name, id, quantity, price):
    return (
        f"Product Name: {name}\n"
        f"Product ID: {id}\n"
        f"Quantity: {quantity}\n"
        f"Product Price: {price}"
    )

if __name__ == "__main__":
    name = "Headphones"
    id = "p101"
    quantity = 3
    price = 699

    print("Product Details:\n")
    print(product_info(name, id, quantity, price))
