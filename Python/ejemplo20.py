# ahora haremos el famoso juego piedra papel o tijera en python
# a comparacion de c++, debe ser mas "faacil"

import random

choises=["piedra","papel","tijera"];
computer=random.choice(choises); #la computadora elige un elemento de la lista

player=None

while player not in choises:
    player=input("piedra papel o tijera?: ").lower();

if computer==player:
    print("computer: ",computer);
    print("Player: ",player);
    print("Empate");
elif player=="piedra":
    if computer=="papel":
        print("player: ",player)
        print("computer: ",computer)
        print("computer win!!");
    if computer=="tijera":
        print("player: ",player)
        print("computer: ",computer)
        print("player win!!");

elif player=="papel":
    if computer=="piedra":
        print("player: ",player)
        print("computer: ",computer)
        print("player win!!");
    if computer=="tijera":
        print("player: ",player)
        print("computer: ",computer)
        print("computer win!!");
else:
    if computer=="piedra":
        print("player: ",player)
        print("computer: ",computer)
        print("computer win!!");
    if computer=="papel":
        print("player: ",player)
        print("computer: ",computer)
        print("player win!!");

