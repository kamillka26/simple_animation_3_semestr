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

