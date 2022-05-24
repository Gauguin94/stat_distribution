from .tool import*

class binomialFunc: # implements binomial distribution. 
    def __init__(self, n, p, target):
        self.n = n    
        self.p = p
        self.t = target
        self.mew = n*p
        self.var = self.mew*(1-p)

    def binomialDist(self):
        result = []
        for i in range(1, self.n+1):
            nCx = combination(self.n, i)
            pmf = nCx*(self.p**i)*((1-self.p)**(self.n-i))
            result.append(pmf)
            if i == self.t:
                location = (i-1, self.targetValue()) # reason of "i-1" : matching value of x axis
        return result, self.mew, self.var, location
    
    def targetValue(self):
        nCx = combination(self.n, self.t)
        val = nCx*(self.p**self.t)*((1-self.p)**(self.n-self.t))
        return val
