import pytest
from cart import ShoppingCart


@pytest.fixture
def cart():
    """A fresh cart with two items before every test."""
    c = ShoppingCart()
    c.add_item("Pen", 2.5, 4)
    c.add_item("Notebook", 5.0, 2)
    return c


def test_empty_cart_total_is_zero():
    assert ShoppingCart().total() == 0


def test_item_count(cart):
    assert cart.item_count() == 6


def test_total(cart):
    assert cart.total() == 20.0


def test_adding_same_item_increases_quantity(cart):
    cart.add_item("Pen", 2.5, 1)
    assert cart.item_count() == 7


def test_remove_item(cart):
    cart.remove_item("Pen")
    assert cart.total() == 10.0


def test_remove_missing_item_raises_error(cart):
    with pytest.raises(KeyError):
        cart.remove_item("Laptop")


def test_discount(cart):
    assert cart.total(discount_percent=10) == 18.0


@pytest.mark.parametrize("discount", [-1, 101])
def test_invalid_discount_raises_error(cart, discount):
    with pytest.raises(ValueError):
        cart.total(discount_percent=discount)


def test_negative_price_raises_error():
    with pytest.raises(ValueError):
        ShoppingCart().add_item("Bad", -5)


@pytest.mark.parametrize("qty", [0, -3])
def test_invalid_quantity_raises_error(qty):
    with pytest.raises(ValueError):
        ShoppingCart().add_item("Pen", 2, qty)
