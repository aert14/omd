import pytest
from pizza_factory import create_pizza
from pizzas import MargheritaPizza, PepperoniPizza, HawaiianPizza

def test_create_margherita_pizza():
    pizza = create_pizza('margherita', 'L')
    assert isinstance(pizza, MargheritaPizza)
    assert pizza.size == 'L'

def test_create_pepperoni_pizza():
    pizza = create_pizza('pepperoni', 'L')
    assert isinstance(pizza, PepperoniPizza)
    assert pizza.size == 'L'

def test_create_hawaiian_pizza():
    pizza = create_pizza('hawaiian', 'L')
    assert isinstance(pizza, HawaiianPizza)
    assert pizza.size == 'L'