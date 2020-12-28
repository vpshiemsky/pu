class Road:
    def __init__(self,_length,_width,_mass,_fat):
        self._length=_length
        self._width=_width
        self._mass = _mass


    def massa(self):
        return self._length*self._width*self._mass*self._fat
class Massacount(Road):
    def __init__(self,_length,_width,_mass,_fat):
        super().__init__(_length,_width,_mass,_fat)

        self._fat = _fat
b=Massacount(20,5000,25,5)
print(b.massa())
