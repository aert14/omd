import pytest
from pizzas import MargheritaPizza, PepperoniPizza, HawaiianPizza


def test_pizza_creation():
    """Test pizza creation."""
    pizza = MargheritaPizza("L")
    assert pizza.name == "Margherita"
    assert pizza.size == "L"

def test_pizza_equality():
    """Test pizza equality."""
    pizza1 = MargheritaPizza("L")
    pizza2 = MargheritaPizza("L")
    assert pizza1 == pizza2

    pizza3 = PepperoniPizza("L")
    assert pizza1 != pizza3