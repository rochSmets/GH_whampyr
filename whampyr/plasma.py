
import numpy as np



class Plasma():
    def __init__(self, populations, B):
        self.populations=populations
        self.B=B
        self.wp={}
        self.wc={}

        for pop in populations:
            name=pop.name
            self.wp.update({name : np.sqrt(pop.distribution.density*pop.charge*pop.charge/pop.mass)})
            self.wc.update({name : self.B*pop.charge/pop.mass})


    def __repr__(self):
        __s1='\n'.join([str(pop) for pop in self.populations])

        __s2='^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n'
        for pop in self.populations:
            __s2=__s2+"  w_cyclotron{:>11} : {:>24}\n".format(pop.name, self.wc[pop.name])
            __s2=__s2+"  w_plasma{:>14} : {:>24}\n".format(pop.name, self.wp[pop.name])
            __s2=__s2+"  |w_c / wp|{:>12} : {:>24}\n".format(pop.name, np.fabs(self.wc[pop.name]/self.wp[pop.name]))

        return f"""======================================================
{"B field":>24} : {self.B:>24}\n"""+__s1+'\n'+__s2

