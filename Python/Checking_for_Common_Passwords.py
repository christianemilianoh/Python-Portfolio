"""
Christian Hernandez
Challenge 07: Checking for Common Passwords
3-9-25
"""

#StoredPasswords contains the common passwords tuple and using the index method checks if the user's password matches with a element in the tuple, returning if it is common or strong.
def StoredPasswords(checkPass):
    #The tuple contains 50 commons passwords indexed from 0 to 49.
    passwds = ("123456", "123456789", "12345", "qwerty", "password", "12345678", "111111",
               "123123", "1234567890", "1234567", "qwerty123", "000000", "1q2w3e",
               "aa12345678", "abc123", "password1", "1234", "qwertyuiop", "123321",
               "password123", "1q2w3e4r5t", "iloveyou", "654321", "666666", "987654321",
               "123", "123456a", "qwe123", "1q2w3e4r", "7777777", "1qaz2wsx", "123qwe",
               "zxcvbnm", "121212", "asdasd", "a123456", "555555", "dragon", "112233",
               "123123123", "monkey", "11111111", "qazwsx", "159753", "asdfghjkl",
               "222222", "1234qwer", "qwerty1", "123654", "123abc")


#This if-in statement checks if the user input matches with an element and returns a print statement stating the result.
    if checkPass in passwds:
        #The index variable uses the index method and checks if the input string matches with any element in passwds, and prints that it is too weak and the element that matched.
        index = passwds.index(checkPass)
        found = f"Your password is too common. Please consider changing it as it was found at index {index}"
        return found
    #if the input doesn't match with any element, a statement saying the password is strong is printed.
    else:
        return "You have a strong password."


#The getUserPass definitions asks the user to input a username and password, stores it in two variables and calls storePasswords and result to display if it is common or not. 
def getUserPass():
    userName = input("Enter a username:")
    password = input("Enter a password:")
    
    #This calls storedPasswords and returns the result.
    result = StoredPasswords(password)
    print(result)
    
    
#Calls getUserPass which leads to the program being fully functional as it calls from other definitions in order to check if the user's password is common or strong. 
if __name__ == '__main__':
    getUserPass()