'''
Challenge 05: Free-Falling Distance Calculator
Author: Christian Hernandez
Date:2/23/25
'''

#The formula for calculating distance.
def calculate(fall_time):
    dist = 0.5 * 9.8 * (fall_time ** 2)
    
#The result of the formula is returned so it can be called in other functions.
    return dist

#The UI shows a print statement asking for the number of seconds the object fell for.
def user_interface():    
    print("Welcome to the free-fall distance calculator!")
    enter = input("enter the period of time in seconds")
    
#converts the user input to a float variable.
    fall_time = float(enter)
    
#if a negative number is entered, the program tells the user to enter a valid number.
    if fall_time < 0:
        print("Please enter a valid number")
    
#This is the counter for the loop so the correct amount of distance values are printed for each second.
    i = 1
    
#The while loop takes the fall_time which run the print statement until the interger is the number the user put in.
    while i <= fall_time:   
        
#calls the calculate function and sets i as the number that will be calculated
        distance = calculate(i)
        
#prints the results of the formula to the user.
        print("The object's distance after falling for", i, "seconds is", distance,"meters")
        
#An increment of 1 is needed in order every second to be calculated.
        i += 1
    
#This is set to run the user_interface and other defined functions to assure the program doesn't have errors.
if __name__ == "__main__":
    user_interface()