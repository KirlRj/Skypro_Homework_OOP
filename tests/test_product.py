from typing import Any

import pytest

from src.product import Product


@pytest.fixture(autouse=True)
def clear_all_products() -> None:

    Product.all_products.clear()


def test_create_new_product() -> None:
    data = {"name": "Яблоко", "description": "Зелёное яблоко", "price": 50, "quantity": 10}
    product = Product.new_product(data)

    assert product.name == "Яблоко"
    assert product.description == "Зелёное яблоко"
    assert product.price == 50
    assert product.quantity == 10
    assert product in Product.all_products


def test_update_existing_product() -> None:

    data1 = {"name": "Яблоко", "description": "Зелёное яблоко", "price": 50, "quantity": 10}
    product1 = Product.new_product(data1)

    data2 = {"name": "Яблоко", "description": "Зелёное яблоко", "price": 55, "quantity": 5}
    product2 = Product.new_product(data2)

    assert product1 is product2

    assert product1.quantity == 15

    assert product1.price == 55

    assert len(Product.all_products) == 1


def test_product_price_setter_raise() -> None:
    product = Product.new_product({"name": "Банан", "description": "Жёлтый банан", "price": 30, "quantity": 5})

    with pytest.raises(ValueError):
        product.price = 0
    with pytest.raises(ValueError):
        product.price = -10


def test_product_price_setter_decrease(monkeypatch: Any) -> None:
    product = Product.new_product({"name": "Груша", "description": "Спелая груша", "price": 40, "quantity": 2})

    monkeypatch.setattr("builtins.input", lambda: "y")
    product.price = 30
    assert product.price == 30

    monkeypatch.setattr("builtins.input", lambda: "n")
    product.price = 20
    assert product.price == 30


def test_multiple_products() -> None:
    data_apple = {"name": "Яблоко", "description": "Зелёное яблоко", "price": 50, "quantity": 10}
    data_banana = {"name": "Банан", "description": "Жёлтый банан", "price": 70, "quantity": 5}
    Product.new_product(data_apple)
    Product.new_product(data_banana)

    assert len(Product.all_products) == 2
    names = [p.name for p in Product.all_products]
    assert "Яблоко" in names
    assert "Банан" in names
