import numpy as np

myNump = [2,3,4,5]
print(myNump)


class mySolarSystem:
    def __init__(self, numPlanets, age, size):
        self.numPlanets = numPlanets
        self.age = age
        self.size = size
        self.defaultColors = ["blue", "red", "green"]

    def blowup(self):
        self.numPlanets = 0
        self.size = self.size+100
        print("ALL PLANETS HAVE BEEN DESTROYED :(")


wanker = mySolarSystem(10, 300, 5000)
print(wanker.numPlanets)
wanker.blowup()
print(wanker.numPlanets)
print(wanker.defaultColors)

print("final added line")



