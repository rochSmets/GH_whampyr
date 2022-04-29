
from .distribution import Dirac
from .distribution import Maxwellian



class Population():
    def __init__(self, name, mass, charge, distribution=Dirac()):
        self.name=name
        self.mass=mass
        self.charge=charge
        self.distribution=distribution


    def __repr__(self):
        return f"""......................................................
{"name":>24} : {self.name:>24}
{"mass":>24} : {self.mass:>24}
{"charge":>24} : {self.charge:>24}
{str(self.distribution)}"""



class Electron(Population):
    def __init__(self, distribution=Dirac()):
        super().__init__(name="electron", mass=1.0, charge=-1.0, distribution=distribution)



class Proton(Population):
    def __init__(self, distribution=Dirac()):
        super().__init__(name="proton", mass=1836.0, charge=1.0, distribution=distribution)

