import random

# --- GLOBAL BOARD CONFIGURATION ---
BOARD_SIZE = 9  # Side length of the Sudoku (9 for 9x9)
BLOCK_SIZE = 3  # Side length of the square blocks (3 for 3x3)
# ----------------------------------

# Number of individuals in each generation (Adjusted based on your testing)
POPULATION_SIZE = 5000

# Valid genes
GENES = '''123456789'''

# The initial Sudoku puzzle string. '-' represents an empty cell.
INITIAL_PUZZLE = "8-7-3---496----3582348-19-7-1---5-4-----4-----4----52----21-43-1-3--48--4-65--1--"
PUZZLE_LENGTH = BOARD_SIZE * BOARD_SIZE
# The indices of the fixed (preset) numbers
FIXED_INDICES = [i for i, char in enumerate(INITIAL_PUZZLE) if char != '-']


class Individual(object):
    '''
    Class representing individual in population (a potential solution board)
    '''

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @staticmethod
    def random_gene():
        global GENES
        return random.choice(GENES)

    @classmethod
    def create_gnome(cls):
        global INITIAL_PUZZLE, PUZZLE_LENGTH
        gnome = list(INITIAL_PUZZLE)

        for i in range(PUZZLE_LENGTH):
            if gnome[i] == '-':
                gnome[i] = Individual.random_gene()

        return gnome

    def mate(self, par2):
        '''
        Performs SIMPLE UNIFORM CROSSOVER.
        '''
        global FIXED_INDICES
        child_chromosome = []

        for i, (gp1, gp2) in enumerate(zip(self.chromosome, par2.chromosome)):
            if i in FIXED_INDICES:
                child_chromosome.append(str(gp1))
                continue

            prob = random.random()

            if prob < 0.5:
                child_chromosome.append(str(gp1))
            else:
                child_chromosome.append(str(gp2))

        return Individual(child_chromosome)

    def mutate(self):
        ''' Block-Swap Mutation (Standard) '''
        global BOARD_SIZE, BLOCK_SIZE, FIXED_INDICES

        br = random.randrange(BLOCK_SIZE)
        bc = random.randrange(BLOCK_SIZE)
        block_cells = []

        start_row = br * BLOCK_SIZE
        start_col = bc * BLOCK_SIZE

        for r in range(BLOCK_SIZE):
            for c in range(BLOCK_SIZE):
                index = (start_row + r) * BOARD_SIZE + (start_col + c)

                if index not in FIXED_INDICES:
                    block_cells.append(index)

        if len(block_cells) >= 2:
            idx1, idx2 = random.sample(block_cells, 2)
            self.chromosome[idx1], self.chromosome[idx2] = self.chromosome[idx2], self.chromosome[idx1]

        self.fitness = self.cal_fitness()
        return self

    def forced_row_mutate(self):
        '''
        Performs a forced mutation: Picks one random non-fixed cell and assigns it a completely new,
        random digit. This is highly disruptive and used to escape deep local minima.
        '''
        global PUZZLE_LENGTH, FIXED_INDICES

        # 1. Choose a random non-fixed cell index
        variable_indices = [i for i in range(PUZZLE_LENGTH) if i not in FIXED_INDICES]

        if not variable_indices:
            # Should not happen on a real Sudoku puzzle
            return self

        idx = random.choice(variable_indices)

        # 2. Assign a new, random digit to that position
        self.chromosome[idx] = Individual.random_gene()

        # Re-calculate fitness after mutation
        self.fitness = self.cal_fitness()
        return self

    def cal_fitness(self):
        ''' Calculate fitness score based on Sudoku rule violations. '''
        global BOARD_SIZE, BLOCK_SIZE
        board = self.chromosome
        errors = 0

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

        # 1. Row Errors
        for r in range(BOARD_SIZE):
            row = board[r * BOARD_SIZE: (r + 1) * BOARD_SIZE]
            errors += count_dupes(row)

        # 2. Column Errors
        for c in range(BOARD_SIZE):
            col = [board[r * BOARD_SIZE + c] for r in range(BOARD_SIZE)]
            errors += count_dupes(col)

        # 3. Block Errors
        for br in range(BLOCK_SIZE):
            for bc in range(BLOCK_SIZE):
                block = []
                start_row = br * BLOCK_SIZE
                start_col = bc * BLOCK_SIZE

                for r in range(BLOCK_SIZE):
                    for c in range(BLOCK_SIZE):
                        index = (start_row + r) * BOARD_SIZE + (start_col + c)
                        block.append(board[index])
                errors += count_dupes(block)

        return errors


# Driver code
def main():
    global POPULATION_SIZE, INITIAL_PUZZLE, BOARD_SIZE

    generation = 1
    found = False
    population = []

    for _ in range(POPULATION_SIZE):
        gnome = Individual.create_gnome()
        population.append(Individual(gnome))

    print(f"Initial Puzzle ({BOARD_SIZE}x{BOARD_SIZE}): {INITIAL_PUZZLE}")
    print(f"Starting Genetic Algorithm to Solve Sudoku (Pop Size: {POPULATION_SIZE})...")

    while not found:
        population = sorted(population, key=lambda x: x.fitness)
        best_fitness = population[0].fitness

        if best_fitness <= 0:
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

            # --- HYPER-MUTATION LOGIC ---
            # If stuck at low fitness (<= 2), use aggressive Row-Swap (15% chance)
            if best_fitness <= 2 and random.random() < 0.15:
                child = child.forced_row_mutate()
            # Otherwise, use the standard Block-Swap (8% chance)
            elif random.random() < 0.08:
                child = child.mutate()

            new_generation.append(child)

        population = new_generation

        if generation % 10 == 0 or generation == 1:
            print("Generation: {}\tFitness: {}\tBest Guess (Row 1): {}". \
                  format(generation,
                         population[0].fitness,
                         "".join(population[0].chromosome[:BOARD_SIZE])))

        generation += 1

    print("\n*** SUDOKU SOLUTION FOUND ***")
    print("Generation: {}\tFitness: {}". \
          format(generation, population[0].fitness))

    solution_string = "".join(population[0].chromosome)
    print("Solution Board:")
    for i in range(BOARD_SIZE):
        print("  " + " ".join(solution_string[i * BOARD_SIZE: (i + 1) * BOARD_SIZE]))


if __name__ == '__main__':
    main()