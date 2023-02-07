from fractions import Fraction
import math


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def reduce(self):
        if abs(self.numerator) % self.denominator == 0:
            reduce_factor = self.numerator / self.denominator
            self.numerator /= reduce_factor
            self.denominator /= reduce_factor

    def add(self, f: Fraction):
        new_denominator = math.lcm(self.denominator, f.denominator)
        f_new_numerator = f.numerator * (self.denominator / f.denominator)

        self.numerator = (self.numerator * (new_denominator / self.denominator)) + f_new_numerator
        self.denominator = new_denominator
        self.reduce()

    def sub(self, f: Fraction):
        new_denominator = math.lcm(self.denominator, f.denominator)
        f_new_numerator = f.numerator * (self.denominator / f.denominator)

        self.numerator = (self.numerator * (new_denominator / self.denominator)) - f_new_numerator
        self.denominator = new_denominator
        self.reduce()
