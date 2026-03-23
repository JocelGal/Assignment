import random

def fitness(x, y):
    return x**2 + y**2

particles = [[random.uniform(-5,5), random.uniform(-5,5)] for _ in range(5)]
velocity = [[0,0] for _ in range(5)]

pbest = particles[:]
gbest = min(particles, key=lambda p: fitness(p[0], p[1]))

for _ in range(20):
    for i in range(len(particles)):
        for d in range(2):
            velocity[i][d] = 0.5 * velocity[i][d] \
                + random.random() * (pbest[i][d] - particles[i][d]) \
                + random.random() * (gbest[d] - particles[i][d])

            particles[i][d] += velocity[i][d]

        if fitness(*particles[i]) < fitness(*pbest[i]):
            pbest[i] = particles[i]

    gbest = min(particles, key=lambda p: fitness(p[0], p[1]))

print("Best solution:", gbest)