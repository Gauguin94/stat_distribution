import math
import sympy as sym

class gammaFunc:
    def __init__(self, alpha, beta, start=None, goal=None, target=None, maximum=None):
        self.alpha = alpha
        self.beta = beta
        self.start = start
        self.goal = goal
        self.target = target
        self.maximum = maximum
        self.mew = alpha*beta
        self.var = self.mew*beta

    def gammaDist(self):
        result = []
        x = sym.Symbol('x')
        gamma = math.gamma(self.alpha)
        for i in range(1, self.maximum+1):
            pdf = ((i**(self.alpha-1))*math.exp(-i/self.beta))/(gamma*(self.beta**self.alpha))
            result.append(pdf)
            if self.target is None:
                pdf = None
            elif i == self.target:
                location = (i-1, pdf)

        if self.goal is not None:
            if self.start is not None:
                cdf = sym.integrate(((x**(self.alpha-1))*sym.exp(-x/self.beta))/(gamma*(self.beta**self.alpha)), (x, self.start, self.goal))
            else:
                cdf = sym.integrate(((x**(self.alpha-1))*sym.exp(-x/self.beta))/(gamma*(self.beta**self.alpha)), (x, 0, self.goal))
        else:
            cdf = None
        return result, self.mew, self.var, location, cdf
