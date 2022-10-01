def make_pizza(size, *toppings):
    """Summarize a pizza were about to make"""
    print(f"We're making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(12,'three meat', 'onion', 'bell pepper')
make_pizza(24,'pepperoni')
    
