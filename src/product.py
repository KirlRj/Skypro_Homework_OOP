class Product:
    """Класс продукта. Структура: имя, описание, цена, количество"""

    name: str
    description: str
    price: float
    quantity: int

    all_products: list[Product] = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def product_price(self) -> float:
        return self.__price

    @product_price.setter
    def product_price(self, price: float) -> None:
        if price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")

        if price <= self.__price:
            print(f"Новая цена {price} руб. меньше старой {self.__price} руб. Заменить цену? y/n")
            q = input()
            if q.lower() == "y":
                self.__price = price
                print("Цена обновлена")
            else:
                print("Цена остается прежней")
        else:
            self.__price = price

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        name = data["name"]
        description = data["description"]
        price = data["price"]
        quantity = data["quantity"]

        for product in cls.all_products:
            if product.name == name:
                product.quantity += quantity
                if price > product.product_price:
                    product.product_price = price
                return product

        new_product = cls(name, description, price, quantity)
        cls.all_products.append(new_product)
        return new_product
