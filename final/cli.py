import click
from pizza_factory import create_pizza  # импортируем функцию создания пиццы


@click.group()

def cli():
    """Command line interface for pizza ordering."""

@cli.command(help = "Order a pizza")

@click.argument("pizza_name")

@click.argument("size")

@click.option("--delivery", "-d",
            is_flag = True, default = False,
            help="Enable delivery")

@click.option("--toppings", "-t",
            is_flag = False, default = None,
            multiple = True,
            help="The toppings for the pizza")

def order(pizza_name: str, size: str, delivery: bool, toppings: tuple[str]) -> None:
    """Ordering pizza"""
    ordered_pizza = create_pizza(pizza_name, size) # создаем экземпляр пиццы
    if toppings: # если есть топпинги, добавляем их
        ordered_pizza.add_toppings(toppings)
    ordered_pizza.bake()
    if delivery: # если доставка, то доставляем, иначе самовывоз
        ordered_pizza.deliver()
    else:
        ordered_pizza.pickup()

@cli.command(help = "Show the menu")

def menu() -> None:
    """Show the menu."""
    print(
    "- Margherita 🧀: tomato sauce, mozzarella, tomatoes\n"
    "- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n"
    "- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples\n"
    "- size: L, XL\n"
    "- toppings: basil, oregano, garlic, pepper, onion, pepperoni,\n"
    "  chicken, pineapples, tomatoes, mozzarella, parmesan, cheddar,\n"
    "  dor blue, feta",
    )

if __name__ == "__main__":
    cli()
