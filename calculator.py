
def calculate_total(price, quantity):
    """Calculate the total cost of an order."""

    if price < 0:
        raise ValueError("Price cannot be negative")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    return price + quantity
