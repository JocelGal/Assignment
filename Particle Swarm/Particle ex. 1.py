import random

def fitness(x):
    return x**2

particles = [random.uniform(-10, 10) for _ in range(5)]
velocity = [0 for _ in range(5)]

pbest = particles[:]
gbest = min(particles, key=fitness)

for _ in range(20):
    for i in range(len(particles)):
        velocity[i] = 0.5 * velocity[i] + random.random() * (pbest[i] - particles[i]) \
                      + random.random() * (gbest - particles[i])

        particles[i] += velocity[i]

        if fitness(particles[i]) < fitness(pbest[i]):
            pbest[i] = particles[i]

    gbest = min(particles, key=fitness)

print("Best solution:", gbest)