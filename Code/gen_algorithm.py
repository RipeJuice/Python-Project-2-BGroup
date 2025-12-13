# Python3 program to create target string, starting from
# random string using Genetic Algorithm

import random

BOARD_SIZE = 9  # Side length of the Sudoku (9 for 9x9)
BLOCK_SIZE = 3  # Side length of the square blocks (3 for 3x3)

# Number of individuals in each generation
POPULATION_SIZE = 100

# Valid genes
GENES = '''123456789'''

# Target string to be generated

# For now, will change board later
INITIAL_PUZZLE = "8-7-3---496----3582348-19-7-1---5-4-----4-----4----52----21-43-1-3--48--4-65--1--"
#TARGET = "123456789123456789123456789123456789123456789123456789123456789123456789123456789"
PUZZLE_LENGTH = BOARD_SIZE * BOARD_SIZE
# The indices of the fixed (preset) numbers
FIXED_INDICES = [i for i, char in enumerate(INITIAL_PUZZLE) if char != '-']

class Individual(object):
    '''
    Class representing individual in population
    '''

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @staticmethod
    def random_gene():
        global GENES
        return random.choice(GENES)
    """
    @classmethod
    def mutated_genes(self):
        '''
        create random genes for mutation
        '''
        global GENES
        gene = random.choice(GENES)
        return gene
    """

    @classmethod
    def create_gnome(self):
        '''
        create chromosome or string of genes
        '''

        """
        global TARGET
        gnome_len = len(TARGET)
        return [self.mutated_genes() for _ in range(gnome_len)]
        """

        global INITIAL_PUZZLE, PUZZLE_LENGTH
        gnome = list(INITIAL_PUZZLE)

        for i in range(PUZZLE_LENGTH):
            if gnome[i] == '-':
                gnome[i] = Individual.random_gene()

        return gnome



    def mate(self, par2):
        '''
        Perform mating and produce new offspring
        '''
        """
        # chromosome for offspring
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):

            # random probability
            prob = random.random()

            # if prob is less than 0.45, insert gene
            # from parent 1
            if prob < 0.45:
                child_chromosome.append(gp1)

            # if prob is between 0.45 and 0.90, insert
            # gene from parent 2
            elif prob < 0.90:
                child_chromosome.append(gp2)

            # otherwise insert random gene(mutate),
            # for maintaining diversity
            else:
                child_chromosome.append(self.mutated_genes())

        # create new Individual(offspring) using
        # generated chromosome for offspring
        return Individual(child_chromosome)
        """
        global FIXED_INDICES
        child_chromosome = []

        for i, (gp1, gp2) in enumerate(zip(self.chromosome, par2.chromosome)):
            if i in FIXED_INDICES:
                child_chromosome.append(gp1)
                continue

            prob = random.random()
            if prob < 0.5:  # 50% from parent 1
                child_chromosome.append(gp1)
            else:  # 50% from parent 2
                child_chromosome.append(gp2)

        return Individual(child_chromosome)

    def mutate(self):

        global BOARD_SIZE, BLOCK_SIZE, FIXED_INDICES

        # Choose random block (br, bc)
        br = random.rangrange(BLOCK_SIZE)
        bc = random.randrange(BLOCK_SIZE)

        block_cells = []

        # Get indices of all non-fixed cells within that block
        start_row = br * BLOCK_SIZE
        start_col = bc * BLOCK_SIZE

        for r in range(BLOCK_SIZE):
            for c in range(BLOCK_SIZE):
                index = (start_row + r) * BLOCK_SIZE + (start_col + c)
                if index not in FIXED_INDICES:
                    block_cells.append(index)

        # if block has 2+ variable cells, perform swap
        if len(block_cells) >= 2:
            # Randomly pick two distinct indices
            idx1, idx2 = random.sample(block_cells, 2)

            # Perform swap on chromosomes
            self.chromosome[idx1] = self.chromosome[idx2] = self.chromosome[idx2], self.chromosome[idx1]

        # Calculate fitness again after mutation
        self.fitness = self.cal_fitness()
        return self

    def cal_fitness(self):
        '''
        Calculate fitness score, it is the number of
        characters in string which differ from target
        string. REVISED: it is the number of errors
        '''
        """
        global TARGET
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET):
            if gs != gt: fitness += 1
        return fitness
        """
        global BOARD_SIZE, BLOCK_SIZE
        board = self.chromosome
        errors = 0

        # Helper function (UNCHANGED)
        def count_dupes(segment):
            counts = {}
            segment_errors = 0
            for digit in segment:
                if digit != '-':
                    counts[digit] = counts.get(digit, 0) + 1
            for count in counts.values():
                if count > 1:
                    segment_errors += (count - 1)
            return segment_errors

        # 1. Row Errors (Dynamic loop limit: BOARD_SIZE)
        for r in range(BOARD_SIZE):
            row = board[r * BOARD_SIZE: (r + 1) * BOARD_SIZE]
            errors += count_dupes(row)

        # 2. Column Errors (Dynamic loop limit: BOARD_SIZE)
        for c in range(BOARD_SIZE):
            col = [board[r * BOARD_SIZE + c] for r in range(BOARD_SIZE)]
            errors += count_dupes(col)

        # 3. Block Errors (Dynamic loop limit: BLOCK_SIZE)
        for br in range(BLOCK_SIZE):
            for bc in range(BLOCK_SIZE):
                block = []
                # Start indices are calculated using BLOCK_SIZE
                start_row = br * BLOCK_SIZE
                start_col = bc * BLOCK_SIZE

                # Internal loops are calculated using BLOCK_SIZE
                for r in range(BLOCK_SIZE):
                    for c in range(BLOCK_SIZE):
                        index = (start_row + r) * BOARD_SIZE + (start_col + c)
                        block.append(board[index])
                errors += count_dupes(block)

        return errors


