# GUI-based version of RPSLS
# This is a possible solution for exercise n6 RPSLS of An Introduction to Interactive Programming in Python at coursera
###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Insert your solution for RPSLS here
def ganapc():
    print 'Computer wins'
def empate():
    print 'Its a tie'
def playerwins():
    print 'Player wins'
def computing(guess):
    print 'Player chose ' + guess
    computer=random.randrange(0,5)
    if computer==0:
        print 'Computer chose rock'
    elif computer==1:
        print 'Computer chose paper'
    elif computer==2:
        print 'Computer chose scissor'
    elif computer==3:
        print 'Computer chose lizard'
    elif computer==4:
        print 'Computer chose spock'
            
    if guess =="rock":
        if computer ==2 or computer ==3:
            playerwins()
        elif computer==0: empate()
        else : ganapc()
    elif guess=="paper":
        if computer ==0 or computer ==4:
            playerwins()
        elif computer==1: empate()
        else : ganapc()
    elif guess=="scissor":
        if computer ==1 or computer ==3:
            playerwins()
        elif computer==2: empate()
        else : ganapc()
    elif guess=="lizard":
        if computer ==1 or computer ==4:
            playerwins()
        elif computer==3: empate()
        else : ganapc()
    elif guess=="Spock":
        if computer ==0 or computer ==2:
            playerwins()
        elif computer==4: empate()
        else : ganapc()
     
    
# handler for input field
def get_guess(guess):
    
    # validate input
    if not (guess == "rock" or guess == "Spock" or guess == "paper" or
            guess == "lizard" or guess == "scissors"):
        print
        print 'Error: Bad input "' + guess + '" to rpsls\n'
        return
    else:
        computing(guess)
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
