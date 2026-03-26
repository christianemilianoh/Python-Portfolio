# INTRODUCTION
A honeypot is a system setup to log information of connections made by users to a specific server, meant for the purpose of getting trace information that can identify visitors who interact with the connection. Through this lab using the Internet Storm Center from the SANS Institute, and commands in the AWS EC2 Ubuntu instance a honeypot will be created and analyzed. Practically, by installing DShield to our instance makes the server dedicated to logging connections made from my Windows machine, and DShield will forward information such as IP address, and port numbers to a web portal I can access with a SANS ICS.

# BREAKPOINT 1
<img width="528" height="127" alt="Picture1" src="https://github.com/user-attachments/assets/b838f864-0d10-4099-bbaf-092de925b484" /><br/>


## Figure 1: IP address information for my machine using ipconfig on command prompt.

<img width="624" height="253" alt="Picture2" src="https://github.com/user-attachments/assets/9bbc8437-382b-41aa-a259-4864e64cb494" /><br/>

## Figure 2: my public facing address using nslookup and 2 sites to return them.

<img width="1430" height="632" alt="Picture3" src="https://github.com/user-attachments/assets/06933ee4-d4ae-4252-bcac-b2e4c24eef72" /><br/>

## Figure 3: Screenshot confirming the successful registration of a SANS ISC account.
My initial actions involved me signing up for an Internet Storm Center (ISC Account) on the SANS Institute website. After entering my email and setting a password a confirmation email was sent which provided a link to validate my account. Next, I took a lot at the command line on my Windows machine to do two things. First I used ipconfig, and located the information that pertains to the wifi adapter my machine has that connects to the network. In figure 1 I have my public and private facing ip addresses as shown. I also confirmed this with the nslookup configuration and used opendns to get my addresses to return to me. I conducted some research and view a YouTube video from the SAN ISC’s YouTube Channel. From it, I learned that logging that has been done in the backend uses machines like Raspberry Pis for their Dshield system.

“SANS TechTuesday Part 11: Introduction to the Internet Storm Center – SANS ISC.” Available: https://www.youtube.com/watch?v=0HiwtzshMXE. [Accessed: Apr. 19, 2025]

# BREAKPOINT 2

<img width="624" height="545" alt="Picture4" src="https://github.com/user-attachments/assets/c68702b2-a005-4098-9e26-c075c57397ca" /><br/>

## Figure 4: The menu on the AWS console to launch an Ubuntu Server Instance for this lab.

<img width="624" height="44" alt="Picture5" src="https://github.com/user-attachments/assets/aa7ed765-30d3-47d8-9d9d-93305e18f184" /><br/>

## Figure 5: Confirmation of the Instance being availible on my AWS EC2 console.

<img width="623" height="309" alt="Picture6" src="https://github.com/user-attachments/assets/947ddb58-9145-4ea0-b3aa-be0600a957c4" /><br/>

## Figure 6: Signing in to the ubuntu server through the key pair and private address on the command line.
Like the last lab, I went on ahead and created an instance through the EC2 Dashboard on the AWS Console. I logged in using Duo Mobile for MFA and went to the EC2 Dashboard under “Services”. I made a new instance, using the same configuration as last time, running Ubuntu 22.04 and using the same key pair. I launched the instance and then logged in using the “ssh pi name.pem ubuntu@private ip” command on the Windows command line. From there I was able to access my EC2 Ubuntu instance perfectly.

# BREAKPOINT 3

<img width="624" height="307" alt="Picture7" src="https://github.com/user-attachments/assets/14cecbbf-4536-44ae-9d29-43d4a6e5e85e" /><br/>

## Figure 7: Updating and rebooting Ubuntu.

<img width="624" height="307" alt="Picture8" src="https://github.com/user-attachments/assets/81583695-b9b7-464f-9022-f2f11a014a0b" /><br/>

## Figure 8: Installing Python and having the needed dependencies.

<img width="623" height="310" alt="Picture9" src="https://github.com/user-attachments/assets/6f36c659-689f-4a7c-a893-390bb8250c0a" /><br/>

## Figure 9: Installing pip to the Python environment.

<img width="624" height="188" alt="Picture10" src="https://github.com/user-attachments/assets/0a2d7e27-40fd-4207-9e9c-3f839b4e0da2" /><br/>

## Figure 10: Rebooting the instance from the EC2 console.

<img width="624" height="310" alt="Picture11" src="https://github.com/user-attachments/assets/b1813dd7-11c9-44e3-9371-ac2bfc7fd4e3" /><br/>

## Figure 11: First window in the dshield GUI installer.

<img width="620" height="300" alt="Picture12" src="https://github.com/user-attachments/assets/cfa45789-d2dd-4933-813c-9c95b97025f3" /><br/>

## Figure 12: The Dshield GUI window with my SANS ISC email and API key.

<img width="624" height="308" alt="Picture13" src="https://github.com/user-attachments/assets/ac4de560-e881-4e3e-aed8-d2fadde3dad9" /><br/>

## Figure 13: The GUI confirming the name of the network interface my instance uses.

<img width="622" height="307" alt="Picture14" src="https://github.com/user-attachments/assets/7a9b30df-db32-41b2-bc81-001ef33c563c" /><br/>

## Figure 14: A instance of Dshield displaying the IP address for the EC2 Instance.

<img width="624" height="307" alt="Picture15" src="https://github.com/user-attachments/assets/64d0dca9-86a1-486a-860f-2e4008fda256" /><br/>

## Figure 15: The SSL Certificate page on the Dshield Installer.


