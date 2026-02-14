from src.product import Product


class Category:
    """Класс категории продуктов. Структура: имя, описание, продукты"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list | None = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Неверный объект")

    @property
    def products(self) -> str | None:
        products = ""
        for product in self.__products:
            products += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products

    def __str__(self) -> str:
        count = 0
        for product in self.__products:
            count += product.quantity
        return f"{self.name}, количество продуктов: {count}"
