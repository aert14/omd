from logs import log

class Pizza:
    """Base Pizza class."""

    def __init__(self, size: str):
        if size not in ["L", "XL"]:
            raise ValueError

        self.size = size
        self.name = None
        self.recept = None

    def __str__(self):
        return f"{self.name} - {self.size}"

    def dict(self):
        print(f"Рецепт: {self.recept}")

    def add_toppings(self, toppings: list[str]) -> None:
        """Добавляет топпинги."""
        print("Добавлены топпинги:", end=" ")
        for topping in toppings:
            print(topping, end=" ")
        print()

    @log("🍳Приготовили за {}c")
    def bake(self) -> None:
        """Готовит пиццу."""

    @log("🛵Доставили за {}c")
    def deliver(self) -> None:
        """Доставляет пиццу."""

    @log("🏡Забрали за {}c")
    def pickup(self, pizza: str) -> None:
        """Самовывозит пиццу."""

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.size == other.size


class MargheritaPizza(Pizza):
    """Margherita pizza."""

    def __init__(self, size: str):
        super().__init__(size)
        self.name = "Margherita"
        self.recept = "tomato sauce, mozzarella, tomatoes"


class PepperoniPizza(Pizza):
    """Pepperoni pizza."""

    def __init__(self, size: str):
        super().__init__(size)
        self.name = "Pepperoni"
        self.recept = "tomato sauce, mozzarella, pepperoni"


class HawaiianPizza(Pizza):
    """Hawaiian pizza."""

    def __init__(self, size: str):
        super().__init__(size)
        self.name = "Hawaiian"
        self.recept = "tomato sauce, mozzarella, chicken, pineapples"
