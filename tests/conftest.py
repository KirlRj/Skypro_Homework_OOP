import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_1() -> Category:
    return Category(name="Фрукты", description="Категория 'Фрукты'", products=["Яблоко", "Апельсин", "Груша", "Банан"])


@pytest.fixture
def category_2() -> Category:
    return Category(name="Овощи", description="Категория 'Овощи'", products=["Огурец", "Помидор", "Капуста"])


@pytest.fixture
def product_1() -> Product:
    return Product(name="Яблоко", description="Яблоко сорта Golden Delicious", price=50.00, quantity=350)
