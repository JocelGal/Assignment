import random
import string

target = "HELLO"
population_size = 10

def random_string():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(len(target)))

def fitness(s):
    return sum(1 for i in range(len(target)) if s[i] == target[i])

population = [random_string() for _ in range(population_size)]

for generation in range(100):
    population = sorted(population, key=fitness, reverse=True)

    if population[0] == target:
        break

    parent1, parent2 = population[0], population[1]

    # Crossover
    child = parent1[:2] + parent2[2:]

    # Mutation
    child = ''.join(
        c if random.random() > 0.1 else random.choice(string.ascii_uppercase)
        for c in child
    )

    population[-1] = child

print("Best match:", population[0])