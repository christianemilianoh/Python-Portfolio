# INTRODUCTION
A honeypot is a system setup to log information of connections made by users to a specific server, meant for the purpose of getting trace information that can identify visitors who interact with the connection. Through this lab using the Internet Storm Center from the SANS Institute, and commands in the AWS EC2 Ubuntu instance a honeypot will be created and analyzed. Practically, by installing DShield to our instance makes the server dedicated to logging connections made from my Windows machine, and DShield will forward information such as IP address, and port numbers to a web portal I can access with a SANS ICS.

# BREAKPOINT 1
 
## Figure 1: IP address information for my machine using ipconfig on command prompt.
 
## Figure 2: my public facing address using nslookup and 2 sites to return them.
 
## Figure 3: Screenshot confirming the successful registration of a SANS ISC account.
My initial actions involved me signing up for an Internet Storm Center (ISC Account) on the SANS Institute website. After entering my email and setting a password a confirmation email was sent which provided a link to validate my account. Next, I took a lot at the command line on my Windows machine to do two things. First I used ipconfig, and located the information that pertains to the wifi adapter my machine has that connects to the network. In figure 1 I have my public and private facing ip addresses as shown. I also confirmed this with the nslookup configuration and used opendns to get my addresses to return to me. I conducted some research and view a YouTube video from the SAN ISC’s YouTube Channel. From it, I learned that logging that has been done in the backend uses machines like Raspberry Pis for their Dshield system.

“SANS TechTuesday Part 11: Introduction to the Internet Storm Center – SANS ISC.” Available: https://www.youtube.com/watch?v=0HiwtzshMXE. [Accessed: Apr. 19, 2025]

# BREAKPOINT 2
 
## Figure 4: The menu on the AWS console to launch an Ubuntu Server Instance for this lab.
 
## Figure 5: Confirmation of the Instance being availible on my AWS EC2 console.
 
## Figure 6: Signing in to the ubuntu server through the key pair and private address on the command line.
Like the last lab, I went on ahead and created an instance through the EC2 Dashboard on the AWS Console. I logged in using Duo Mobile for MFA and went to the EC2 Dashboard under “Services”. I made a new instance, using the same configuration as last time, running Ubuntu 22.04 and using the same key pair. I launched the instance and then logged in using the “ssh pi name.pem ubuntu@private ip” command on the Windows command line. From there I was able to access my EC2 Ubuntu instance perfectly.

# BREAKPOINT 3
 
## Figure 7: Updating and rebooting Ubuntu.
 
## Figure 8: Installing Python and having the needed dependencies.
 
## Figure 9: Installing pip to the Python environment.
 
## Figure 10: Rebooting the instance from the EC2 console.
 
## Figure 11: First window in the dshield GUI installer.
 
## Figure 12: The Dshield GUI window with my SANS ISC email and API key.
 
## Figure 13: The GUI confirming the name of the network interface my instance uses.
 
## Figure 14: A instance of Dshield displaying the IP address for the EC2 Instance.
 
## Figure 15: The SSL Certificate page on the Dshield Installer.
 
## Figure 16: Final output of the Dshield installer and status.sh script.
From here, I installed the honeypot software using a couple of commands and navigating through the installer for DShield. Following the Lab instructions provided, I navigated to the home directory, and installed python 3, 2.7, and git. Next using curl I obtained an installer script for pip and displayed the output of pip to assure the file was downloaded correctly. I then ran the file with python2.7 to make sure it was functioning correctly, then rebooted the server from the EC2 console. Once rebooted, I created a directory named “installed” and navigated to it using mkdir and cd. To install DShield I cloned the git release from the github linked in the instructions, then navigated and ran the DShield Install script using cd and sudo. Once the installer was running, a GUI appeared informing me about the changes that can occur when making this machine dedicated to DShield. I accepted them and began to go through the prompts which asked me to configure several pieces of information. Entering my SANS ISC email and API Key, confirming the network interface name, local network IP and ports that I will use for the honeypot, and the SSH certificate for the DShield instance I configure in this install. After the installation was completed, I ran the status.sh script, and it resulted in most of the checks being good, except a few errors that will require troubleshooting on the next step.


# BREAKPOINT 4
 
## Figure 17: Getting to the security group rules page on the console.
 
## Figure 18: The security group for the EC2 instance.
 
## Figure 19: The inbound rules configured to allow all traffic for the EC2 instance with Dshield installed.
After the DShield installation, my Instance now needs the proper security configuration to receive all kinds of traffic in order for the honey pot to receive inbounds connections and make outbounds connections so we can view a log containing information about connections made to the DShield Instance. To do this I went back to the EC2 Instance Dashboard and clicked on the Instance I am running. Next on the Security Tab, I was able to view the security groups associate with the instance. From there, I looked at the rules list and configured the Inbound rules to allow different connections from IPv4 and IPv6 traffic within a range wide enough to support port 12222, which is what I used for DShield. After saving these rules to match the ones in the instructions, I then tried to make a connection to the server through the command line so my logs will have information appear on the DShield center. The DShield center was accessible with the SAN ISC account I made in the first breakpoint.

# BREAKPOINT 5
 
## Figure 20: The ISC account page showing Logs from the Dshield instance.
 
## Figure 21: Viewing Dshield logs.
 
## Figure 22: Showing my DShield instance log using Color My Logs.
With activity to the DShield instance being made, I decided to go to the DShield page on the SANS ISC and viewed the Firewall logs. I unfortunately could only get one item to appear after waiting for other attempts to appear but was able to view information such as the date, time, IP address, source port, the target connection and the port made with this inbound connection. I placed it into the Color my Logs page as well, and saw that it highlighted the host machine’s IP, and the network connection that was made from attempting to login into the DShield instance. From this one item I can tell this was from the Windows Machine due to the appearance of Microsoft appearing in the report and the IP Address listed.

“Color My Logs,” SANS Internet Storm Center. Available: https://isc.sans.edu/colormylogs.html. [Accessed: Apr. 19, 2025]

# CONCLUSION
This lab was an excellent continuation of expanding on the skills learned from the previous lab with setting up a server instance on AWS and connecting to it. I ran into some trouble after installing DShield to my instance however, I was able to get a report to appear on the Dshield portal. The fix was done by waiting a bit after I installed DShield and configured my inbound connection to match the ones from breakpoint 4. From there I was able to view items on the DShield portal, but only one instance appeared, and I couldn’t get any others to appear. With what I was able to do here I understood the purpose of setting up software to adjust a server to work as a honeypot and it’s practical use in enterprises. If I were to do a blue teaming project or work for an organization that required me to obtain information that can be traced back to individuals of interest, setting  up a honeypot like in the lab I complete and making it appear more authentic to what a individual of interest would be looking for would be a important concept into meeting goals for certain projects.

# REFERENCES
“Amazon Web Services”, Amazon. Available: https://us-east-1.console.aws.amazon.com/console/home. [Accessed: Apr. 19, 2025]

“Register,” SANS Internet Storm Center. Available: https://isc.sans.edu/register.html. [Accessed: Apr. 19, 2025]

“SANS TechTuesday Part 11: Introduction to the Internet Storm Center – SANS ISC.” Available: https://www.youtube.com/watch?v=0HiwtzshMXE. [Accessed: Apr. 19, 2025]

“Color My Logs,” SANS Internet Storm Center. Available: https://isc.sans.edu/colormylogs.html. [Accessed: Apr. 19, 2025]COLLABORATION
