from dataclasses import dataclass

@dataclass          #Don't have to write representation methods or any of that
class Investor:
    name: str
    age: int
    cash: float
    favoriteSport: str

i1 = Investor("John", 80, 700, "Soccer")
i2 = Investor("Mike", 18, 2000, "Baseball")
i3 = Investor("John", 80, 700, "Basketball")

print(i1)
print(i1 == i2)
print(i1 == i3)