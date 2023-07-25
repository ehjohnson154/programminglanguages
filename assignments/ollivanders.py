import random as r

class Wand:
    def __init__(self, length, wood, core):
        self.length = length,
        self.wood = wood
        self.core = core
        self.person = 'Nobody'

    def set_owner(self, person):
        self.person = person

    def __str__(self):
        return 'This wand is {} inches long, made of {}, with a core of {}.  {} owns this wand.'\
            .format(self.length, self.wood, self.core, self.person)

woods = ['oak', 'elder', 'cherry']
wands = []

def main():
    cores = ['phoenix feather', 'dragon heartstring', 'unicorn hair']
    wizards = [...]
    for wizard in wizards:
        wand = Wand(length=r.randrange(6,13), wood=r.choice(woods), core=r.choice(cores))
        wand.set_owner(person=wizard)
        wands.append(wand)

# ‘woods‘
# ‘wands‘
# ‘wizards‘
# ‘wand‘
# ‘wizard‘
# ‘self.person‘

    print("hello!")
    print(type(woods))
    print(type(wands))
    print(type(wizards))
    print(type(wand))   
    print(type(wizard))
    print(type(wand.person))

if __name__ == '__main__':
    main()