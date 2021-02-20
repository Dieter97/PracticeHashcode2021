from pizza.pizza_optimizer import PizzaOptimizer
from pizza.pizza_parser import PizzaParser


def work(input_file: str, output_file: str):
    parser = PizzaParser()
    problem = parser.parse_file(input_file)
    optimizer = PizzaOptimizer(problem[0],problem[1],problem[2],problem[3],problem[4])
    solution = optimizer.calculate_solution()
    write_solution(solution, output_file)

def write_solution(solution, file):
    f = open(file, "w")
    f.write(str(len(solution[0])+len(solution[1])+len(solution[2]))+'\n')
    for i in range(3):
        for k in range(len(solution[i])):
            f.write(solution[i][k]+'\n')
    f.close()

if __name__ == "__main__":
    inputs = ["inputs\\a_example", "inputs\\b_little_bit_of_everything.in","inputs\\c_many_ingredients.in", "inputs\\d_many_pizzas.in", "inputs\\e_many_teams.in"]
    outputs = ["outputs\\out.a", "outputs\\out.b", "outputs\\out.c", "outputs\\out.d", "outputs\\out.e"]
    for i in range(len(inputs)):
        work(inputs[i], outputs[i])
