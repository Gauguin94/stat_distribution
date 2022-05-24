import math

class chiFunc:
    def __init__(self, dof, target=None, maximum=None):
        self.dof = dof # degree of freedom
        self.beta = 2
        self.target = target
        self.maximum = maximum
        self.mew = dof
        self.var = 2*dof

    def chiDist(self):
        result = []
        gamma = math.gamma(self.dof/2)
        coef = gamma*(self.beta**(self.dof/2))
        for i in range(1, self.maximum+1):
            pdf = ((i**((self.dof/2)-1))*math.exp(-i/self.beta))/coef
            result.append(pdf)
            if self.target is None:
                pdf = None
            elif i == self.target:
                location = (i-1, pdf)
        return result, self.mew, self.var, location
