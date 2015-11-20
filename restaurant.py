meals = {
    1: {
        'name': 'Chicken Burger',
        'price': 16.50
    },
    2: {
        'name': 'Asam Pedas Chicken',
        'price': 6.80
    },
    3: {
        'name': 'Chips',
        'price': 4
    },
    4: {
        'name': 'Drinks Free Flow',
        'price': 0
    }
}

def print_orders(orders):
    """Prints orders"""
    print ""
    print "-"*20
    print "Bill"
    print "-"*20
    order_total = 0
    for key in orders.keys():
        meal = meals[key]
        qty = orders[key]
        price = meal.get('price')
        meal_total = qty * price
        order_total += meal_total
        print "%s (%d * %.2f = RM%.2f)" % (meal['name'], qty, price, meal_total)

    print "\nTotal = RM%.2f" % order_total

def print_menu():
    """Print menu"""
    print "\nPlease choose from our delicious meals."
    print "You may type in '0' when you're done. Thank you."
    for key, meal in meals.items():
        print "(%d) %s RM %.2f" % (key, meal.get("name"), meal.get("price"))

print "Welcome to restaurant"

# orders, item => quantity
orders = {}
select = None

try:
    while select != 0:
        print_menu()
        select = int(raw_input("Your order: "))

        # Get order
        order = meals.get(select)

        if order:
            if select in orders:
                orders[select] += 1
            else:
                orders[select] = 1

        print_orders(orders)

    print_orders(orders)
except EOFError:
    print "\nBye"