from product import product_info

def test_product_info():
    expected_output = (
        "Product Name: Headphones\n"
        "Product ID: p101\n"
        "Quantity: 3\n"
        "Product Price: 699"
    )
    result = product_info("Headphones", "p101", 5, 699)
    assert result == expected_output
