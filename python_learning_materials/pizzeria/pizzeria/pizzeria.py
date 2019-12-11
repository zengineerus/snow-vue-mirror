class Size():
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Topping():
    PEPPERONI = 1
    SAUSAGE = 2
    MUSHROOMS = 3
    OLIVES = 4


class Pizzeria():
    def order(self, size, toppings):
        if size == 1:
            cost = 10
        if size == 2:
            cost = 15
        if size == 3:
            cost = 20
        for topping in toppings:
            if topping == 1 or topping == 2:
                cost += 2
            if(topping == 3 or topping == 4):
                cost += 1
        return cost
