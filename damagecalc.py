class Player():
    def __init__(self, name, health, attack, armor, mr):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        self.mr = mr

    def __str__(self):
        res = self.name
        res+= "\nhealth: " + str(self.health)
        res+= "\nAttack: " + str(self.attack)
        res+= "\nArmor: " + str(self.armor)
        return res

    def level_up(self):
        self.health += 50
        self.attack += 5

    def take_damage(self, opponent_attack):
        damage_multiplier = 100/(100+self.armor)
        real_damage = damage_multiplier * opponent_attack 
        self.health -= real_damage

p1 = Player("Grabben", 200, 50, 0)
p2 = Player("Grabbtvå", 150, 60, 100)

print(p1.name, "attackerar", p2.name)
p2.take_damage(p1.attack)
print(p2.name, "har", p2.health, "hp kvar")
p1.level_up()
