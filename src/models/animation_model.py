import math
import random


class Particle:
    def __init__(self, x, y, vx, vy, lifetime,
                 radius, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.age = 0.0
        self.lifetime = lifetime
        self.radius = radius
        self.color = color

    @property
    def is_alive(self):
        if self.age < self.lifetime:
            return True
        else:
            return False

    @property
    def alpha(self):
        remaining = self.lifetime - self.age
        return max(0.0, remaining / self.lifetime)

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.age += dt


class ParticleSystem:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.spawn_rate = 60.0
        self.lifetime = 2.0
        self.speed_min = 20.0
        self.speed_max = 80.0
        self.radius_min = 2.0
        self.radius_max = 5.0
        self.color = (255, 105, 180)
        self.max_particles = 400
        self.particles = []
        self._accum = 0.0

    def update(self, dt):
        self.particles = [p for p in self.particles if p.is_alive]

        self._accum += self.spawn_rate * dt
        while self._accum >= 1.0 and len(self.particles) < self.max_particles:
            self._accum -= 1.0
            self.particles.append(self._create_particle())

        for p in self.particles:
            p.update(dt)

    def _create_particle(self):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(self.speed_min, self.speed_max)
        vx = math.cos(angle) * speed
        vy = math.sin(angle) * speed
        radius = random.uniform(self.radius_min, self.radius_max)
        return Particle(self.x, self.y, vx, vy, self.lifetime, radius,
                        self.color)


class Model:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.systems = []
        self.add_system(width // 2, height // 2)

    def add_system(self, x, y):
        system = ParticleSystem(x, y)
        self.systems.append(system)

    def update(self, dt):
        for system in self.systems:
            system.update(dt)

    def clear(self):
        self.systems.clear()
        self.add_system(self.width // 2, self.height // 2)
