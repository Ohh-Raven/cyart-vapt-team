from scapy.all import sniff, TCP, UDP, ICMP
import matplotlib.pyplot as plt
from collections import Counter

# -------- SETTINGS --------
INTERFACE = "tun0"   # Change to your interface:
# Linux: "lo", "wlan0"
# Windows: "Wi-Fi"

PACKET_COUNT = 1000
# --------------------------

protocol_counts = Counter()


def identify_protocol(packet):
    """Identify protocol of a packet."""
    if packet.haslayer(TCP):
        protocol_counts["TCP"] += 1
    elif packet.haslayer(UDP):
        protocol_counts["UDP"] += 1
    elif packet.haslayer(ICMP):
        protocol_counts["ICMP"] += 1
    else:
        protocol_counts["Other"] += 1


print(f"[*] Capturing {PACKET_COUNT} packets on {INTERFACE}...")

# Capture packets
sniff(iface=INTERFACE, count=PACKET_COUNT, prn=identify_protocol, store=False)

print("\n[+] Capture complete!")
print("Protocol Distribution:")
for proto, count in protocol_counts.items():
    print(f"{proto}: {count}")

# --------- Plot Bar Chart ---------
protocols = list(protocol_counts.keys())
counts = list(protocol_counts.values())

plt.figure(figsize=(8, 5))
plt.bar(protocols, counts)
plt.title("Network Protocol Distribution")
plt.xlabel("Protocol")
plt.ylabel("Packet Count")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()
