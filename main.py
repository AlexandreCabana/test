from dataclasses import dataclass
from random import randint
@dataclass
class Personnage:
    name: str
    health: int
    max_result :int = 6
    result_dice:int = None
    def __str__(self):
        return f'{self.name} a {self.health} vie et a fait un {self.result_dice}. '
    @property
    def is_alive(self):
        return self.health > 0
    def shake_dice(self):
        self.result_dice = randint(0, self.max_result)
        0
class Player(Personnage):
    def __init__(self, name, health):
        super().__init__(name, health)
    def heal(self, damage: int):
        self.result_dice = None
        self.health += randint(0,5)-damage

def fight(player: Player, monster: Personnage):
    player.shake_dice()
    if player.result_dice < monster.result_dice:
        player.health -= monster.result_dice
    else:
        monster.health -= player.result_dice
def user_choice():
    choix = input('Voulez vous attaquer ou prendre une potion(heal/fight): ')
    if choix == 'heal' or choix == 'fight':
        return choix
    return user_choice()
def turn(player: Player, monster: Personnage):
    print(player)
    print(monster)
    monster.shake_dice()
    if user_choice() == 'heal':
        player.heal(damage=monster.result_dice)
    elif user_choice() == 'fight':
        print('Vous attaquez le monstre')
        fight(player, monster)
def main():
    player = Player('Alex',50)
    monster = Personnage('Karol', 50)
    while player.is_alive and monster.is_alive:
        turn(player, monster)
        if not player.is_alive: print('Vous avez perdu')
        elif not monster.is_alive: print('vous avez gagner')
if __name__ == '__main__':
    main()