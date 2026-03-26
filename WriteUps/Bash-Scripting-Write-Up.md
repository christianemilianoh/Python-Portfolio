# INTRODUCTION
For the terminal, lot of actions can be done and programs as well have a lot of parameters and options that can be stated. In order to do certain things, several programs and commands are needed. With a shell script and a text editor this can be done efficiently and in a clean manner. With incremental testing, comments for expressions and functions, and understanding of expression and functions of programs and commands A interactive script that can return IP addresses, date and time, open ports, and a Ceaser cipher all in one script can be done with proper design and organization measures. Using certain commands, a script such as the one mentioned can be created, executed, and written as a complete project.


## BREAKPOINT 1


<img width="621" height="298" alt="Picture1" src="https://github.com/user-attachments/assets/51c43674-01b9-4985-b638-fdcc39e6c182" /><br>
### Figure 1: Creating a folder and script in the terminal


Here are the commands I used to get to this point within the lab:
•	cd Documents, mkdir lab-06: this navigates the target directory to the Documents folder and creates a folder named “lab-06”
•	echo $RANDOM: generates a random number I used for my script name
•	touch hernandez-23625.sh: creates a shell script file using my last name, followed by a hyphen and the random number I generated using echo $RANDOM.
•	ls -l: list directories and files in the target directory and attributes such as permissions, file size and the modification timestamp.
•	chmod +x hernandez-23625.sh: Set the script permission to allow it to be executed.
•	sudo nano hernandez-23625.sh: opens the script in the CLI text editor nano as root.
•	./hernandez-23625.sh: executes the named script.
In this first part of the lab, using the command line I managed to make a folder for this lab within the Documents folder and a script in the nested “lab-06” folder. Using chmod and nano I was able to allow the script to be executed and was able to write code into it so executing it can result in a visible output. With scripts, the advantage of being able to execute several commands and arguments in a sequence without manually typing all of them in is present, as well as repetition of actions as well.


## BREAKPOINT 2


<img width="624" height="465" alt="Picture2" src="https://github.com/user-attachments/assets/660d20e3-0ca3-45cb-aa94-6601abd15a30" /><br>
### Figure 2: My script with the functions and echo statements established


<img width="624" height="152" alt="Picture3" src="https://github.com/user-attachments/assets/2cfe8ae9-7a85-4d41-945f-8bae2701a07a" /><br>
### Figure 3: Result of executing the script in the current state of it in Breakpoint 2


The creation of the outline and design of the script was made here. The script at this current state only includes comments for each function and variable I established, as “function name” () { states the function and “}” closes the variables off so only code written in between those two lines is a part of said function. I also have the lines that output text so when the script is executed the end user is present with text describing what data they will be viewing. Comments allow the code to be understood efficiently if shared with others or if it needs to be revisited or debugged without confusion of how the code is structured or how it operates.


## BREAKPOINT 3


<img width="624" height="532" alt="Picture4" src="https://github.com/user-attachments/assets/e7aec278-8312-4827-8346-394f30dfe34f" /><br>
### Figure 4: Added a functioning display of date and time to the script


<img width="624" height="212" alt="Picture5" src="https://github.com/user-attachments/assets/a1854194-ca5d-4348-a120-ffe918a32945" /><br>
### Figure 5: Executing the script with the date and time being able to be displayed


This update to the code now displays the date and time at the moment beneath the “Today’s Date:” and the “The current time:” lines in my script. I added two variables, tdate and current_time which have “date +” a set of variables that are formatted as “%” followed by a specific value that states if it’s an hour, minute, or day or month that needs to be displayed. I also modified the echo lines by adding “\n” and “$” followed by the variables stated before so on the output lines the date or time is on a separate line then the text describing if it’s the date or time that will be displayed. Two coding conventions I have followed here are indentation and function names. I kept my functions names all lowercase and no spaces or an underscore if the function is multiple words and made indentations for the code that follows the initialized function line.


## BREAKPOINT 4


<img width="624" height="596" alt="Picture6" src="https://github.com/user-attachments/assets/b50531c5-c764-48c1-9740-9b0917d11b8b" /><br>
### Figure 6: The addition of curl and nmap and other commands are added to the script so network and host information can be displayed


