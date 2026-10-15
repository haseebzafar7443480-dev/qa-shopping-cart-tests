# Shopping Cart Test Suite

A beginner QA project: automated tests in Python (pytest) for a shopping cart.

## What is tested
- Adding and removing items
- Total price and item count
- Discount calculation (0 to 100 percent)
- Invalid input: negative price, zero quantity, missing item

## Testing techniques used
- **Fixtures:** a fresh cart is created for every test
- **Boundary testing:** discounts of -1 and 101
- **Negative testing:** invalid inputs raise errors
- **Parametrized tests**

## How to run
```
pip install pytest
pytest -v
```
