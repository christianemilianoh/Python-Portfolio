'''
Challenge 01

Christian Hernandez

1/25/2025


1.

2048 = 100000000000
2048/2 = 1024 = remainder of 0
1024/2 = 512 = remainder of 0
512/2 = 256 = remainder of 0
256/2 = 128 = remainder of 0
128/2 = 64 = remainder of 0
64/2 = 32 = remainder of 0
32/2 = 16 = remainder of 0
16/2 = 8 = remainder of 0
8/2 = 4 = remainder of 0
4/2 = 2 = remainder of 0
2/2 = 1 = remainder of 0
½ < 1 ~ 0 = remainder of 1


To convert decimal 2048 to binary form, I divided the value 2048 continuously until the
number was less than 1 or 0. I then took the dividend for each result which is all the values
for 2048 in binary form. The very last value that was less than 1 is the first value from left to
right in binary form since the numbers in binary values from right to left have the base value
increase by 2. The result is 100000000000.


2.

11001010 = 202
2+8+64+128 = 202
How I converted 11001010 into decimal was I count the 1s and 0s from the right side to the
left side, with the 0 on the right side being converted to a decimal value of 1. Each value
that follows is the preceding value multiplied by 2. To convert the whole binary to the
decimal value, I found the sum of only the 1s in the binary number and converted it to
decimal. 202 is the decimal value.


3.
In an IDE, Interactive Mode allows you execute code line by line in the interpreter. Script
Mode stores the code you right into a file, and will execute the whole file first, then the
output is then shown.
'''

print("Hello, my name is Christian Hernandez. My major is Cyber Security. I am a Junior. I have programming experience with the following language(s): Python, and some Java.")