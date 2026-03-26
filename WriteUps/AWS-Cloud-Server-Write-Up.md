# INTRODUCTION
Enterprises, and many people who work with cloud computing must use a service that hosts the interface to use remote machines and services from the client’s device. This lab provides insight into Amazon web services, and the security and configuration measures needed to set up a basic server using AWS. Included within AWS is MFA, policy configuration for IAM groups and users, and encryption keys necessary to login into the server using a method such as SSH. These procedures will allow me to set up a basic environment to configuration and access to use it for future labs that will require it.

# BREAKPOINT 1


<img width="624" height="504" alt="Picture1" src="https://github.com/user-attachments/assets/e23f24b9-8dc4-43f9-9c02-2bf58ea2a212" />
<br/>
### Figure 1: The AWS sign up page.


<img width="624" height="485" alt="Picture2" src="https://github.com/user-attachments/assets/a081fb04-1ed3-4719-a1ee-b3cc58591a26" />
<br/>
### Figure 2: The confirmation page for creating a AWS account. To initialize the first procedure of the lab, I opened the link to register for an AWS account provided in the instructions. After entering my email, and other information such as my number, my credit card number for verification, and the root username and password for the account I was able to access a dashboard. The dashboard was the Management Console, which I found quite seamless to sign up and navigate to. 


# BREAKPOINT 2


<img width="624" height="192" alt="Picture3" src="https://github.com/user-attachments/assets/712a42ed-0234-48a9-8923-b956fa6b559a" />
### Figure 3: IAM Dashboard with a alert to set up MFA.

<img width="624" height="296" alt="Picture4" src="https://github.com/user-attachments/assets/da93008b-550e-4348-baac-09ba48f3e017" />
### Figure 4: Enabling Free Tier alerts for the root email. I found that on the dashboard I was alerted to complete MFA authentication using the Duo Mobile App. After scanning the QR code and entering the 2 PIN numbers I had it set up. The last measure I took was to look at the left panel on the website and click billing preferences. Through here I enabled Free Tier alerts to assure usage of the plan is not wasted. This step is important in assuring I have good security measures for accessing something vulnerable and powerful such as the root user for the IAM console dashboard. Within this step I have MFA setup, and alerts setup to make sure I received those alerts.


# BREAKPOINT 3


<img width="624" height="263" alt="Picture5" src="https://github.com/user-attachments/assets/16da1b06-653b-4e7c-a3d7-a7a608f4273d" />
### Figure 5: The initial set up screen for creating a User/Group.


<img width="624" height="193" alt="Picture6" src="https://github.com/user-attachments/assets/5b340098-4109-49c0-b2c1-e9f6d3d8b885" />
### Figure 6: The create group details window.


<img width="624" height="216" alt="Picture7" src="https://github.com/user-attachments/assets/092378f0-895b-47e3-b66a-97527a9e5e0e" />
### Figure 7: The window for filling out primary information for our non-root user.


<img width="624" height="165" alt="Picture8" src="https://github.com/user-attachments/assets/f3aae3e6-ad23-4bf4-881f-ce82e5467267" />
### Figure 8: Setting the Amazon EC2 details for the policy needed for our instance.


<img width="624" height="220" alt="Picture9" src="https://github.com/user-attachments/assets/cd07f5df-292f-458b-9d88-f2c140eb9b42" />
### Figure 9: The configuration window details for our EC2-Instance.


<img width="624" height="148" alt="Picture10" src="https://github.com/user-attachments/assets/f330ea46-bfde-4a34-b0e1-4523b6138c8b" />
### Figure 10: Applying the EC2-Instance permission set.


<img width="624" height="517" alt="Picture11" src="https://github.com/user-attachments/assets/46cfcfe0-9aff-4ea2-a635-cc4528c7689d" />
### Figure 11: The Dashboard after adding the EC2-Instance.


<img width="624" height="373" alt="Picture12" src="https://github.com/user-attachments/assets/75acee8a-ad70-474c-bb74-689ee084e525" />
### Figure 12: The EC2 page to where we initially will launch the Ubuntu Instance. To securely assure I can set up our AWS server, I created a group and user within the console to assure this can be done. Through the IAM Identity Center, I was able to create a user and group. Through the prompts, I filled out information such as the user’s name and set up MFA for the user as well. I did obtain a confirmation email to continue accessing AWS with my new user who I named john. Initially there’s wasn’t any content on the dashboard for john, so I had to setup permissions that gave the user access to one. I went through the group creation process like how a user was made and assigned john to Group_1. After, it was time to make a policy and have it assigned to john’s group. I pressed the create policies button, and within the selection panels I set the permission type to custom and searched for the “AmazonEC2FullAccess” set. I set the runtime for the server to be for 4 hours and confirmed the creation of the EC2 Instance. Finally, I assigned the EC2-Instance permission set to Group_1, through the permission sets windows on the IAM Identity Center console.


