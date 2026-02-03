from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_analyzer(packet):

    if IP in packet:
        print("\n=========== PACKET CAPTURED ===========")

        print("Source IP        :", packet[IP].src)
        print("Destination IP   :", packet[IP].dst)

        if TCP in packet:
            print("Protocol         : TCP")
            print("Source Port      :", packet[TCP].sport)
            print("Destination Port :", packet[TCP].dport)

        elif UDP in packet:
            print("Protocol         : UDP")
            print("Source Port      :", packet[UDP].sport)
            print("Destination Port :", packet[UDP].dport)

        else:
            print("Protocol         : Other")

        if packet.haslayer(Raw):
            print("Payload          :", packet[Raw].load)

print("Starting Network Sniffer...")
print("Press CTRL + C to stop\n")

sniff(prn=packet_analyzer, store=False)

