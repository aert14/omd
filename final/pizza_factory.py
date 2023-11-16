from pizzas import MargheritaPizza, PepperoniPizza, HawaiianPizza

pizza_classes = {
    'margherita': MargheritaPizza,
    'pepperoni': PepperoniPizza,
    'hawaiian': HawaiianPizza,
}

def create_pizza(pizza_name: str, size: str) -> object:
    pizza_class = pizza_classes[pizza_name.lower()]
    return pizza_class(size)
