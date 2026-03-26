# INTRODUCTION
For operating systems such as Linux, the file system infrastructure must be protected with the proper configurations, and verification that attributes were set to prevent as much vulnerabilities as possible. Within this lab I use Linux utilities such as the creation of groups, reading and view attributes of directories in the operating system such as the bin and etc folder. The inodes, the read, write, and execute permissions using ACL, and tested these configurations by logging into the ssh user as different non root users and navigating and executing scripts within and outside of home user directories will be done. The results of this lab teaches the aspects of having a protected operating system with specific permission for files, and directories so a attacker couldn’t use objects such as files with vulnerable file permissions or directories that aren’t secured due to a lack of restrictions on copies of files in vulnerable directories with common permission with the original file that could be in a personal user’s directory.

# BREAKPOINT 1


<img width="624" height="313" alt="Picture1" src="https://github.com/user-attachments/assets/e02c428f-d466-42d5-80a5-f82fb1d41bfa" /><br>
## Figure 1: Creating a hard link so "ls" points to /bin/ls on Ubuntu Server.


<img width="624" height="309" alt="Picture2" src="https://github.com/user-attachments/assets/825b3b73-0afb-4b33-af25-9797ba98c307" /><br>
## Figure 2: Removing the ls hard link.
Within this lab, several commands and expressions were used in order to manage and create files and configurations within the Ubuntu Server. With these first few commands, I took the ls utility and created a link to it to a copy of it in the /tmp directory. The expressions such as “-l” allowed me to see aspects of the ls utility such as the inode number that they both shared since they’re both hard linked. For the files in /tmp, it’s the temporary directory so having the sticky bit a security measure as copies of those files can contain important information in scenarios to where the computer is using those files. The stick bit prevents someone from deleting or modifying the files, so if an attacker were to view the inode numbers and other information of two files they could use it to write anything to the copy of the file in /tmp with the stick bit.
Next, I used the rm commands to remove the hard link. I had to use sudo privileges when working with directories not within my home directory. I finally used the stat command to view the files in the ls utility which showed aspects such as time and permissions of the files.

# BREAKPOINT 2 

<img width="624" height="322" alt="Picture3" src="https://github.com/user-attachments/assets/4965ba9e-d297-4e19-a9cc-794f8c45f74b" /><br>
## Figure 3: Adding users and setting their passwords on Ubuntu Server.

<img width="624" height="88" alt="Picture4" src="https://github.com/user-attachments/assets/7346ff25-fd4a-4805-9c82-3016c05d890b" /><br>
## Figure 4: Checking the pwquality package has been installed to Ubuntu Server.

<img width="624" height="382" alt="Picture5" src="https://github.com/user-attachments/assets/865b2bef-fa26-42ba-ac22-98ca14d8efed" /><br>
## Figure 5: Configuring the PAM password configuration to be more secure using nano on Ubuntu Server.

<img width="624" height="533" alt="Picture6" src="https://github.com/user-attachments/assets/7723eeaf-d7c4-47d4-b419-eb7ffb4dce12" /><br>
## Figure 6: Testing the password protection and attempts for the user lovelace on Ubuntu Server, and creating a script at the root of the home directory.

<img width="624" height="571" alt="Picture7" src="https://github.com/user-attachments/assets/8f6c75ea-4e0d-404a-95aa-8a7c11c52573" /><br>
## Figure 7: Proof of the creation and login of the user lovelace on Ubuntu Server.

<img width="624" height="550" alt="Picture8" src="https://github.com/user-attachments/assets/f302a068-734d-4796-8792-a9e82177a830" /><br>
## Figure 8: Proving the creation and login of the user turing on Ubuntu Server.
The creation of two new users within this labs was a process of creating and configuring security measures for the password system within the Ubuntu Server environment.  Next I modified the PAM configuration file and added a few expressions that secured the login system. For example “retry=3” would give the user an error after 3 incorrect attempts, “minlen=8, maxrepeat=3, “[u,l,d, or o]credit” and reject_username ” make the password creation process for challenging when it comes to setting a acceptable password. The password has to be at least 8 characters, 3 characters can be repeat at maximum, and the password must have at least a digit, a upper and lower-case character and a special character. I tested the new configuration by resetting the server and trying to change the password as lovelace, to which it asked for a new password. I entered passwords that didn’t meet the requirements, and I was prevented from attempting to change the password after 3 incorrect attempts.
In order to test file permissions between users, I created a bash script named ada.sh, which prints a message when executed. Using chmod 4475, I made it accessible to be executed by users, but when I copied it to the home directory folder, the permissions can be view with “ls -l”. The file seems to run on my own user environment just fine, the other two non-root users can execute it as well. With this file not only in my home directory and the home folder, this is a vulnerability due to the fact that any user has not only executable but write permissions because the setUID attribute in a sense override other attributes. To avoid this setting permissions for all users as a group will result in prevented access to the file and only letting trusted users access just the file or path of what they can view is integral to security.


# BREAKPOINT 3

<img width="624" height="424" alt="Picture9" src="https://github.com/user-attachments/assets/ba800c10-71d5-4b6d-a2d7-73108a6ae342" /><br>
## Figure 9: All three terminals displaying that the ssh server has 3 created users.

