from .tool import*

class NBFunc: # implements negative binomial distribution.
    def __init__(self, success, p, maximum):
        self.maximum = maximum
        self.p = p
        self.r = success
        self.mew = success*(1-p)/p
        self.var = self.mew/p

    def NBdist(self):
        result = []
        for x in range(1, self.maximum+1):
            nCx = combination(x+self.r-1, self.r-1)
            pmf = nCx*(self.p**self.r)*((1-self.p)**x)
            result.append(pmf)
            if x == self.r:
                location = (x-1, self.targetValue(x)) # reason of "x-1" : matching value of x axis
        return result, self.mew, self.var, location

    def targetValue(self, x):
        #nCx = combination(x-1, self.r-1)
        nCx = combination(x+self.r-1, self.r-1)
        val = nCx*(self.p**self.r)*((1-self.p)**x)
        return val
