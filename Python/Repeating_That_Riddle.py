'''
Challenge 04
Author: Christian Hernandez
Date: 2/14/25
'''

#The counter for the amount of riddles correctly or incorrectly answered
count = 0
wrong = 0


#asks user if you they wish to play
intro = input("Would you like to play a game?")


#if the user answers yes the quiz starts
if intro.lower() == "yes":
#this while loop counts the amount of riddles answered correctly. count and wrong are reinstated so that the amount of riddles answer is reset every trial.
    while count < 5:
        count = 0
        wrong = 0
        #the answers to each riddle
        trial_1 = "Your left hand"
        trial_2 = "A towel"
        trial_3 = "A rubber band"
        trial_4 = "G"
        trial_5 = "When it is ajar"


        #The questions to each riddle in a constant input variable, with .lower implemented to assure responses in all lowercase are counted as correct
        pass_1 = input(("What can you hold in your right hand, but never in your left hand?").lower())
        pass_2 = input(("What gets wet while drying?").lower())
        pass_3 = input(("What kind of band never plays music?").lower())
        pass_4 = input(("What is the end of everything?").lower())
        pass_5 = input(("When is a door no longer a door?").lower())
            
            
        #the if-else statements that go through each question, and an increment is added to the correct or incorrect values
        if pass_1 == trial_1.lower():
        #an increment of 1 is added to the correct counter if the end user answers the riddle correctly
            count += 1
            print("Correct!")
        else:
        #an increment of 1 is added to the incorrect counter if the end user answers the riddle incorrectly
            print("Incorrect!")
            wrong += 1
            
        if pass_2 == trial_2.lower():
            print("Correct!")
            count += 1
        else:
            print("Incorrect!")
            wrong += 1
            
        if pass_3 == trial_3.lower():
            print("Correct!")
            count += 1
        else:
            print("Incorrect!")
            wrong += 1
            
        if pass_4 == trial_4.lower():
            print("Correct!")
            count += 1
        else:
            print("Incorrect!")
            wrong += 1
            
        if pass_5 == trial_5.lower():
            print("Correct!")
            count += 1
        else:
            print("Incorrect!")
            wrong += 1
        
        
        #if the user answered everything correctly they escaped the room and the program ends. Otherwise they are told the number of riddles answered incorrectly the quizno restarts.
        if count == 5:
            print("you were asked 5 riddles and you answered", count, "riddles correctly. Congratulations, you escaped the room of many riddles!")
            
        else:
            print("you were asked 5 riddles and you answered", count, "riddles correctly. Unfortunately, you did not escape the room of many riddles. Let's run that back!")
            
            
#if the user answers no, the program ends.
elif intro.lower() == "no":
    print("goodbye")