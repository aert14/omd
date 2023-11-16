import click.testing
import pytest
from cli import cli


def test_order_pizza_no_delivery():
    runner = click.testing.CliRunner()
    result = runner.invoke(cli, ["order", "pepperoni", "L", "-t", "pepperoni"])
    result = result.output.split()
    assert "Добавлены" in result
    assert "pepperoni" in result
    assert "🍳Приготовили" in result
    assert "🏡Забрали" in result

def test_order_pizza_no_toppings():
    runner = click.testing.CliRunner()
    result = runner.invoke(cli, ["order", "hawaiian", "L", "--delivery"])
    result = result.output.split()
    assert "Добавлены" not in result
    assert "🍳Приготовили" in result
    assert "🛵Доставили" in result