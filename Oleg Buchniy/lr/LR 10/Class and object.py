class Gladiator:
 
    def __init__(self, name, Heals,Damage,Armor,Teritory,Skin):
        self.name = name    
        self.age = 1        # штучно доданий атрибут, лєвий
        self.Heals=Heals
        self.Damage=Damage
        self.Armor=Armor
        self.Teritory=Teritory
        self.Skin=Skin
    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")
 
 
tom = Gladiator("Tom")
tom.Skin="-_-"
tom.Teritory= "-----------------"+"\n|               |"+f"\n|      {tom.Skin}       |"+"\n|               |"
tom.display_info()      # Name: Tom  Age: 37
 
bob = Gladiator("Bob")
bob.Skin="+_="
bob.display_info()      # Name: Bob  Age: 41