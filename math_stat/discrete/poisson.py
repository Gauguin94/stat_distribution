import math

class poissonFunc:
    def __init__(self, frequency, target, maximum):
        self.m = frequency
        self.x = target
        self.maximum = maximum
        self.mew, self.var = self.m, self.m

    def poissonDist(self):
        result = []
        for i in range(1, self.maximum+1):
            pmf = (math.exp(-self.m)*self.m**i)/math.factorial(i)
            result.append(pmf)
            if i == self.x:
                location = (i-1, self.targetValue()) # reason of "i-1" : matching value of x axis
        return result, self.mew, self.var, location

    def targetValue(self):
        val = (math.exp(-self.m)*self.m**self.x)/math.factorial(self.x)
        return val
