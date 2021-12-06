class Rational(object):
    def __init__(self, numer, denom) :
        self.numer = numer
        self.denom = denom
        self._reduce()

    def numerator(self):
        return self.numer

    def denominator(self):
        return self.denom

    def __add__(self, other):
            newNumer = self.numer * other.denom + \
                other.numer * self.denom
            newDenom = self.denom * other.denom
        return Rational(newNumer, newDenom)

    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)
    
    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.numer == other.numer and \
                self.denom == other.denom

    def _reduce(self):
        divisor = self._gcd(self.numer, self.denom)
        self.numer = self.numer // divisor
        self.denom = self.denom // divisor
    
    def __lt__(self, other):
        extremes = self.numer * other.denom
        means = other.numer * self.denom
        return extremes < means

    def _gcd(self, a, b):
        (a, b) = (max(a, b), min(a, b))
        while b > 0:
            (a, b) = (b, a % b)
        return a