# Driver code
def main():
    """
    global POPULATION_SIZE

    # current generation
    generation = 1

    found = False
    population = []

    # create initial population
    for _ in range(POPULATION_SIZE):
        gnome = Individual.create_gnome()
        population.append(Individual(gnome))

    while not found:

        # sort the population in increasing order of fitness score
        population = sorted(population, key=lambda x: x.fitness)

        # if the individual having lowest fitness score ie.
        # 0 then we know that we have reached to the target
        # and break the loop
        if population[0].fitness <= 0:
            found = True
            break

        # Otherwise generate new offsprings for new generation
        new_generation = []

        # Perform Elitism, that mean 10% of fittest population
        # goes to the next generation
        s = int((10 * POPULATION_SIZE) / 100)
        new_generation.extend(population[:s])

        # From 50% of fittest population, Individuals
        # will mate to produce offspring
        s = int((90 * POPULATION_SIZE) / 100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)

        population = new_generation

        print("Generation: {}\tString: {}\tFitness: {}". \
              format(generation,
                     "".join(population[0].chromosome),
                     population[0].fitness))

        generation += 1

    print("Generation: {}\tString: {}\tFitness: {}". \
          format(generation,
                 "".join(population[0].chromosome),
                 population[0].fitness))
    """
    global POPULATION_SIZE, INITIAL_PUZZLE, BOARD_SIZE

    generation = 1
    found = False
    population = []

    # create initial population
    for _ in range(POPULATION_SIZE):
        gnome = Individual.create_gnome()
        population.append(Individual(gnome))

    print(f"Initial Puzzle ({BOARD_SIZE}x{BOARD_SIZE}): {INITIAL_PUZZLE}")
    print("Starting Genetic Algorithm to Solve Sudoku...")


    while not found:


        population = sorted(population, key=lambda x: x.fitness)

        if population[0].fitness <= 0:
            found = True
            break

        new_generation = []
        s = int((10 * POPULATION_SIZE) / 100)
        new_generation.extend(population[:s])

        s = int((90 * POPULATION_SIZE) / 100)
        mating_pool = population[:POPULATION_SIZE // 2]

        for _ in range(s):
            parent1 = random.choice(mating_pool)
            parent2 = random.choice(mating_pool)
            child = parent1.mate(parent2)

            if random.random() < 0.08: # 8% mutation chance
                child = child.mutate()

            new_generation.append(child)

        population = new_generation

        print("Generation: {}\tFitness: {}\tBest Guess (Row 1): {}". \
              format(generation,
                     population[0].fitness,
                     "".join(population[0].chromosome[:BOARD_SIZE]))) # Use BOARD_SIZE

        generation += 1

    print("\n*** SUDOKU SOLUTION FOUND ***")
    print("Generation: {}\tFitness: {}". \
          format(generation, population[0].fitness))

    solution_string = "".join(population[0].chromosome)
    print("Solution Board:")
    for i in range(BOARD_SIZE): # Use BOARD_SIZE
        print("  " + " ".join(solution_string[i*BOARD_SIZE : (i+1)*BOARD_SIZE]))


if __name__ == '__main__':
    main()