# BREAKPOINT 4


<img width="624" height="389" alt="Picture13" src="https://github.com/user-attachments/assets/98a0ba2f-982e-49cd-b401-6b36c488ef88" />
### Figure 13: Setting the EC2 instance to run Ubuntu Server 22.04 LTS.


<img width="624" height="595" alt="Picture14" src="https://github.com/user-attachments/assets/ad8d2f03-436c-4492-9e19-94a512799666" />
### Figure 14: Setting the key pair type as RSA in the .pem format.


<img width="624" height="298" alt="Picture15" src="https://github.com/user-attachments/assets/bacd6071-b343-4d08-b572-20ae604b1551" />
### Figure 15: Assuring that our instance can allow SSH traffic from our Windows machine.


<img width="624" height="238" alt="Picture16" src="https://github.com/user-attachments/assets/f4973398-9e04-44bf-a4c1-ef371643ffc9" />
### Figure 16: Configuring the storage allocation settings for our instance.


<img width="624" height="188" alt="Picture17" src="https://github.com/user-attachments/assets/6d543199-1495-4686-9a1b-4a364a536d29" />
### Figure 17: The page confirms the installation and setup of our instance. After setting up my EC2-Instance, I navigated to the Services menu on the dashboard and clicked the “launch an instance” button. These next few steps require certain specifications to have our instance properly function correctly. I configured my server instance to run Ubuntu 22.04 LTS image, a key pair with the RSA encryption type and the .pem format. For the lab, allowing SSH traffic to the server is allowed, and allocating 25gb of storage is essential as well for our instance. After reviewing and pressing “launch instance”, I am now able to begin to setup logging in to the server via SSH. 


# BREAKPOINT 5

<img width="624" height="272" alt="Picture18" src="https://github.com/user-attachments/assets/bcd50bc3-0397-4b76-adaf-84d54303a1d7" />
### Figure 18: The PuTTY program's download page.


<img width="602" height="471" alt="Picture19" src="https://github.com/user-attachments/assets/58d297b2-e847-44de-a59f-a1e506d9ce43" />
### Figure 19: PuTTY key generator program which we will convert our original EC2 key to a private key we can use to login to the instance via SSH.


<img width="624" height="326" alt="Picture20" src="https://github.com/user-attachments/assets/2d31c6fb-0154-4d11-ba1b-79b119187da9" />
### Figure 20: Successful login of our instance through SSH.


<img width="624" height="310" alt="Picture21" src="https://github.com/user-attachments/assets/98acc10a-2c81-4471-98f6-8e57ae434897" />
### Figure 21: A demonstration confirming basic Linux commands work on our instance and exiting providing us the IP address to our instance.


<img width="624" height="152" alt="Picture22" src="https://github.com/user-attachments/assets/427b2a43-ff3e-4df1-9ee4-4e4012b331fa" />
### Figure 22: Confirmation that I have terminated the instance I have created with my AWS account. When attempting to connect to the server with the .pem I created in the instance server process, I received an error due to the key not being converted from it’s original private .pem format. The instructions I followed were from the AWS documentation for Amazon EC2. To do this I downloaded and installed PuTTYgen, a program that will convert the key to a new file format that I can use to login to the SSH server. I loaded the private .pem file, and set the encryption key to stay as RSA. I saved it as a new key file so I know I can login with the newly generated key. On Windows I used the command line to login, using “ssh -I ASDASF.pek [the name of my .pem file] ubuntu@ip”. I successfully logged in, tested a few basic Linux commands to make sure I can correctly write commands and get output as seen in figure 21. My final command was “exit” which output the line “Connection to [IP] closed”, which is the private ip address for the machine/instance. Finally to close things off, I terminate the instance to prevent wasted usage of data through the EC2 dashboard.


# CONCLUSION
This lab was my first experience with Amazon Web services, so I learned quite a bit about the fundamentals of using the server and modules such as the EC2 console and the configuration of IAM groups and users. I did look at other options aside from the free plan to see what other services Amazon can provide to people who use AWS. Amazon also provided other documentation regarding the setup for connecting your instance through SSH and the generated key. Overall, I did not find the lab very challenging, but it was still a new endeavor I am content to have completed. I can see within a lab or a position where I must secure a server that uses AWS, I must assure that access to it is secure using MFA, and permissions are correctly set using group and user policies as well.

### REFERENCES
“How to Setup Your Development Environment for AWS | Module 2,” Amazon Web Services, Inc. Available: https://aws.amazon.com/getting-started/guides/setup-environment/module-two/. [Accessed: Apr. 14, 2025]

“Connect to your Linux instance using PuTTY - Amazon Elastic Compute Cloud.” Available: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-from-windows.html. [Accessed: Apr. 14, 2025]
