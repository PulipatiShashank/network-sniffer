import socket

def main():
    # Create raw socket (for IPv4 packets)
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

    # Use your local IP address
    host = socket.gethostbyname(socket.gethostname())

    sniffer.bind((host, 0))

    # Include IP headers
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # Enable promiscuous mode (only works on Windows)
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    print(f"🔍 Sniffing started on {host}... Press Ctrl+C to stop.\n")

    try:
        while True:
            raw_data = sniffer.recvfrom(65565)[0]
            print(f"[+] Packet received: {raw_data[:20]}")
    except KeyboardInterrupt:
        # Turn off promiscuous mode before exit
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        print("\n🛑 Sniffing stopped.")

if __name__ == "__main__":
    main()
