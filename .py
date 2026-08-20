class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def ShowNumber(self):
        print(self.real,"i +", self.imag,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return Complex(newReal, newImag)
num1 = Complex(1,5)
num1.ShowNumber()

num2 = Complex(3,6)
num2.ShowNumber()