Network traffic is a very active and broad aspect of computing systems and various methods that are used in order to communicate with each other. To analyze various parts of network traffic within a network, many tools have been developed in order to provide this ability to view in real-time network traffic. In this lab I will be looking into Wireshark, and several protocols that are used when analyzing my host machine connected to host servers and how interactions made with my web browser and the command line on Windows. The first initial step I took was to download Wireshark from the official website and executed the program so I could start a capture. After I started a capture, I opened my web browser and began to utilize to generate enough traffic for Wireshark to display enough packets to analyze. After pausing the traffic for the first initial testing, I noticed that I saw an abundance of packets that are utilizing TCP and UDP (Figure 4 and 6). To properly generate more traffic, I navigated to the university’s site to sign into the single sign on portal. This resulted in Wireshark displaying packets using the ARP protocol (Figure 1) and the DNS request from my host machine to the servers I accessed by viewing the university’s single sign on page (Figure 2).

After entering in my credentials and signing in, I checked back to Wireshark for other protocols that were in previous packets such as HTTP, and HTTPS which is assuring that a process is being made to verify that I am accessing a secure website with proper certifications (Figure 5). As I continued to access other online services that are currently accessible, I viewed other details in the packet details pane such as the protocol types, and the source and destination IP addresses, which do alternate when viewing UDP and TCP packets during this traffic capture. For further inspection I proceeded to use my email service and various other sites provided by the university to generate traffic. I noticed that I had enough traffic to view that a consistent number of packets were using the ICMP protocol, and by viewing more details I observed that during this time my host machine was actively connected to my router that underneath the length field, I observed that this type of protocol is responding from the router to the host machine in order to function as a proper way to check if communication from my machine to the router is continuously in operation (Figure 7).

A notable protocol I wanted to generate traffic for and inspect is FTP, to which by having my machine connected to a website or on standby could not suffice properly wanting to viewing details of what occurs when using FTP through a utility such as the command line on Windows. To start this process, I searched for a available way to access a FTP server which led to sftp.net, a website that provides credentials and information for these services available for demonstration and testing (see resources). I opened the command line and proceeded to access the ftp server with the ftp command, and an address from the list of ftp servers. Once I entered that command, I was faced with a prompt to enter credentials. After doing so, I proceeded to view my filter the packet list to view exclusively the FTP packets (Figure 8). This was done by clicking the filter tab and choosing to filter wireshark to just display the FTP packets. From what I can observe that contains the exact data I entered, and the responses given back from the FTP server. The port numbers I am accessing the FTP server on is also viewFTP well as other information as the enabling of text encoding and successful passage of text within the session I had accessing the FTP server through the command line.

Overall viewing these protocols are entailing of the amount not only transferring but verification and communication between my machine and router and the servers I access results in being able to view an abundance of data. I decided to start a new capture and left my machine idle for an hour in order to view an amount of network traffic that can be overviewed within Wireshark. After this was completed, I proceeded to view the network traffic statistics through the Statistics tab, and the Capture File Properties button I accessed the overview and was able to see packets statistics (Figure 9). A few notable aspects of the capture file properties is the time subsection, which contains timestamps for the instant the first packet was capture, and the last packet was captured. A notable part of this instance of capturing network traffic was the number of packets that was captured, and the lack of dropped packets that were captured. The Statistics tab contains valuable information such as the time span of the packets, and the average amount of bytes and bits transported during these sessions. These statistics are pretty useful in that overall, many actions such as accessing a site or leaving a computer running an operating system such as Windows will always still generate traffic that is generating pings and receiving responses that can be recorded and inspected.

To observe a difference with more long-term analyzation of network traffic, I tested a four-hour Wireshark session to view if there is anything notable from the one-hour session and the four-hour session, I proceeded to wait for network traffic to be collected. During this extended amount of time, I viewed that certain packets were only being generated, commonly ones using ICMP and they were being generated at a much slower rate during the later hours of this scan. After four hours elapsed, the same procedure was done to pull the network statistics from Wireshark (Figure 10). A noticeable difference from this capture from the one-hour one is now it is apparent that dropped packets are visible within the captured session. The rate of bytes that were being transferred during this session was much larger than the one-hour session as on average 18k bytes were transferred during this networking session. Other fields in the Statistics section are notably larger as although there is constant traffic that was collected, the amount of time that elapsed resulted in a significantly larger opportunity for network activity and results such as dropped packets to be apparent after long term monitoring using Wireshark.

The final procedure for this lab was to verify that the network interface I choose is matching with the main network interface found accessible through ipconfig on the command line. I found a few packets that utilize ARP, which helps identify that the network interface is communicating to a destination point correctly. I filtered Wireshark to view the ARP packets and noticed that a certain IP address and MAC address is listed in a few of them (Figure 11). I verified that the network interface chosen matched the IP and MAC address listed in the ARP packet’s information field. By using ipconfig, I was able to find my WiFi router, with the matching IP address and MAC address associated with my device.

