import math


def add_complex(a, b):
    """
    Takes two complex numbers and returns their sum
    :param a: First complex number as tuple: a + bi -> (a, b)
    :param b: Second complex number as tuple: a + bi -> (a, b)
    :return: Sum of the two complex numbers
    """
    return a[0] + b[0], a[1] + b[1]


def subtract_complex(a, b):
    """
    Takes two complex numbers and returns their difference
    :param a: First complex number as tuple: a + bi -> (a, b)
    :param b: Second complex number as tuple: a + bi -> (a, b)
    :return: Difference of the two complex numbers
    """
    return a[0] - b[0], a[1] - b[1]


def multiply_complex(a, b):
    """
    Takes two complex numbers and returns their product
    :param a: First complex number as tuple: a + bi -> (a, b)
    :param b: Second complex number as tuple: a + bi -> (a, b)
    :return: Product of the two complex numbers
    """
    real = (a[0] * b[0]) - (a[1] * b[1])
    imag = (a[0] * b[1]) + (b[0] * a[1])
    return real, imag


def divide_complex(a, b):
    """
    Takes two complex numbers and returns their quotient
    :param a: First complex number as tuple: a + bi -> (a, b)
    :param b: Second complex number as tuple: a + bi -> (a, b)
    :return: Division of the two complex numbers
    """
    denominator = (b[0] ** 2) + (b[1] ** 2)
    real = ((a[0] * b[0]) + (a[1] * b[1])) / denominator
    imag = ((b[0] * a[1]) - (a[0] * b[1])) / denominator
    return real, imag


def modulus(a):
    """
    Takes one complex number and returns its modulus
    :param a: Complex number as tuple: a + bi -> (a, b)
    :return: The modulus of the complex number
    """
    return math.sqrt(a[0] ** 2 + a[1] ** 2)


def conjugate(a):
    """
    Takes one complex number and returns its conjugate: conjugate ((a, b)) -> (a, -b)
    :param a: Complex number as tuple: a + bi -> (a, b)
    :return:
    """
    return a[0], -a[1]


def phase(a):
    """
        Calculate the phase (argument) of a complex number.

        :param a: Complex number (a, b).
        :return: Phase of the complex number in radians.
        """
    return math.atan2(a[1], a[0])


def cartesian_to_polar(a):
    """
    Takes one complex number in cartesian form and returns its polar form
    :param a: Complex number as tuple: a + bi -> (a, b)
    :return: Polar form of the complex number
    """
    p: float = modulus(a)
    theta = math.atan2(a[1], a[0])
    return p, theta


def polar_to_cartesian(cplx):
    """
    Takes one complex number in polar form and returns its cartesian form
    :param cplx: Complex number as tuple: a + bi -> (a, b)
    :return: Cartesian form of the complex number
    """
    a = cplx[0] * math.cos(cplx[1])
    b = cplx[0] * math.sin(cplx[1])
    return a, b
