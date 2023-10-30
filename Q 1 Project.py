# Ghost Game
from random import randint
print('ghost game')
feeling_brave = True
score = 0
ghost_door = randint (1, 3)
splits=''
print ('Three doors ahead...')
print('A ghost is behind one.')
print('Which door do you open?')
door = input ('1, 2 or 3?') 
door_num = int (door) 
if door_num == 1:
    ghoul = input('You feel a chill up your spine... Which path do you take? Middle, Left, Right?: ')
    if ghoul == 'Middle':
        print('Ghost has gotten you. GGs go next')
    elif ghoul == 'Left':
        print('Grandad has come back from the dead.')
    elif ghoul == 'Right':
        print('you pass on but have a werid feeling of being followed')
        splits == input('as you are runing down the hall you see a division in the hall' )
        print('left you ran into a ghoul with the face of your teacher')
        if splits == 'left': 
            print  ('left you ran into a ghoul with the face of your teacher')
            print('right you ran in to the school gym')


elif door_num == 2:
    
    zombie = input ( 'you hear a growl comeing fro  the bathroom' )
    print ('no zombie!')
    feeling_scard = True
    score = score + 1
    print ('Run away! you are about to be attacked by a group of zombies')
    print ('Game over! you scored', score)
    input ('1, 2 or 3?') 
    door_num - int (door) 


elif input ('1 then go to the next room'):
    print('Next Room is Haunted. GGs go next.')
elif door_num == 3:
    print ('werewolf!')
    feeling_brave = False
    werewofl = input('You feel a chill up your spine... Which path do you take? Middle, Left, Right?: ')
    if werewofl == 'Middle':
        print('Ghost has gotten you. GGs go next')
    elif werewofl == 'Left':
        print('Grandad has come back from the dead.')
    elif werewofl == 'Right':
        print('you pass on but have a werid feeling of being followed')
        if werewofl == input(  ):
           print('Blank')

else:
    print ('No monsters!')
    score = score + 1
print ('Run away!')
print ('Game over! you scored', score)
