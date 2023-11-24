from pizzas import HawaiianPizza, MargheritaPizza, PepperoniPizza

pizza_classes = {
    "margherita": MargheritaPizza,
    "pepperoni": PepperoniPizza,
    "hawaiian": HawaiianPizza,
}

def create_pizza(pizza_name: str, size: str) -> object:
    """Создает пиццу."""
    pizza_class = pizza_classes[pizza_name.lower()]
    return pizza_class(size)
if __name__ == "__main__":
    pass
