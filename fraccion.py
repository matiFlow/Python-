class Fraccion:

    def __init__(self,num,den) -> None:
        self.num = num
        self.den = den
    
    def __str__(self) -> str:
        return f"{self.num}/{self.den}"
    
    def __eq__(self, otro: object) -> bool:
        return self.num == otro.num and self.den == otro.den
    
    def mcd(self,numerador,denominador):
        while numerador%denominador != 0:
            mViejo = numerador
            nViejo = denominador

            numerador = nViejo
            denominador = mViejo%nViejo
        return denominador
    
    def __add__(self,otro):
        numerador = self.num * otro.num + self.den * otro.den
        denominador = self.den * otro.den
        comun = self.mcd(numerador,denominador)
        return Fraccion(numerador//comun,denominador//comun)



miFraccion = Fraccion(2,3)
miFraccion2 = Fraccion(5,4)
suma = miFraccion + miFraccion2
print(suma)
assert miFraccion != miFraccion2

assert miFraccion.__str__() == "2/3"