VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol):
    symbol = symbol.upper().strip()

    if len(symbol) < 6:
        raise ValueError("Invalid trading symbol.")

    return symbol


def validate_side(side):
    """
    Validate BUY or SELL.
    """
    side = side.upper()

    if side not in VALID_SIDES:
        raise ValueError(
            f"Invalid side. Choose one of: {', '.join(VALID_SIDES)}"
        )

    return side


def validate_order_type(order_type):
    """
    Validate MARKET or LIMIT.
    """
    order_type = order_type.upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(
            f"Invalid order type. Choose one of: {', '.join(VALID_ORDER_TYPES)}"
        )

    return order_type


def validate_quantity(quantity):
    """
    Quantity must be greater than zero.
    """
    quantity = float(quantity)

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return quantity


def validate_price(price, order_type):
    """
    Price is required only for LIMIT orders.
    """
    if order_type.upper() == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")

        price = float(price)

        if price <= 0:
            raise ValueError("Price must be greater than zero.")

        return price

    return None