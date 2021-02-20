
from pizza.pizza import Pizza

class PizzaParser:

    def __init__(self):
        super().__init__()

    def parse_file(self,input_file):
        f = open(input_file)
        
        n_pizza, n2, n3, n4 = (int(s) for s in f.readline().split())
        pizzas = []
        i = 0
        for line in f:
            info = line.split()
            pizzas.append(Pizza(i, int(info[0]), info[1:]))
            i += 1
        pizzas.sort(key=lambda x: x.n_in, reverse=True)
        return n_pizza, n2, n3, n4, pizzas