<img width="624" height="153" alt="Picture10" src="https://github.com/user-attachments/assets/e1f6464b-7c4c-49fb-bf0b-9f0a9f30cc92" /><br>
## Figure 10: Creation of the directory "boring-stuff" within the lovelace home directory.

<img width="624" height="178" alt="Picture11" src="https://github.com/user-attachments/assets/f22a30bf-fc5e-4b5b-9cc0-568caa85e299" /><br>
## Figure 11: Creating the group coders and verifying the ID numbers using grep and cat.

<img width="522" height="103" alt="Picture12" src="https://github.com/user-attachments/assets/cbe511c8-0256-4502-b86e-a665b1d4db90" /><br>
## Figure 12: Editing the file permissions of ada.sh..

<img width="624" height="259" alt="Picture13" src="https://github.com/user-attachments/assets/3a974744-e3a3-4322-a1d4-8382d94e6d6c" /><br>
## Figure 13: Attempting to execute the ada.sh script as the user turing on Ubuntu Server.
Strengthening and testing the security of my system calls for the creation of directories and files that I can modify the attributes of in order to verify that my system isn’t vulnerable because of user permissions possibly having vulnerability. A directory named “boring-stuff” was created within the lovelace user directory, and the contents of ada.sh were copied to a file named secret.sh within the boring-stuff directory. In order to properly have each user configured, using usermod, the coders group was created. The expressions “-aG” append the following expressions to the group that’s specified, which is coders. 
Next I took the ada.sh script and copied it from the home directory to the boring-stuff directory. With it having same file permissions as the original “ada.sh” script, I had to modify the permissions of the file so only a root user can access it. This was done by using chmod and using 700, I was able to give the owner of the file permissions (7) and the 0’s result in the absence of permissions for other users. To test this change, I logged in as turning and tried to execute the script, which resulted in a permission denied error. This setup of permissions and attributes globally and per user demonstrate the use of Access Control Lists (ACLS), since I based created a group to bundle all user in, but set specific attributes for specific files for certain users and not entire directories yet. This result in specific permissions that limit the actions of certain users, which is the least privilege principle (NSCS, n.d.).

Sources:
“Secure design principles.” Available: https://www.ncsc.gov.uk/collection/cyber-security-design-principles. [Accessed: Mar. 18, 2025]

# BREAKPOINT 4

<img width="472" height="339" alt="Picture14" src="https://github.com/user-attachments/assets/a687d261-1583-4cac-bb86-afa23d97d17b" /><br>
## Figure 14: Using acl utilties such getfacl and setfacl to change permissions of ada.sh.


<img width="426" height="206" alt="Picture15" src="https://github.com/user-attachments/assets/53de9c49-b517-406f-a902-575b8ea9e646" /><br>
## Figure 15: Creation of a super-secret directory with a alan.sh file that's has special permissions which lovelace cannot execute the script due to this.

<img width="397" height="473" alt="Picture16" src="https://github.com/user-attachments/assets/5f8a2a64-ddcb-4787-baba-12268e9f9077" /><br>
## Figure 16: Using setfacl to modify the permission of alan.sh for the user turning, and attempting to make sure turning cannot access the secret.sh script.

<img width="624" height="83" alt="Picture17" src="https://github.com/user-attachments/assets/5cea6542-734b-493b-84bc-318c1a9c4a69" /><br>
## Figure 17: Preventing the user turing from accessing the secret.sh script.
Further expanding the process of configuring attributes within the Linux system, I used ACL in order to view the logs and modify the permission of what user can specifically do.  I checked the permission of the ada.sh file and the permission of lovelace who owns the file, and viewed how these attributes are structured not only for permissions from the user but for individual files as well. I noticed using getfacl shows fields such as user, group and other, which shows me the owner of the object, and if the have to ability to read, write or execute the file in that sequence and if permissions are possibly overridden by group or global user attributes. The creation of a new directory and bash file named “secret” within a super-secret directory is necessary for testing the modifications made with ACL. By using turning, whom didn’t create any scripts or directories, I restricted the executable and write permission for that user so while the alan.sh file is accessible, the secret.sh file is not despite them sharing a nested directory. The getfacl command and using “u:<user>” and attributes such as –x or r—allowed me to make adjust to those two scripts only for the turning user.


## CONCLUSION
The configuration of the different users and attributes within the Ubuntu Server environment was an experience I found initially familiar but eventually quite challenging due to errors I was receiving from trying to set attributes for specific directories such as the super-secret folder and the parent directory boring stuff for the turning user. It seemed like attempting to use setfacl as with my own username and lovelace result in failed attempts to specifically get turing to properly be unable to view the alan.sh script while trying to get the secret.sh file readable and executable. I see how these configurations are integral to creating a secure infrastructure for file systems that run on L	inux. This lab was very challenging for me, but a very important learning experience.

## REFERENCES

NCSC, “Secure design principles.” Available: https://www.ncsc.gov.uk/collection/cyber-security-design-principles. [Accessed: Mar. 18, 2025]
