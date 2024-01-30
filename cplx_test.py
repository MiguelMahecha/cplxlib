import unittest
from cplx import *


class TestComplexOperations(unittest.TestCase):

    def test_add_complex(self):
        self.assertEqual(add_complex((1, 2), (3, 4)), (4, 6))
        self.assertEqual(add_complex((-1, -2), (3, 4)), (2, 2))

    def test_subtract_complex(self):
        self.assertEqual(subtract_complex((1, 2), (3, 4)), (-2, -2))
        self.assertEqual(subtract_complex((-1, -2), (3, 4)), (-4, -6))

    def test_multiply_complex(self):
        self.assertEqual(multiply_complex((1, 2), (3, 4)), (-5, 10))
        self.assertEqual(multiply_complex((-1, -2), (3, 4)), (5, -10))

    def test_divide_complex(self):
        self.assertAlmostEqual(divide_complex((1, 2), (3, 4)), (0.44, 0.08), places=2)
        self.assertAlmostEqual(divide_complex((-1, -2), (3, 4)), (-0.44, -0.08), places=2)

    def test_modulus(self):
        self.assertAlmostEqual(modulus((3, 4)), 5)
        self.assertAlmostEqual(modulus((0, 0)), 0)

    def test_conjugate(self):
        self.assertEqual(conjugate((3, 4)), (3, -4))
        self.assertEqual(conjugate((-3, -4)), (-3, 4))

    def test_phase(self):
        self.assertAlmostEqual(phase((1, 0)), 0, places=7)
        self.assertAlmostEqual(phase((0, 1)), math.pi / 2, places=7)
        self.assertAlmostEqual(phase((-1, 0)), math.pi, places=7)
        self.assertAlmostEqual(phase((0, -1)), -math.pi / 2, places=7)

    def test_convert_complex_cartesian_to_polar(self):
        self.assertAlmostEqual(convert_complex((1, 1), 'polar'), (1.4142135623730951, 0.7853981633974483), places=7)
        self.assertAlmostEqual(convert_complex((-1, -1), 'polar'), (1.4142135623730951, -2.356194490192345),
                               places=7)

    def test_convert_complex_polar_to_cartesian(self):
        self.assertAlmostEqual(convert_complex((1, 1), 'cartesian'), (0.5403023058681398, 0.8414709848078965),
                               places=7)
        self.assertAlmostEqual(convert_complex((1, -1), 'cartesian'), (0.5403023058681398, -0.8414709848078965),
                               places=7)


if __name__ == '__main__':
    unittest.main()
