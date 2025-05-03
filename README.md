Network Sniffer (Educational Use Only)
This is a basic Python-based network packet sniffer designed for educational purposes. It captures IPv4 packets using raw sockets, allowing you to see network traffic on your local machine. This tool is intended for learning about networking, protocols, and raw socket programming.

Important: This tool only works on Windows and requires Administrator privileges to run.

Features
📡 Captures IPv4 packets in real-time

🧑‍💻 Uses raw sockets for packet sniffing

🚨 Runs in promiscuous mode to capture all traffic

⚡ Simple and lightweight implementation

Prerequisites
Python 3.x

Administrator privileges (for using raw sockets and enabling promiscuous mode)

Installation
Download the repository:

bash
Copy
Edit
git clone https://github.com/your-username/network-sniffer.git
cd network-sniffer
Run the script:

Since raw socket operations require admin privileges, you need to run this script as an administrator.

Open Command Prompt as Administrator.

Navigate to the folder containing the script:

bash
Copy
Edit
cd "E:\My Portfolio"
Then run the script:

bash
Copy
Edit
python sniffer_win.py
Usage
Once the script is running, it will capture all incoming and outgoing IPv4 packets on your network interface. It will print the first 20 bytes of each packet in the terminal.

To stop sniffing, press Ctrl + C.

Example Output
vbnet
Copy
Edit
🔍 Sniffing started on 192.168.1.5... Press Ctrl+C to stop.

[+] Packet received: b'\x45\x00\x00\x3c\x1c\x46\x40\x00\x40\x06\xb1\xe6\xc0\xa8\x00\x68\xc0\xa8\x00\x01'
[+] Packet received: b'\x45\x00\x00\x3c\x1c\x47\x40\x00\x40\x06\xb1\xe7\xc0\xa8\x00\x68\xc0\xa8\x00\x02'
Notes
Promiscuous mode: Enables the sniffing of all packets on the network, not just those directed to the machine.

The script will capture raw Ethernet frames and display the first 20 bytes of each packet.

License
This project is for educational use only. Please ensure you're using it ethically and legally. Unauthorized packet sniffing can be illegal in many regions.

Disclaimer
This project is intended for learning purposes and ethical hacking. Always ensure you have proper authorization before sniffing network traffic.
