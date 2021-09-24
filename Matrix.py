import numpy as np
from pprint import pprint
class Matrix:

    individual = [[[]]]

    def fillData(self, population):
        """
        This method fills the matrix with random initial population
        :param population: the initial population of the solution
        :return: matrix filled
        """
        for i in range(population):
            matrix = np.random.randint(1,5,(3,3))
            self.individual.append(matrix)
        self.individual.pop(0)

    def fitness(self, position):
        return self.bottle_fitness(position) + self.wine_fitness(position)

    def bottle_fitness(self, position):
        """
        This method calculates de fitness cost of the repeated bottles
        :return: cost
        """
        cost = 10
        # range -> i=3 and j=3. it's because of the problem
        for i in range(3):
            row = 0
            for j in range(3):
                row += self.individual[position][i][j]
            if row != 7:
                cost -= 1
        return cost

    def wine_fitness(self, position):
        """
        This method calculates the fitness of the measure of wine
        :param value:
        :return: cost
        """
        cost = 10
        full = 1
        empty = 0
        media = 0.5
        col0 = 0
        col1 = 0
        col2 = 0
        for i in range(3):
            for j in range(3):
                if j == 0:
                    if i == 0:
                        col0 += full * self.individual[position][i][j]
                    elif i == 1:
                        col0 += media * self.individual[position][i][j]
                    elif i == 2:
                        col0 += empty * self.individual[position][i][j]
                if j == 1:
                    if i == 0:
                        col1 += full * self.individual[position][i][j]
                    elif i == 1:
                        col1 += media * self.individual[position][i][j]
                    elif i == 2:
                        col1 += empty * self.individual[position][i][j]
                if j == 2:
                    if i == 0:
                        col2 += full * self.individual[position][i][j]
                    elif i == 1:
                        col2 += media * self.individual[position][i][j]
                    elif i == 2:
                        col2 += empty * self.individual[position][i][j]
        if col0 != col1:
            cost -= 2
        if col1 != col2:
            cost -= 2
        if col0 != col2:
            cost -= 2
        return cost

    def first_son(self, position1, position2, wposition1):
        matrix_resultant = [[None for y in range(3)] for x in range(3)]
        for i in range(2):
            for j in range(3):
                matrix_resultant[i][j] = self.individual[position1][i][j]
        for k in range(3):
            matrix_resultant[2][k] = self.individual[position2][2][k]
        self.individual[wposition1] = matrix_resultant

    def second_son(self, position1, position2, wposition2):
        matrix_resultant = [[None for y in range(3)] for x in range(3)]
        for i in range(2):
            for j in range(3):
                matrix_resultant[i][j] = self.individual[position2][i][j]
        for k in range(3):
            matrix_resultant[2][k] = self.individual[position1][2][k]
        self.individual[wposition2] = matrix_resultant

    def first_son_mutation(self, wposition, mutation_probability):
        random_number = np.random.random()
        if random_number <= mutation_probability:
            for i in range(2):
                for j in range(3):
                    self.individual[wposition][i][j] = np.random.randint(1,5)

    def second_son_mutation(self, wposition, mutation_probability):
        random_number = np.random.random()
        if random_number <= mutation_probability:
            for i in range(1,3):
                for j in range(3):
                    self.individual[wposition][i][j] = np.random.randint(1, 5)

    def printMatrix(self, position):
        pprint(self.individual[position])

    def printTotal(self):
        pprint(self.individual)