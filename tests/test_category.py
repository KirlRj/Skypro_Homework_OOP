import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_2() -> Category:
    cucumber = Product.new_product({"name": "Огурец", "description": "Свежие огурцы", "price": 20, "quantity": 1})
    tomato = Product.new_product({"name": "Помидор", "description": "Красные помидоры", "price": 30, "quantity": 1})
    cabbage = Product.new_product(
        {"name": "Капуста", "description": "Белокочанная капуста", "price": 25, "quantity": 1}
    )

    category = Category(name="Овощи", description="Категория 'Овощи'", products=[cucumber, tomato, cabbage])
    return category


@pytest.fixture
def category_1() -> Category:
    apple = Product.new_product({"name": "Яблоко", "description": "Красное яблоко", "price": 50, "quantity": 2})
    orange = Product.new_product({"name": "Апельсин", "description": "Апельсин сладкий", "price": 60, "quantity": 1})
    pear = Product.new_product({"name": "Груша", "description": "Сочная груша", "price": 55, "quantity": 1})
    banana = Product.new_product({"name": "Банан", "description": "Жёлтый банан", "price": 70, "quantity": 3})

    category = Category(name="Фрукты", description="Категория 'Фрукты'", products=[apple, orange, pear, banana])
    return category


@pytest.fixture
def category_3() -> Category:
    apple = Product("Яблоко", "Свежие яблоки", 50, 10)
    banana = Product("Банан", "Жёлтые бананы", 70, 5)

    category = Category("Фрукты", "Свежие фрукты")
    category.add_product(apple)
    category.add_product(banana)

    return category


@pytest.fixture
def empty_category() -> Category:
    return Category(name="Пустая", description="Категория без товаров", products=[])


@pytest.fixture
def category_with_products() -> Category:
    product1 = Product(name="Яблоко", description="Зелёное", price=50, quantity=10)
    product2 = Product(name="Банан", description="Жёлтый", price=70, quantity=5)
    product3 = Product(name="Апельсин", description="Оранжевый", price=80, quantity=3)
    return Category(name="Фрукты", description="Фрукты", products=[product1, product2, product3])


@pytest.fixture
def category_with_one_product() -> Category:
    product = Product(name="Яблоко", description="Зелёное", price=50, quantity=10)
    return Category(name="Фрукты", description="Фрукты", products=[product])


def test_category(category_2: Category) -> None:
    assert category_2.name == "Овощи"
    assert category_2.description == "Категория 'Овощи'"
    assert "Огурец" in category_2.products
    assert "Помидор" in category_2.products
    assert "Капуста" in category_2.products
    assert category_2.category_count >= 1
    assert category_2.product_count >= 3


def test_category_1(category_1: Category) -> None:
    assert category_1.name == "Фрукты"
    assert category_1.description == "Категория 'Фрукты'"
    assert "Яблоко" in category_1.products
    assert "Апельсин" in category_1.products
    assert "Груша" in category_1.products
    assert "Банан" in category_1.products
    assert category_1.category_count >= 2
    assert category_1.product_count >= 7


def test_category_str(category_3: Category) -> None:
    assert str(category_3) == "Фрукты, количество продуктов: 15"


def test_average_price_empty_category(empty_category: Category) -> None:
    assert empty_category.middle_price() == 0


def test_average_price_with_products(category_with_products: Category) -> None:
    expected = (50 + 70 + 80) / 3
    assert category_with_products.middle_price() == expected


def test_average_price_one_product(category_with_one_product: Category) -> None:
    assert category_with_one_product.middle_price() == 50


def test_average_price_with_zero_price_product() -> None:
    product = Product(name="Тест", description="Описание", price=0, quantity=5)
    category = Category(name="Тест", description="Описание", products=[product])
    assert category.middle_price() == 0
