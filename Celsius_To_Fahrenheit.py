"Asks user to input a numerical value in Celsius, set as a float value in order to correctly converter non-intergers to the correct number"
prompt = float(input("Can you please enter a temperature in Celsius?"))

"This variable takes the float created by the user input and converts it to Farenheit"
conv = (9 / 5 * prompt + 32)
 
"Displays the results of converting the temperature from Celsius to Farenheit"
print(prompt , "°C", "is", conv ,  "°F")