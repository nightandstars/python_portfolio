position_value = lambda position: position.quantity * position.purchase_price

absolute_earnings = lambda position, actual_prices: (actual_prices.purchase_price - position.purchase_price) * position.quantity

yield_in_percent = lambda actual_price, positions: ((actual_price.purchase_price - positions.purchase_price) / positions.purchase_price) * 100 if is_above_0(positions.purchase_price) else "buying_price must be above 0"

actual_value = lambda quantity, actual_price: quantity * actual_price

is_above_0 = lambda to_check: bool(to_check) > 0