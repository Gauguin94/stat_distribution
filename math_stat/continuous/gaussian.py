import math
import sympy as sym

class gaussianFunc:
    def __init__(self, mew, var, start=None, goal=None, target=None, maximum=None):
        self.mew=mew
        self.var=var
        self.start=start
        self.goal=goal
        self.target=target
        self.maximum=maximum

    def normDist(self):
        result = []
        x = sym.Symbol('x')
        coef = 1/(math.sqrt(2*sym.pi*self.var))
        for i in range(1, self.maximum+1):
            pdf = coef*math.exp(-(((i-self.mew)**2)/(2*self.var)))
            result.append(pdf)
            if self.target is None:
                pdf = None
            elif i == self.target:
                location = (i-1, pdf)

        if self.goal is not None:
            if self.start is not None:
                cdf = sym.integrate((1/sym.sqrt(2*sym.pi)*sym.sqrt(self.var))*sym.exp(-(((x-self.mew)**2)/(2*self.var))), (x,self.start,self.goal))
            else:
                cdf = sym.integrate((1/sym.sqrt(2*sym.pi)*sym.sqrt(self.var))*sym.exp(-(((x-self.mew)**2)/(2*self.var))), (x,0,self.goal))
        else:
            cdf = None
        return result, self.mew, self.var, location, cdf
