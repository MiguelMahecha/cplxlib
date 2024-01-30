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


def convert_complex(number, to_representation):
    """
    Convert a complex number between cartesian and polar representations.

    :param number: Complex number as tuple: a + bi -> (a, b) or (r, theta).
    :param to_representation: String indicating the desired representation: 'cartesian' or 'polar'.
    :return: Converted complex number.
    """
    if to_representation == 'polar':
        p = modulus(number)
        theta = math.atan2(number[1], number[0])
        return p, theta
    elif to_representation == 'cartesian':
        a = number[0] * math.cos(number[1])
        b = number[0] * math.sin(number[1])
        return a, b
    else:
        raise ValueError("Invalid representation. Please choose 'cartesian' or 'polar'.")
