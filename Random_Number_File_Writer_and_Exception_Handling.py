'''
Challenge 06 - Random Number File Writer & Exception Handling
Name: Christian Hernandez
Date: 3-2-25
'''
#Imports the random number module needed to randomly generate intergers for the random number parameter.
import random


#The main definition for the prompt that asks the user to enter a interger, exeception handling and the for loop needed to write random intergers from 1-500 the correct number of times to a text file.
def main():
    #The exception handler which asks the user to enter a interger, if a interger isn't enter, a Value Error is detect and a prompt is printed so the user is returned to the initial prompt.
    while True:
        #The try statement is needed to prevent the user from entering a value that could break the program, and a user interface is present with a certain paramter that should be passed (intergers).
        try:
            user_input = int(input("Enter the number of random numbers this file will contain: "))
            break
        #This except statement makes sure the user knows they enter a non-interger and takes them back to the initial prompt.
        except ValueError:
            print("Please only enter an integer.")
            
#The directory path the file will be created and written to.
    file = r"/Users/User/Desktop/nameOfFile.txt"
    
    #This opens and closes the file in write mode so the number of random intergers that should be entered will be entered into the txt file.
    with open(file, "w") as file:
        
        #This for loop uses an underscore as a placeholder since num_pick handles the range and random selection module in one variable. The random intergers are picked and printed based on user input.
        for _ in range(user_input):
            #This randomly picks numbers from 1 to 500
            num_pick = random.randint(1, 500)
            #The file created on the desktop has a random number written into it, with "\n" placing each interger on a new line until those actions occurred as much as the interger entered.
            file.write(str(num_pick) + "\n")
            
#calls the main definition
if __name__ == "__main__":
    main()