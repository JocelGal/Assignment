import random

# Fitness function
def fitness(x):
    return x**2

# Create population
population = [random.randint(0, 31) for _ in range(6)]

for generation in range(10):
    population = sorted(population, key=fitness, reverse=True)

    # Select best 2
    parent1, parent2 = population[0], population[1]

    # Crossover
    child = (parent1 + parent2) // 2

    # Mutation
    if random.random() < 0.1:
        child += random.randint(-2, 2)

    population[-1] = child

print("Best solution:", max(population, key=fitness))