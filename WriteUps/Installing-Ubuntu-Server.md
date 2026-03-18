INTRODUCTION
The ability computers must connect to networks and communicate with each other brings tons of possibilities on how managing and accessing a server through a host machine can be done. With this lab, creating a virtual machine with Ubuntu server, configuring virtual box to use a bridged adapter network interface, and creating a ssh server that can be logged into from a windows host machine will be done to demonstrate the capabilities of a ssh server and virtual machine in Cyber Security. Setting up a good password, enabling the right setting and knowledge of commands in bash and the external ip addresses ensures that a ssh server is setup and accessible through the virtual machine hosting it and is password protected for other hosts to acesss it.

BREAKPOINT 1

Here I downloaded the ubuntu server ISO and i have virtual box already installed and updated to the latest version on my computer. Downloading the ISO was an easy task and took only a few minutes for it to download to my Downloads folder.

BREAKPOINT 2

After I had the ISO in a folder and rebooted my computer, I proceeded to execute Virtual Box and set up the virtual machine. I have it named to something that I can distinguish from other Linux Virtual machines, and an appropriate amount of storage, processing power, memory, and video memory is configured to make sure I have a smooth experience. I was able to start the Ubuntu Server installer with no problems, and the installation process worked perfectly. I made sure a host name, username and password I can retype was entered in Ubuntu alongside having the box checked that says I will use Ubuntu Server to host a ssh server.

BREAKPOINT 3

The reboot process had no problems, after I pressed “reboot” the virtual machine restarted as if I restarted a physical machine and showed a screen asking for my username and password. After entering them I was able to use bash and successfully entered the “whoami” and “date” commands.

BREAKPOINT 4

Prior to pinging and testing the network connections on my virtual and host machine, I had to adjust a setting in Virtual Box so my Virtual network adapter can communicate with machine outside of the virtual network. Within the settings panel under Network, I changed the network adapter from NAT to bridged adapter. Within Windows, I right clicked on my network applet and was able to go into my network settings and allow my host machine to be discoverable to other devices. On Ubuntu server I used “ip addr” to get information on my internal and external ip addresses. My adapter on Ubuntu server is named “enp0s3” and my ip is 127.0.0.1. For Windows I used “ip config” and was able to find my ip through the output. Through the “ping” command, I was to successfully ping from my virtual machine to windows, and from my windows to my virtual machine.

BREAKPOINT 5

As mentioned before, during the installation process i clicked the box that said I will be using Ubuntu Server to setup a ssh server. For this step, I made sure that the ssh service wasn’t running by entering “sudo service  sshd status” which showed me that I had to configure and enable it. I entered “sudo ssh enable” and “sudo ufw allow ssh” to enable the ssh service and allow the network port meant for ssh to be open. Once port 22 was open and ssh was enabled, I decided to run ssh and use my username and ip to access it. After saying yes to the fingerprint prompt and setting my information, I was showed an output that showed information for my Ubuntu Server, proving that I can login and run commands to my virtual machine through cmd on my host machine.

CONCLUSION
This lab was easy going, and the whole process was familiar to me, and I have set a virtual machine with previous course work from earlier courses. I knew before entering commands and making sure I made any connections to the network, I read the Instructions, so I knew how to configure this correctly and have the right amount of safety measures before opening my virtual machine to the internet. The instructions were very helpful all the way through and I’m sure the ability to set up a ssh server will be of use in many projects and problems that require looking for vulnerabilities and penetration testing.


