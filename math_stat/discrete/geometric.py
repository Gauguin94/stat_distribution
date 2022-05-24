class geoFunc: # implements geometric distribution.
    def __init__(self, failure, p):
        self.y = failure
        self.p = p
        self.mew = (1-p)/p
        self.var = self.mew/p

    def geoDist(self):
        result = []
        for i in range(1, self.y+1):
            pmf = (self.p)*((1-self.p)**i)
            result.append(pmf)
        return result, self.mew, self.var
