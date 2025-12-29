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

totalscore1 = []
totalscore2 = []

score1 = 0
score2 = 0

#Ask their names
name1 = input("Player 1, whats your name? ")
name2 = input("Player 2, whats your name? ")

#print("poo")

sit1 = False
sit2 = False

letter = 1
stick = False

#If theres a 6 at the start of a round, then that roll is terminated 
# and we roll again until we start with a number thats not 6

def game(letter, sit1, sit2, name1, name2, score1, score2, totalscore1, totalscore2):
    while (letter<= 6):
        while (sit1==False or sit2 == False):
            rollCount = 1
            dice = rollDice()
            if(dice<6):
                print("This roll is a " + str(dice))
                #Record how many rolls in this round
                rollCount += 1
            elif(rollCount == 1 and dice==6):
                #Should restart the inner loop
                print(".....Started on 6, restarting round.....")
                continue
            else:
                rollCount += 1
                print("☠️❌ This roll is a " + str(dice) + "❌☠️")

            #Act depending on dice roll (Player 1)
            if(dice == 6 and sit1 == False):
                print(name1 +" lost their points!")

                score1 = 0
                
                print(name1 + " has " + str(score1) + " points")
            
            elif(dice==6 and sit1==True):
                print(name1 + " has " + str(score1) + " points")

            elif(sit1==False):
                score1 += dice #they get points!
                print(name1 + " has " + str(score1) + " points")
            
            elif(sit1==True):
                print(name1 + " has " + str(score1) + " points")


            #Act depending on dice roll (Player 2)
            if(dice == 6 and sit2 == False):
                print(name2 +" lost their points!")

                score2 = 0
                
                print(name2 + " has " + str(score2) + " points")
            
            elif(dice==6 and sit2==True):
                print(name2 + " has " + str(score2) + " points")

            elif(sit2==False):
                score2 += dice #they get points!
                print(name2 + " has " + str(score2) + " points")
            
            elif(sit2==True):
                print(name2 + " has " + str(score2) + " points")

            #Moving onto next round if roll is 6
            if(dice==6):
                letter += 1
                print(" ")
                print("🔄 Moving onto round " + str(letter) + "/6 ! 🔄")
                #Make everyone stand up again!
                sit1 = False
                sit2 = False
                break
            #Moving onto next round if both players sit down
            elif(sit1==True and sit2==True):
                letter += 1
                print("Moving onto round " + str(letter) + "/6 !")
                #Make everyone stand up again!
                sit1 = False
                sit2 = False
                break
                

            #Here, we ASK the player, "hey u wanna sit now? But only ask this if they're standing for the round"
            if(sit1==False):
                response1 = input("Hey " + name1 + "! You wanna sit now? (T/F) ")
            if(sit2==False):
                response2 = input("Hey " + name2 + "! You wanna sit now? (T/F) ")
            
            #Now, if we change their sitting or standing based off their response
            if(response1 == "T" or response1=="t"):
                sit1 = True
            else:
                sit1 = False

            if(response2 == "T" or response2=="t"):
                sit2 = True
            else:
                sit2 = False

        print("🜲 Game over! 🜲") 
        totalscore1.append(score1)
        totalscore2.append(score2)
            
    superscore1 = sum(totalscore1)
    superscore2 = sum(totalscore2)

    return [superscore1, superscore2]

game(letter, sit1, sit2, name1, name2, score1, score2, totalscore1, totalscore2)