Wireshark’s capabilities here provided an opportunity to have an insight to standard internet protocol activity, but more can be done in order to utilize the full capabilities of Wireshark when it can be used in conjunction with other utilities to properly test a networking for troubleshooting issues or testing how a network is transferring data during certain events that could be trigged or inspected with other programs. In a role as a someone who would need to configure a proper setup not only for analyzation, but detection would be using another tool to detect network activity that Wireshark can provide details for in order to have tangible reports. When a router is operating and many devices are sending network traffic, an Intrusion detection system such as SNORT provides alerts and establishes that network activity that can seem suspect can be logged and viewed through the SNORT utility, and for Wireshark to specifically display details and an overview of specific aspects of network traffic such as TCP errors can be detected and analyze in a tangible forum (Jain G., 2021). In an scenario such as a researcher or if troubleshooting if a server would need to be configured to prevent issues such as network traffic errors or suspicious network activity that could be recorded in real time due to the issues with vulnerabilities this combination of utilities is efficient for analysis.

Another example of Wireshark being able to list details of a variety of network traffic which is useful in many cases such as red teaming would be recording the results of an attack like a SYN flood could entail for setting Wireshark’s capability to be a robust tool for many processes that involved real time and precise inspection of network packets. A test required several uses of recording network activity during a SYN flood attack, to which Wireshark is capable of recording statistics that can find that detailed information “the attack takes advantage of the machines’ weaknesses and able to waste performance” just by viewing statistics readily accessible within Wireshark (Mabsali, N. A., Jassim, H., & Mani, J., 2023, p.133). Within this experiment and the previous one regarding another Intrusion detection system, this proves that Wireshark is a tool that can provide precise details at the moment of network traffic occurring, and further access to diagrams and various other methods of documenting specific data that can be used to research how or when an incident can occur on an network, or analyze a network that is active for improvements or reports that disclose the state of the network and how regulations and host machines making requests to the routers are made to the internet and responses are sent back to the machine. From the initial procedure of this lab to other lab reports it is a tool that can be integral to assisting in the protection and response to network activity as it has been used entirely to detect activity and is used by professionals to response or verify that a network is protected.

Appendices
Figure 1. ARP Protocol

<img width="786" height="228" alt="Picture1" src="https://github.com/user-attachments/assets/c71da772-be04-4364-9771-2fa9293293f4" />

Figure 2. DNS Protocol

<img width="786" height="229" alt="Picture2" src="https://github.com/user-attachments/assets/8e6a64d7-23c4-4160-a70c-f22e45c325f4" />

Figure 3. HTTP Protocol

<img width="786" height="163" alt="Picture3" src="https://github.com/user-attachments/assets/a9d6db03-eec7-4e54-bd73-e4fb5ae4c547" />

Figure 4. TCP Protocol

<img width="786" height="230" alt="Picture4" src="https://github.com/user-attachments/assets/61d83d9f-d941-4517-86c3-37ed89ff9907" />


Figure 5. TLSv1.3 (HTTPS) Protocol

<img width="786" height="229" alt="Picture5" src="https://github.com/user-attachments/assets/c4060136-2fc3-4dda-b7d3-71d670244c43" />


Figure 6. UDP Protocol

<img width="786" height="228" alt="Picture6" src="https://github.com/user-attachments/assets/62c51c09-871f-424d-8071-9c9fe96cb0a9" />


Figure 7. ICMP Protocol

<img width="786" height="228" alt="Picture7" src="https://github.com/user-attachments/assets/c6ba2c35-1c5e-47fd-91d5-f82bd9903850" />


Figure 8. FTP Protocol

<img width="786" height="139" alt="Picture8" src="https://github.com/user-attachments/assets/5997cd05-5608-46ea-be59-7265c54e25b5" />


Figure 9. One Hour Scan Network Statistics

<img width="786" height="416" alt="Picture9" src="https://github.com/user-attachments/assets/4c82a9df-992a-47e7-99be-f1990a4491eb" />



Figure 10. Greater than Four Hour Scan Network Statistics

<img width="786" height="416" alt="Picture10" src="https://github.com/user-attachments/assets/5edaa95f-b0c8-4711-98bf-788cea0267a7" />




Figure 11. ARP with MAC and IP Address

<img width="786" height="220" alt="Picture11" src="https://github.com/user-attachments/assets/9aadc48c-805b-49b9-a01c-1809e5fd2cda" />


Figure 12.  Capture your computer’s MAC and IP Address

<img width="628" height="466" alt="Picture12" src="https://github.com/user-attachments/assets/b8360716-77e4-4ab9-887f-0e0372837105" />




### Resouces

SFTP.net. SFTP.net - SFTP (SSH File Transfer Protocol) info site for C#, VB.NET and Java developers. (n.d.). https://www.sftp.net/public-online-ftp-servers


### Bibliography

Jain, G. (2021, March). Application of snort and wireshark in network traffic analysis. In IOP Conference Series: Materials Science and Engineering (Vol. 1119, No. 1, p. 012007). IOP Publishing.

Mabsali, N. A., Jassim, H., & Mani, J. (2023, January). Effectiveness of Wireshark Tool for Detecting Attacks and Vulnerabilities in Network Traffic. In 1st International Conference on Innovation in Information Technology and Business (ICIITB 2022) (pp. 114-135). Atlantis Press.
