
class Distribution():
    def __init__(self, name=None, density=None):
        assert(name!=None)
        self.name=name
        self.density=density


    def __repr__(self):
        return f"""{"Distribution":>24} : {self.name:>24}
{"density":>24} : {self.density:>24}"""



class Dirac(Distribution):
    def __init__(self, density=1.0):
        super().__init__(name="Dirac", density=density)



class Maxwellian(Distribution):
    def __init__(self, density=1.0, temperature=0.1):
        super().__init__(name="Maxwellian", density=density)
        self.temperature=temperature


    def __repr__(self):
        return f"""{str(Distribution.__repr__(self))}
{"temperature":>24} : {self.temperature:>24}"""

