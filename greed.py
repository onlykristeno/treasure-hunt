#Same game played in AP Stats
# Mulyiplayer Game, a dice will be rolled (variable), and the number or 
#VALUE, from that roll will be added to the players score
# UNTILLL a 6 is rolled
# Player can chose when to sit down 
#(boolean variable that says when true, stop adding to their score or smthn)
#1st player to get to MAX wins

#INGREDIENTS: var dice = randInt(1, 6)
# var boolean roll = True //Turn to FALSE when player wants to sit down
# var score1 = cumulative score from dice for player 1
# var score2 = cumulative score from dice for player 2
# loop through until both rolls=False or one player is at 50 points

#STEP 1 RANDOM NUMBER
import random

def rollDice():
    dice = random.randint(1, 6)
    return dice

totalscore1 = 0
totalscore2 = 0

score1 = 0
score2 = 0

name1 = "Player 1"
name2 = "Player 2"

print("poo")

sit1 = False
sit2 = False

letter = 1

def game(letter, sit1, sit2, name1, name2, score1, score2, totalscore1, totalscore2):
    while (letter<= 6):
        while (sit1==False & sit2 == False):
            dice = rollDice()
            if(dice == 6):
                totalscore1 += score1
                totalscore2 += score2

                print("You lost! Moving onto next round!")
                letter += 1
                score1 = 0
                score2 = 0
                break
            else:
                score1 += dice
                score2 += dice

            #Now, if the dice is 6 we need to set the score=0  and exit the loop


            #Here, we ASK the player, "hey u wanna sit now?"
            response1 = input("Hey " + name1 + "! You wanna sit now? (T/F) ")
            response2 = input("Hey " + name2 + "! You wanna sit now? (T/F) ")
            
            #Now, if we change their sitting or standing based off their response
            if(response1 == "T"):
                sit1 = True
            else:
                sit1 = False

            if(response2 == "T"):
                sit2 = True
            else:
                sit2 = False
            
            #Adding their total score up if they didn't sit down or get a 6
            totalscore1 += score1
            totalscore2 += score2
    
    return score1 + score2

game()
