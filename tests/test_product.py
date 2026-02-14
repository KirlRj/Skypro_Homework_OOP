from typing import Any

import pytest

from src.product import BaseProduct, LawnGrass, Product, Smartphone


@pytest.fixture(autouse=True)
def clear_all_products() -> None:

    Product.all_products.clear()


@pytest.fixture
def product_1() -> Product:
    return Product(name="Яблоко", description="Зелёное яблоко", price=50, quantity=10)


@pytest.fixture
def product_2() -> Product:
    return Product(name="Банан", description="Жёлтый банан", price=70, quantity=5)


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


def test_product_str(product_1: Any) -> None:
    assert str(product_1) == "Яблоко, 50 руб. Остаток: 10 шт.\n"


def test_product_add(product_1: Any, product_2: Any) -> None:
    assert product_1 + product_2 == 850


def test_smartphone_creation() -> None:
    phone = Smartphone(
        name="iPhone 15",
        description="256GB Black",
        price=120000.0,
        quantity=3,
        efficiency=98.5,
        model="15 Pro",
        memory=256,
        color="Black",
    )

    assert isinstance(phone, Product)
    assert phone.name == "iPhone 15"
    assert phone.price == 120000.0
    assert phone.quantity == 3
    assert phone.efficiency == 98.5
    assert phone.model == "15 Pro"
    assert phone.memory == 256
    assert phone.color == "Black"


def test_lawn_grass_creation() -> None:
    grass = LawnGrass(
        name="GreenField",
        description="Газон для дачи",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14",
        color="Зеленый",
    )

    assert isinstance(grass, Product)
    assert grass.name == "GreenField"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "14"
    assert grass.color == "Зеленый"


def test_add_same_type_products() -> None:
    phone1 = Smartphone("Samsung", "S23", 100000.0, 2, 95.0, "S23", 256, "Gray")

    phone2 = Smartphone("Samsung", "S24", 120000.0, 1, 97.0, "S24", 512, "Black")

    total = phone1 + phone2

    assert total == (100000.0 * 2 + 120000.0 * 1)


def test_add_different_types_raises_error() -> None:
    phone = Smartphone("Samsung", "S23", 100000.0, 2, 95.0, "S23", 256, "Gray")

    grass = LawnGrass("Green", "Газон", 500.0, 10, "Россия", "14", "Зеленый")

    with pytest.raises(TypeError):
        phone + grass


def test_base_product_abstract() -> None:
    with pytest.raises(TypeError):
        BaseProduct("", "", 0, 0)


def test_product_repr() -> None:
    product = Product("Яблоко", "Зелёное", 50, 10)
    assert repr(product) == "Product(Яблоко, Зелёное, 50, 10)"


def test_smartphone_repr() -> None:
    phone = Smartphone("iPhone", "Смартфон", 80000, 3, 95.5, "13", 128, "черный")
    assert repr(phone) == "Smartphone(iPhone, Смартфон, 80000, 3)"


def test_lawn_grass_repr() -> None:
    grass = LawnGrass("Газон", "Трава", 1000, 5, "Россия", "14", "зеленый")
    assert repr(grass) == "LawnGrass(Газон, Трава, 1000, 5)"
