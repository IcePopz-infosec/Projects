import scapy.all as scapy


def packet_sniffer(packet):
    if packet.haslayer(scapy.Raw):
        print(packet[scapy.Raw].load)


def start_sniffer(interface):
    scapy.sniff(iface=interface, store=False, prn=packet_sniffer)


# Replace 'eth0' with the name of your network interface (e.g., 'eth0', 'wlan0')
start_sniffer('lo0')
