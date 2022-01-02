class Investor:

    def __init__(self, name: str, age: int, cash: float):
        self.name = name
        self.age = age
        self.cash = cash
    
    def __repr__(self):
        return f"Name: {self.name}"
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __lt__(self, other):
        return self.cash < other.cash

i1 = Investor("John", 25, 9000)
i2 = Investor("Anna", 30, 12000)
i3 = Investor("Bob", 70, 800000)

i4 = Investor("John", 5, 100)

print(i1)       #This is able to display i1 name because we created a representation in line 8 that let us 
print(i1==i4)   #This lets us see that we have two investors that are the same because they have the same name shown in line 11
                #otherwise it will say that they are different people
print(i1 < i4)  #Compare cash

# All of does comparisions and statements are able because we programmed it manually, one by one and it will be time consuming
# to get it running at a 100%

    
