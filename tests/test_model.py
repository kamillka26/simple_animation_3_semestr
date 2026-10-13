import unittest

from src.models.animation_model import Model, Particle


class TestParticle(unittest.TestCase):
    def test_alpha_start(self):
        p = Particle(0, 0, 0, 0, 2.0, 3, (255, 0, 0))
        self.assertAlmostEqual(p.alpha, 1.0)

    def test_alpha_middle(self):
        p = Particle(0, 0, 0, 0, 2.0, 3, (255, 0, 0))
        p.age = 1.0
        self.assertAlmostEqual(p.alpha, 0.5)

    def test_update(self):
        p = Particle(0, 0, 10, 5, 5.0, 1, (0, 0, 0))
        p.update(1.0)
        self.assertAlmostEqual(p.x, 10.0)
        self.assertAlmostEqual(p.y, 5.0)


class TestModel(unittest.TestCase):
    def test_add_system(self):
        m = Model(800, 600)
        m.add_system(100, 100)
        self.assertEqual(len(m.systems), 2)

    def test_clear(self):
        m = Model(800, 600)
        m.add_system(10, 10)
        m.clear()
        self.assertEqual(len(m.systems), 1)


if __name__ == "__main__":
    unittest.main()
