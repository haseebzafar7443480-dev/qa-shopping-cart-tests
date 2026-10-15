"""A simple shopping cart to practice testing."""


class ShoppingCart:
    def __init__(self):
        self.items = {}  # name -> {"price": float, "qty": int}

    def add_item(self, name, price, qty=1):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if qty <= 0:
            raise ValueError("Quantity must be at least 1")
        if name in self.items:
            self.items[name]["qty"] += qty
        else:
            self.items[name] = {"price": price, "qty": qty}

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"{name} is not in the cart")
        del self.items[name]

    def item_count(self):
        return sum(item["qty"] for item in self.items.values())

    def total(self, discount_percent=0):
        if not 0 <= discount_percent <= 100:
            raise ValueError("Discount must be between 0 and 100")
        subtotal = sum(i["price"] * i["qty"] for i in self.items.values())
        return round(subtotal * (1 - discount_percent / 100), 2)
