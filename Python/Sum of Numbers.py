'''
Challenge 12: Sum of Numbers

Christian Hernandez

4-18-25
'''

#The intialization of the sum_recurse definition. The variable "n" is stated because it will be called recursively.
def sum_recurse(n):
    #This if statement (base case) assures if "n" == 1 to make sure in any case even if n == 1 the sum is correctly calculated through the return statement and the recursion within the else-return statement.
    if n == 1:
        return 1
    #The else statement calls n and the sum_recurse function, creating the stack value and calling sum_recurse recursively by substracting 1 from itself and returning each value.
    else:
        #n will be smaller than its initially called value, sum_recurse will have its value closer each time to "if n == 1" (base case).
        return n + sum_recurse(n-1)
    

#The main function statement which contains the input arguement variable and print statement for displaying the sum of all integers from 1 to n(user's arguement).
if __name__ == "__main__":
    #Input for the user to enter an integer arguement, and prints the sum to stdout.
    input = int(input("Enter a number:"))
    print(sum_recurse(input))