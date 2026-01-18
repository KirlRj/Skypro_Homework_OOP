import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_1():
    return Category(
        name="Фрукты",
        description = "Категория 'Фрукты'",
        products = ["Яблоко", "Апельсин", "Груша", "Банан"]
    )


@pytest.fixture
def category_2():
    return Category(
        name="Овощи",
        description="Категория 'Овощи'",
        products=["Огурец", "Помидор", "Капуста"]
    )

@pytest.fixture
def product_1():
    return Product(name="Яблоко",
                   description = "Яблоко сорта Golden Delicious",
                   price = 50.00,
                   quantity = 350
                   )
