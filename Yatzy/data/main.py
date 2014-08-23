# -*- coding UTF-8 -*-

import random
import time
from player import *
from test_functions import *

while True: 
    change = [False] * 5
    
    
    playercount = int(raw_input("How many players? > "))

    players = []
    player_points = []
    for r in range(0, playercount):
        players.append(Player(raw_input("What is your name? > ")))
    currentplayer = 0
    
    # Game loop
    while True:
        if len(players[currentplayer].checklist) == 0:
            player_points.append(sum(players[currentplayer].points.values()))
            break
        
        dies = [random.randint(1, 6),
                random.randint(1, 6),
                random.randint(1, 6),
                random.randint(1, 6),
                random.randint(1, 6)]
        
        # Decide dice to keep
        for i in range(0, 2):
            print("\nNow playing: %s\n" % players[currentplayer].name)
            print (", ".join(players[currentplayer].checklist))
            print "\n1: %s  \n2: %s  \n3: %s  \n4: %s  \n5: %s\n" % tuple(dies)
    
            for r in range(0, 5):
                while True:
                    input = raw_input("Keep die %d? y/n > " % (r+1))
                    if input.lower().startswith('y'):
                        change[r] = False
                        break
                    elif  input.lower().startswith('n'):
                        change[r] = True
                        break
                    else:
                        print "\nThe option is not valid.\n"
    
            cast_die(change)
    
        print "\n1: %s  \n2: %s  \n3: %s  \n4: %s  \n5: %s\n" % tuple(dies)
        
        #Decide where to put the points
        while True:
            print "\nOptions left to choose from: "
            print(" \n".join(players[currentplayer].checklist))
            choice = raw_input(" > ").lower()
            
            #Calculate the points
            block1 = ["1","2","3","4","5","6"]
            if choice in players[currentplayer].checklist:
                players[currentplayer].checklist.remove(choice)
                if choice in block1:
                    players[currentplayer].points[choice] = test_block1(dies,choice)
                else:
                    players[currentplayer].points[choice] = test_block2(dies,choice)
                break
            else:
                print "The choice that you have entered is not correct."
            
        currentplayer += 1
    
        if currentplayer > playercount-1:
            currentplayer = 0
    
        print("\n\n Next player!")
    
    #Don't remove code below
    
    #print "The most points gathered is %s." % max(player_points)
    #print "That player is..."
    #time.sleep(1)
    #print "%s!" % players.index(max(player_points)).name
    
    maxpoints = 0
    for pl in players:
        print("\n%s: %d points.\n" % (pl.name, pl.get_score_total()))
    
    answer = raw_input("Do you want to play again? > ")
    if answer.lower().startswith('n'):
        print "\n\nThank you for playing."
        time.sleep(3)
        break
    else:
        continue
    