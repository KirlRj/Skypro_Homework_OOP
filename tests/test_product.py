from src.product import Product


def test_product_1(product_1: Product) -> None:
    assert product_1.name == "Яблоко"
    assert product_1.description == "Яблоко сорта Golden Delicious"
    assert product_1.price == 50.00
    assert product_1.quantity == 350
