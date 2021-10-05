from matrix import Matrix

def startProcess(population, iterations, mutation_probability, fiability):
    matrix = Matrix()
    best1 = 0
    best2 = 0
    position1 = 0
    position2 = 0
    worst1 = 1000
    worst2 = 1000
    wposition1 = 0
    wposition2 = 0
    number = 0

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
            # print(f'Individual {i}: Cost = {fit}')
            # print(matrix.individual(i))

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

        # Validating the worst individuals
        for i in range(population):
            if fitness[i] < worst1:
                positon_aux = i
                if positon_aux != position1:
                    worst1 = fitness[i]
                    wposition1 = i
        for i in range(population):
            if fitness[i] < worst2:
                positon_aux = i
                if positon_aux != wposition1 and positon_aux != position1 and positon_aux != position2:
                    worst2 = fitness[i]
                    wposition2 = i
        # print(f'Best 1: {position1} and Best 2: {position2}')
        # print(f'Worst 1: {wposition1} and Worst 2: {wposition2}')
        # print(f'{number} Iteration'.center(50, '-'))

        # Validating if the fitness of the best individual is better than the entered fiability
        if best1 >= fiability:
            break

        # Reproduction of the best individuals
        matrix.first_son(position1, position2, wposition1)
        matrix.second_son(position1, position2, wposition2)

        # Mutation
        matrix.first_son_mutation(wposition2, mutation_probability)
        matrix.second_son_mutation(wposition1, mutation_probability)

        # Restart variables
        best1 = 0
        best2 = 0
        worst1 = 1000
        worst2 = 1000
    response = {
        'Iteration': number,
        'Individual': position1,
        'Cost': matrix.fitness(position1),
        'Best Solution': matrix.individual[position1]
    }
    return response


