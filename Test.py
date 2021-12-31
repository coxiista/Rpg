from Player import Player
from Battle import Battle

p1 = Player('Eric', 'spellcaster')
p2 = Player('Joao', 'warrior')

b = Battle(player_1=p1, player_2=p2)

while p1.p_hp > 0 and p2.p_hp > 0:
    b.player_2_atk_1()
    b.player_1_atk_2()