<img width="624" height="308" alt="Picture16" src="https://github.com/user-attachments/assets/f5a429e9-afb9-4a9f-ac05-71f2a751c45f" /><br/>

## Figure 16: Final output of the Dshield installer and status.sh script.
From here, I installed the honeypot software using a couple of commands and navigating through the installer for DShield. Following the Lab instructions provided, I navigated to the home directory, and installed python 3, 2.7, and git. Next using curl I obtained an installer script for pip and displayed the output of pip to assure the file was downloaded correctly. I then ran the file with python2.7 to make sure it was functioning correctly, then rebooted the server from the EC2 console. Once rebooted, I created a directory named “installed” and navigated to it using mkdir and cd. To install DShield I cloned the git release from the github linked in the instructions, then navigated and ran the DShield Install script using cd and sudo. Once the installer was running, a GUI appeared informing me about the changes that can occur when making this machine dedicated to DShield. I accepted them and began to go through the prompts which asked me to configure several pieces of information. Entering my SANS ISC email and API Key, confirming the network interface name, local network IP and ports that I will use for the honeypot, and the SSH certificate for the DShield instance I configure in this install. After the installation was completed, I ran the status.sh script, and it resulted in most of the checks being good, except a few errors that will require troubleshooting on the next step.


# BREAKPOINT 4

<img width="624" height="114" alt="Picture17" src="https://github.com/user-attachments/assets/435933be-8b00-420a-a1de-97fe8a0755b2" /><br/>

## Figure 17: Getting to the security group rules page on the console.

<img width="624" height="77" alt="Picture18" src="https://github.com/user-attachments/assets/66ea5035-6d4a-4a4c-89c7-1a392b7ae593" /><br/>

## Figure 18: The security group for the EC2 instance.

<img width="624" height="236" alt="Picture19" src="https://github.com/user-attachments/assets/b3df4f45-fcad-411b-9e0b-cf4ea5e92e49" /><br/>

## Figure 19: The inbound rules configured to allow all traffic for the EC2 instance with Dshield installed.
After the DShield installation, my Instance now needs the proper security configuration to receive all kinds of traffic in order for the honey pot to receive inbounds connections and make outbounds connections so we can view a log containing information about connections made to the DShield Instance. To do this I went back to the EC2 Instance Dashboard and clicked on the Instance I am running. Next on the Security Tab, I was able to view the security groups associate with the instance. From there, I looked at the rules list and configured the Inbound rules to allow different connections from IPv4 and IPv6 traffic within a range wide enough to support port 12222, which is what I used for DShield. After saving these rules to match the ones in the instructions, I then tried to make a connection to the server through the command line so my logs will have information appear on the DShield center. The DShield center was accessible with the SAN ISC account I made in the first breakpoint.

# BREAKPOINT 5

<img width="624" height="200" alt="Picture20" src="https://github.com/user-attachments/assets/c9991ad0-8f86-436a-b923-94a145d96e4e" /><br/>

## Figure 20: The ISC account page showing Logs from the Dshield instance.

<img width="1430" height="618" alt="Picture21" src="https://github.com/user-attachments/assets/3612510e-81cf-48ec-b6b6-36ca80eb6f88" /><br/>

## Figure 21: Viewing Dshield logs.

<img width="624" height="237" alt="Picture22" src="https://github.com/user-attachments/assets/29d1f57b-96bf-4f75-8b6a-695b27db13eb" /><br/>

## Figure 22: Showing my DShield instance log using Color My Logs.
With activity to the DShield instance being made, I decided to go to the DShield page on the SANS ISC and viewed the Firewall logs. I unfortunately could only get one item to appear after waiting for other attempts to appear but was able to view information such as the date, time, IP address, source port, the target connection and the port made with this inbound connection. I placed it into the Color my Logs page as well, and saw that it highlighted the host machine’s IP, and the network connection that was made from attempting to login into the DShield instance. From this one item I can tell this was from the Windows Machine due to the appearance of Microsoft appearing in the report and the IP Address listed.

“Color My Logs,” SANS Internet Storm Center. Available: https://isc.sans.edu/colormylogs.html. [Accessed: Apr. 19, 2025]

# CONCLUSION
This lab was an excellent continuation of expanding on the skills learned from the previous lab with setting up a server instance on AWS and connecting to it. I ran into some trouble after installing DShield to my instance however, I was able to get a report to appear on the Dshield portal. The fix was done by waiting a bit after I installed DShield and configured my inbound connection to match the ones from breakpoint 4. From there I was able to view items on the DShield portal, but only one instance appeared, and I couldn’t get any others to appear. With what I was able to do here I understood the purpose of setting up software to adjust a server to work as a honeypot and it’s practical use in enterprises. If I were to do a blue teaming project or work for an organization that required me to obtain information that can be traced back to individuals of interest, setting  up a honeypot like in the lab I complete and making it appear more authentic to what a individual of interest would be looking for would be a important concept into meeting goals for certain projects.

# REFERENCES
“Amazon Web Services”, Amazon. Available: https://us-east-1.console.aws.amazon.com/console/home. [Accessed: Apr. 19, 2025]

“Register,” SANS Internet Storm Center. Available: https://isc.sans.edu/register.html. [Accessed: Apr. 19, 2025]

“SANS TechTuesday Part 11: Introduction to the Internet Storm Center – SANS ISC.” Available: https://www.youtube.com/watch?v=0HiwtzshMXE. [Accessed: Apr. 19, 2025]

“Color My Logs,” SANS Internet Storm Center. Available: https://isc.sans.edu/colormylogs.html. [Accessed: Apr. 19, 2025]
