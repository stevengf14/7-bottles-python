import geneticAlgorithm
from pprint import pprint

# Input values
population = int(input('Enter the population: '))
iterations = int(input('Enter the number of iterations: '))
mutation_probability = float(input('Enter the Probability of mutation (between 0 and 1): '))
fiability = int(input('Enter the fiability (value between 0 and 20): '))

response = geneticAlgorithm.startProcess(population, iterations, mutation_probability, fiability)
pprint(response, sort_dicts=False)