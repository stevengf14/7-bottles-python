from Matrix import Matrix

matrix = Matrix()
fiability = 0
best1 = 0
best2 = 0
position1 = 0
position2 = 0
positon_aux = -1
worst1 = 1000
worst2 = 1000
wposition1= 0
wposition2 =0
validator = False
number = 0
population = int(input('Enter the population: '))
iterations = int(input('Enter the number of iterations: '))
mutation_probability = float(input('Enter the Probability of mutation (between 0 and 1): '))
fiability = int(input('Enter the fiability (value between 0 and 20): '))
# Init the population of random individuals
matrix.fillData(population)

# The process starts here
while number < iterations:
    number += 1
    fitness = []
    # Calculatig fitness per individual
    for i in range(population):
        fit = matrix.fitness(i)
        fitness.append(fit)
        print(f'Individual {i}: Cost = {fit}')
        matrix.printMatrix(i)

    # Validating the best individuals
    for i in range(population):
        if fitness[i] > best1:
            best1 = fitness[i]
            position1 = i
    for i in range(population):
        if fitness[i] > best2:
            positon_aux = i
            if positon_aux != position1:
                best2 = fitness[i]
                position2 = i
    positon_aux = -1

    # Validating the worst individuals
    for i in range(population):
        if fitness[i] < worst1:
            positon_aux = i
            if positon_aux != position1:
                worst1 = fitness[i]
                wposition1 = i
    position_aux = -1
    for i in range(population):
        if fitness[i] < worst2:
            positon_aux = i
            if positon_aux != wposition1 and positon_aux != position1 and positon_aux != position2:
                worst2 = fitness[i]
                wposition2 = i
    position_aux = -1
    print(f'Best 1: {position1} and Best 2: {position2}')
    print(f'Worst 1: {wposition1} and Worst 2: {wposition2}')
    print(f'{number} Iteration'.center(50, '-'))
    if best1 >= fiability:
        validator = True
        break

    # Reproduction of the best individuals
    matrix.first_son(position1, position2, wposition1)
    matrix.second_son(position1, position2, wposition2)

    # Mutation
    matrix.first_son_mutation(wposition2, mutation_probability)
    matrix.second_son_mutation(wposition1, mutation_probability)
    best1 = 0
    best2 = 0
    worst1 = 1000
    worst2 = 1000
response = {
    'Iteration': number,
    'Individual': position1,
    'Cost': matrix.fitness(position1),
}
print(response, '\n Best Solution: ')
matrix.printMatrix(position1)
# matrix.printTotal()

