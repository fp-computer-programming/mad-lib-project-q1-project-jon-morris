# Ghost Game
from random import randint
print('ghost game')
feeling_brave = True
score = 0
ghost_door = randint (1, 3)
splits=''
vampire=''
go=''
trip=''
fake=''
fakedoor=''
leave=''
end=''






print ('Three doors ahead...')
print('A ghost is behind one.')
print('Which door do you open?')
door = input ('1, 2 or 3?') 
door_num = int (door) 
if door_num == 1:
    ghoul = input('You feel a chill up your spine... Which path do you take? Middle, Left, Right?: ')
    if ghoul == 'Middle':
        print('Ghoul has chased you down')
    elif ghoul == 'Left':
        print('Grandad has come back from the dead.')
    elif ghoul == 'Right':
        print('you pass on but have a werid feeling of being followed')
        splits == input('as you are runing down the hall you see a division in the hall' )
        print('left you ran into a ghoul with the face of your teacher')
        if splits == 'left': 
            print  ('left you ran into a ghoul with the face of your teacher')
        elif splits == 'right':   
            print('right you ran in to the school gym')
        go == input('as you are runing down the hall you see the exit' )
        print('left you ran into a wall')
        if go == 'left': 
            print  ('left you ran into a door and its stuck')
        elif go == 'right':
            print('right you ran into a door and you are free now')   
            leave == input('runing down the hall you to the exit' )
        print('left you ran into a wall')
        if leave == 'left': 
            print  ('left you ran into a door and its stuck')
        elif leave == 'right':
            print('right you ran into a door and you are free now')   
    else:
        print('the ghoul gets you')
        






elif door_num == 2:

    
    vampire = input('you hear a loud flapping noise coming from the up stiars attic: ')
    if vampire == 'Middle':
        print('vampire has gotten you. GGs go next')
    elif vampire == 'Left':
        print('vampire has biitten you.but ok') 
    elif vampire == 'Right':
        print('you pass on but have a werid feeling of being followed')
        splits == input('as you are runing down the hall you see a division in the hall' )
        print('left you ran into a ghoul with the face of your teacher')
        if splits == 'left': 
            print  ('left you ran into a vampire were there is no where else to run')
        elif splits == 'right':
            print('right you ran in to the school closet')
        trip == input('as you are runing down the hall you see the exit' )
        print('left you ran into a wall')
        if trip == 'left': 
            print  ('left you ran into a door and its stuck and niow you are trapped ')
        elif trip == 'right':
            print('right you ran into a door and the vampire gets closer')
        elif trip == 'middle':
            print ('middle you ran a 4.2 and you ran straight through the door')
        end == input('as you are runing down the hall you see the exit' )
        print('left you ran into a wall')
        if end == 'left': 
            print  ('left you ran into a door and its stuck and niow you are trapped ')
        elif end == 'right':
            print('right you ran into a door and the vampire gets closer')
        elif end == 'middle':
            print ('middle you ran a 4.2 and you ran straight through the door')





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
        if werewofl == input( 'as you are runing you hear haer the sound of claws following you' ):
           splits == 'left'
         
           print('Blank? you run into an all white room ')
           splits == 'right'
           print ( 'you see the werewolf eating a deer')
        fakedoor == input('as you are runing down the hall you see the exit' )
        print('left you ran into a wall')
        if fakedoor == 'left': 
            print  ('left you ran into a door and its stuck')
        elif  fakedoor == 'right':
           
            print('right you ran into a door and you are free???')
            print('fake door so close but yet so far')
            fake == input('as you are runing down the hall you see the exit' )
        print('left you ran into a wall')
        if fake == 'left': 

            print  ('left you ran into a door and its stuck and niow you are trapped ')
        elif fake == 'right':

            print('right you ran into a door and the vampire gets closer')
        elif fake == 'middle':

            print ('middle you ran a 4.2 and you ran straight through the door')



else:
    print ('No monsters!')
    
    score = score + 1
print ('Run away!')
print ('Game over! you scored', score)




zombie = input ( 'you hear a growl comeing fro  the bathroom' )
print ('no zombie!')
feeling_scard = True
score = score + 1
print ('Run away! you are about to be attacked by a group of zombies')
print ('Game over! you scored', score)
input ('1, 2 or 3?') 
door_num - int (door) 