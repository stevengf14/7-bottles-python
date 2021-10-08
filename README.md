# 7_bottles
It's an adaptation of the Problem of 7 bottles, using Genetic Algorithm in Python.

#### The problem
You have 21 bottles of wine. 7 full, 7 half full and 7 empty. And you must distribute to 3 people so that each one has the same amount of wine and the same number of bottles.

#### The solution
The problem request an initial population, the number of iterations, the mutation probability and the cost or fitness that you expect.

**Population:** The algorithm generates a random number of individuals that represent a solution.\
**Iterations:** The populations will reproduce with its best individuals and will sometimes mutate. This process is carried out during n iterations.\
**Mutation:** A random number is compared with the mutation probability and only in this case, it generates new individuals.\
**Cost/Fitness:** The perfect solution will cost 20. But you can enter a different cost to stop the process.

#### Solution Interpretation
**Example:**\
{'iteration': 111,
 'individual': 28,
 'cost': 20,
 'bestSolution': [[2, 1, 4], [2, 1, 4], [2, 1, 4]]}

**Iteration:** Represents the number of iterations that process executed.\
**Individual:** Represents the position of the best individual.\
**Cost:** Represents the fitness cost of the best individual.\
**Best Solution:** Represents a matrix of the best solution.\

In the example, we have the next matrix:\
[[2, 1, 4],\
 [2, 1, 4],\
 [2, 1, 4]]\
The rows represent the number of bottles.\
The columns represent the amount of wine (1rst -> full, 2nd -> half full -> 3rd -> empty).\
So, we have:\
**Number of bottles:**\
2 + 1 + 4 = 7 bottles\
2 + 1 + 4 = 7 bottles\
2 + 1 + 4 = 7 bottles\
**Amount of wine:**\
2 full + 1 half full + 4 empty = 2.5 amount of wine\
2 full + 1 half full + 4 empty = 2.5 amount of wine\
2 full + 1 half full + 4 empty = 2.5 amount of wine