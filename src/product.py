from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):

        self.name = name
        self.description = description
        self.price = price  # Здесь будет срабатывать сеттер
        self.quantity = quantity

    @property
    @abstractmethod
    def price(self) -> float:
        """Абстрактный геттер для цены"""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        """Абстрактный сеттер для цены"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, data: dict) -> "BaseProduct":
        """Абстрактный класс-метод для создания продукта"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный строковый метод"""
        pass

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Абстрактный метод сложения продуктов"""
        pass


class MixinProduct:

    def __repr__(self):
        class_name = self.__class__.__name__
        data = f"{self.name}, {self.description}, {self.price}, {self.quantity}"
        return f"{class_name}({data})"


class Product(BaseProduct, MixinProduct):
    """Класс продукта. Структура: имя, описание, цена, количество"""

    name: str
    description: str
    quantity: int

    all_products: list[Product] = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
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
    def new_product(cls, data: dict) -> "BaseProduct":
        name = data["name"]
        description = data["description"]
        price = data["price"]
        quantity = data["quantity"]

        for product in cls.all_products:
            if product.name == name:
                product.quantity += quantity
                if price > product.price:
                    product.price = price
                return product

        new_product = cls(name, description, price, quantity)
        cls.all_products.append(new_product)
        return new_product

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other: "BaseProduct") -> float:
        if type(self) is type(other):
            total = self.price * self.quantity + other.price * other.quantity
            return total
        else:
            raise TypeError("Классы продуктов разные")


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
