# 5.2: Order system

def add_order(order, orders, number=1):
    for _ in range(number):
        orders.append(order)

def get_orders(order, orders=None):
    if orders is None:
        orders = []
    return orders + [order]


if __name__ == "__main__":
    current_orders = get_orders('Curry')
    current_orders2 = get_orders('Burger')
    add_order('Pizza', current_orders, 2)
    add_order('Wrap', current_orders2)
    add_order('Pizza', current_orders2)
    print("Current orders: ", current_orders)
    print("Current orders 2: ", current_orders2)
