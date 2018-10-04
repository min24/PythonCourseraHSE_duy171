class Complex:
    """The class of complex number"""
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        return str(self.re) + '+' + str(self.im) + 'i'

    def __add__(self, other):
        if isinstance(other, Complex):
            result =  Complex(self.re+other.re, self.im+other.im)
            return result
        elif isinstance(other, int) or isinstance(other, float):
            other = Complex(other)
            result = Complex(self.re+other.re, self.im+other.im)
            return result
        else:
            error = ComplexError(self, other)
            raise error

    def __mul__(self, other):
        if isinstance(other, Complex):
            result = Complex(self.re*other.re-self.im*other.im, self.re*other.im+self.im*other.re)
            return result
        elif isinstance(other, int) or isinstance(other, float):
            other = Complex(other)
            result = Complex(self.re*other.re-self.im*other.im, self.re*other.im+self.im*other.re)
            return result
        else:
            error = ComplexError(self, other)
            raise error

    __rmul__ = __mul__
    __radd__ = __add__

class ComplexError(BaseException):
    def __init__(self, complex, other):
        self.first = complex
        self.second = other

a = Complex()
b = Complex(1)
c = Complex(1,2)
print(a)
try:
    print('b'*c)
except ComplexError as ce:
    print("ERROR\nfirstpara:", ce.first, "\nsecondpara:", ce.second, sep=' ')
print(2*c)