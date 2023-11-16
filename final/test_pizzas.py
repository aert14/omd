import contextlib
import io
import sys

import pytest
from pizzas import HawaiianPizza, MargheritaPizza, PepperoniPizza


def test_pizza_creation():
    """Test pizza creation."""
    pizza_1 = MargheritaPizza("L")
    pizza_2 = HawaiianPizza("XL")
    pizza_3 = PepperoniPizza("L")

    assert pizza_1.name == "Margherita"
    assert pizza_1.size == "L"
    assert pizza_1.recept == "tomato sauce, mozzarella, tomatoes"

    assert pizza_2.name == "Hawaiian"
    assert pizza_2.size == "XL"
    assert pizza_2.recept == "tomato sauce, mozzarella, chicken, pineapples"

    assert pizza_3.name == "Pepperoni"
    assert pizza_3.size == "L"
    assert pizza_3.recept == "tomato sauce, mozzarella, pepperoni"

def test_pizza_equality():
    """Test pizza equality."""
    pizza1 = MargheritaPizza("L")
    pizza2 = MargheritaPizza("L")
    assert pizza1 == pizza2

    pizza3 = PepperoniPizza("L")
    assert pizza1 != pizza3

def test_dict():
    """Test pizza dict."""
    pizza = MargheritaPizza("L")
    with io.StringIO() as buf, contextlib.redirect_stdout(buf):
        pizza.dict()
        output = buf.getvalue()
    assert output == "Рецепт: tomato sauce, mozzarella, tomatoes\n"
