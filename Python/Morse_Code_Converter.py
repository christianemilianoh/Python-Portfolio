'''
Challenge 08: Morse Code Converter

Christian Hernandez

3-23-25
'''
#morse_conv defentition handles the storing, counting, appending and reinstatements of converting the string characters sent by the user to the morse code strings.
def morse_conv(text):
    
    #The actual index of characters that can be converted to morse code.
    morse_dict = {
        ' ': ' ',
        ',': '--..--',
        '.': '.-.-.-',
        '?': '..--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'
    }

    #This is used to store the input for conversion of the string characters to the morse code list of elements.
    morse_result = []
    
    #i is set to 0 in order to have a functioning counter for specifically going through the input.
    i = 0
    
    #This while loop goes through every character, and uses i (0) as the first element in the input. The upper converts the characters to upper case.
    while i < len(text):
        char = text[i].upper()
        
        #The if statement is to see if the character from the user's input is in the dictionary, and if the character from the string gets appended to morse_result for conversion.
        if char in morse_dict:
            morse_result.append(morse_dict[char])
            
        #Else statement is used to pass any invalid characters that don't appear in the morse code dictionary.
        else:
            pass
        
        #This increment helps with the progression of the counter which moves the index.
        i = i + 1

    #The empty string is used to store the morse code characters.
    morse_string = ""
    
    #counter for making sure the loops and increments start at the first element (0) properly.
    x = 0
    
    # The while loop goes through each Morse code character using len and x which is set to 0, or the first element in the index.
    while x < len(morse_result):
        
        # Appends the morse code equivalent to the regular string character. 
        morse_string = morse_string + morse_result[x]
        
        #This if statement makes sure that if the user input contains multiple words with spaces that the space is counted in the index and is converted correctly.
        if x < len(morse_result) - 1:
            morse_string = morse_string + " "
        #The increment for the counter assures that all characters are converted.
        x = x + 1

    return morse_string  


#The morse_ui definition gets user input, and calls the morse_cov function with the user input being the variable. The result is then printed.
def morse_ui():
    user_input = input("Enter a string: ")
    result = morse_conv(user_input)
    print("Morse code:", result)
    
# This calls the morse code converter user interface function.
if __name__ == "__main__":
    morse_ui()