import pytest
from pizza_factory import create_pizza
from pizzas import HawaiianPizza, MargheritaPizza, PepperoniPizza


def test_create_margherita_pizza():
    """Test create margherita pizza."""
    pizza = create_pizza("margherita", "L")
    assert isinstance(pizza, MargheritaPizza)
    assert pizza.size == "L"

def test_create_pepperoni_pizza():
    """Test create pepperoni pizza."""
    pizza = create_pizza("pepperoni", "L")
    assert isinstance(pizza, PepperoniPizza)
    assert pizza.size == "L"

def test_create_hawaiian_pizza():
    """Test create hawaiian pizza."""
    pizza = create_pizza("hawaiian", "L")
    assert isinstance(pizza, HawaiianPizza)
    assert pizza.size == "L"