<img width="624" height="293" alt="Picture7" src="https://github.com/user-attachments/assets/a8969a4b-1d4c-40ab-94b9-4176b4389c02" /><br>
### Figure 7:Output of the script with the addition of programs that help display network connection and host machine information


Here I added quite a few additions to the ip_ports function, such as the use of two programs such as curl and nmap. Using ““program name” -h”, I was able to get a list of commands or a description of how these program function. Curl allows you to transfer data using several network protocols, and nmap scans networks and the host machine for information such as ports and connection info. 
•	hostname -I: displays the private IP address by reading the hostname of the machine
•	curl ifconfig.me: displays the public ip address by communicating with ifconfig.me which returns the public IP address
•	nmap scanme.nmap.org: Scans the site scanme.nmap.org which results in the host machines ports being scan so detailed such as open ports and closed ports can be disclosed.
•	echo -e “\n”: creates a separate output line that gets displayed.


## BREAKPOINT 5


<img width="624" height="548" alt="Picture8" src="https://github.com/user-attachments/assets/b348a0c5-025b-4b2a-854f-1bf66762f2c7" /><br>
### Figure 8: Example of the script with a functioning Caesar cipher encryption/decryption method


<img width="575" height="479" alt="Picture9" src="https://github.com/user-attachments/assets/80ad7836-89af-453e-985a-86c31cb8363b" /><br>
### Figure 9: 2nd example of the Ceaser cipher function


<img width="611" height="697" alt="Picture10" src="https://github.com/user-attachments/assets/c33e8b10-e178-4588-b0a8-a9a516fcb7c4" /><br>
### Figure 10: The script's code with the addition of the 3 letter Caesar cipher function


<img width="611" height="406" alt="Picture11" src="https://github.com/user-attachments/assets/a976067d-0550-4246-bb18-d13646b0129f" /><br>
### Figure 11: The script's code with the addition of the 5 letter Caesar cipher function


<img width="501" height="421" alt="Picture12" src="https://github.com/user-attachments/assets/fc004d25-8931-4f8e-934c-ab6ab9f0aec3" /><br>
### Figure 12: Output of the script with the 5 letter Caesar cipher implemented


Implementing the Caesar cipher function using the sample code in the instructions and adding comments to the code allowed for the correct implementation of the Caesar Cipher in this script. I noticed that “tr” the command that allows me to state a range of letters and state how characters in a sequence can be swapped. This result in a output of a prompt that allows the user to enter a string, and the string get encrypted with a 3 letter shift method, and decrypted using tr again but reverting the range and swapping of letters.
For the modified version of the script with the 5 character shift, I modified the two lines that use “tr” in order to make the 5 letter shift occur.
For encryption the line modified the expressions “a-zA-Z” and “f-za-eF-ZA-E” it changed to “a-zA-Z” and “d-za-cD-ZA-C”. The first letter of the second part I change from “f” to “d” which result in the range adjusting to a 5 character shift instead of a 3 characters shift. I applied this logic to the other letters in the expression, by just moving them a certain amount of times down the alphabet so the output is a 5 character shift and the range is adjust to it.
 I took the line “a-zA-Z” to “x-za-wX-ZA-W” and changed it to “a-zA-Z”  “v-za-vV-ZA-V”, resulting in the change occurring since I changed the first letter from “x” to “v” and the other letters to match with each letter in the alphabet being shifted by 5 letter instead of 3 for the decryption.

 
## CONCLUSION
I found that this lab was very informative and fun to work on. I did spend time understanding the Ceaser Cipher and being able to modify it correctly to correctly encrypt and decrypt a string by 5 characters. The skills of structuring and designing code and a script are quite useful for information technology and I will be practicing and utilizing these skills outside of my studies to make tasks easier to do on my personal computer and for projects that require me to utilize tools to transfer data or obtain information using programs such as curl or nmap.


## REFERENCES
“styleguide,” styleguide. Accessed: Nov. 19, 2024. [Online]. Available: https://google.github.io/styleguide/shellguide.html

“I Used The Linux/Unix tr Command To Defeat The Roman Empire - YouTube.” Accessed: Nov. 19, 2024. [Online]. Available: 
https://www.youtube.com/watch?v=A-QwLbRXwss
