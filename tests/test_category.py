from src.category import Category


def test_category(category_2: Category) -> None:
    assert category_2.name == "Овощи"
    assert category_2.description == "Категория 'Овощи'"
    assert category_2.products == ["Огурец", "Помидор", "Капуста"]
    assert category_2.category_count == 1
    assert category_2.product_count == 3


def test_category_2(category_1: Category) -> None:
    assert category_1.name == "Фрукты"
    assert category_1.description == "Категория 'Фрукты'"
    assert category_1.products == ["Яблоко", "Апельсин", "Груша", "Банан"]
    assert category_1.category_count == 2
    assert category_1.product_count == 7
