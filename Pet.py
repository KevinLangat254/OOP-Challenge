class Pet:
    def __init__(self,name,hunger,energy,happiness):
        self.name=name
        self.hunger=max(0, min(hunger, 10))
        self.happiness=max(0, min(energy, 10))
        self.energy=max(0, min(happiness, 10)) 
        self.Tricks=list()
    def eat(self):
        self.hunger=max(0,self.hunger-1)   
        self.happiness=min(10,self.happiness+1)
        print(self.name+" is eating....")
        return self.hunger,self.happiness
    def sleep(self):
        self.energy=min(10,self.energy+5)
        print(self.name+" is sleeping") 
        return self.energy    
    def play(self):
        self.energy=max(0,self.energy-2)
        self.happiness=min(10,self.happiness+2)
        self.hunger=min(10,self.hunger+1)
        print(self.name+" is playing")
        return self.energy,self.happiness,self.hunger  
    def get_status(self):
        return f"{self.name}'s status;\nPet's name:{self.name}\nHunger level:{self.hunger}\nEnergy level:{self.energy}\nHappiness level:{self.happiness}" 
    def train(self,trick):
        self.Tricks.append(trick)
    def show_tricks(self):
        return self.Tricks    

Dog=Pet("Rex",6,6,5)
#Dog.eat()
Dog.play()
# Dog.sleep()
print(Dog.get_status())
# Dog.train("sit")
# Dog.train("Roll over")
# print(Dog.show_tricks())

