def make_pizza(*toppings, base):
    print(toppings, base)


def make_pizza_2(*base, toppings):
    print(base, toppings)


make_pizza("mushroom", "tomato", "cheese", base="thin crust")
make_pizza_2("soft","slightly crust","crust", toppings="onion")