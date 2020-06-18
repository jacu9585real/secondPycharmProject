print("here is your second script boy")
myVar = 82


for x in range(10):
    print(x*57)
    print(myVar)


class energyDrink:
    def __init__(self, shape, color, ounces="12"):
        self.ounces = ounces
        self.shape = shape
        self.color = color
        print("NEW CAN HAS BEEN CREATED :)")
    def recycle(self):
        print("clang clang clang!")
        self.shape = "flat"
        self.ounces = 0

class monster(energyDrink):
    def drink(self):
        print("SSSUUUUUUPER ENERGY BOD")

class reign(energyDrink):
    def drink(self):
        print("You have choosen to ingest reign.. do not pass go do not collect $200 and don't sleep ever again")
        self.ounces = 0
    def recycle(self):
        print("reign cannot be recycled it is technically hazardous waste...")

myDrink = reign("orange", "cylinder")
print(myDrink.ounces)
myDrink.recycle()
print(myDrink.ounces)

print("added one last line just ot test bud")





