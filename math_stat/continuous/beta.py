import math
import numpy as np

class betaFunc:
    def __init__(self, alpha, beta, maximum=None):
        self.alpha = alpha
        self.beta = beta
        self.maximum = maximum
        self.mew = alpha/(alpha+beta)
        self.var = (alpha*beta)/((alpha+beta+1)*(alpha+beta)**2)
    
    def betaDist(self):
        result = []
        x_lin = np.linspace(0,0.99,self.maximum)
        coef = math.gamma(self.alpha+self.beta)/(math.gamma(self.alpha)*math.gamma(self.beta))

        for x in x_lin:
            x_expr_1 = x**(self.alpha-1) 
            x_expr_2 = (1-x)**(self.beta-1)
            pdf = coef*(x_expr_1)*(x_expr_2)
            result.append(pdf)

        return result, self.mew, self.var
