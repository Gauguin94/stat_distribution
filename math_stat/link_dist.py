# 구현한 분포를 불러오는 역할

from continuous import*
from discrete import*

class linkToDist:
    def __init__(self):
        pass

    def switch(self, arg):
        self.case_ = "case_"+str(arg)
        self.case = getattr(self, self.case_, lambda:"default")
        return self.case()

    def case_B(self):
        binoLoad = binomialFunc(n=50, p=0.1, target=1)
        binoInfo, mew, var, location = binoLoad.binomialDist()
        showPlot(binoInfo, mew, location)

    def case_NB(self):
        NBLoad = NBFunc(success=2, p=0.5, maximum=20)
        NBInfo, mew, var, location = NBLoad.NBdist()
        showPlot(NBInfo, mew, location)

    def case_G(self):
        geoLoad = geoFunc(failure=20, p=0.1)
        geoInfo, mew, var = geoLoad.geoDist()
        showPlot(geoInfo, mew)

    def case_P(self):
        poiLoad = poissonFunc(frequency=2, target=3, maximum=20)
        poissonInfo, mew, var, location = poiLoad.poissonDist()
        showPlot(poissonInfo, mew, location)

    def case_r(self):
        pop_mean = 0.5
        gammaLoad = gammaFunc(alpha=5, beta=1/pop_mean, goal=10, target = 10, maximum=100)
        gammaInfo, mew, var, location, cdf = gammaLoad.gammaDist()
        print(cdf)
        showPlot(gammaInfo, mew, location, False)

    def case_X_2(self):
        chiLoad = chiFunc(dof=10, target = 12, maximum=100)
        chiInfo, mew, var, location = chiLoad.chiDist()
        showPlot(chiInfo, mew, location, False)

    def case_Beta(self):
        betaLoad = betaFunc(alpha=0.5, beta=0.5, maximum=100)
        betaInfo, mew, var = betaLoad.betaDist()
        showPlot(betaInfo, mew, None, False)

    def case_N(self):
        gaussianLoad = gaussianFunc(mew=50, var=100, goal=50, target = 50, maximum=100)
        normInfo, mew, var, location, cdf = gaussianLoad.normDist()
        print(cdf)
        showPlot(normInfo, mew, location, False)
