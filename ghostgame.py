#ghost game :D

from random import randint
print ("ghost game")
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint (1, 3)
    print (" three doars ahed....")
    print (" a ghost behind one")
    print ("which doar do you open?")
    door = input ("1, 2, or 3?")
    door_num = int(door)
    if door_num == ghost_door:
        print ("GHOST")
        feeling_brave = False
    else:
        print("no ghost (phew)")
        print("you enter the next room!")
        score = score + 1
print ("run away!")
print("game over! you scored",score)

#how does this work?
