class IceCreamery:
    def order(self, scoops, toppings):
        if scoops == 1:
            cost = 3
        if scoops == 2:
            cost = 4
        if scoops >= 3:
            cost = 5
        cost += len(toppings) * .50
        return cost
