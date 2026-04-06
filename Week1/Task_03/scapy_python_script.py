from scapy.all import IP, TCP, send
from typing import List
import time


def syn_port_scan(target_ip: str, ports: List[int]) -> None:
    """
    Sends TCP SYN packets to multiple ports on the target
    to simulate a port scan.

    :param target_ip: Target machine IP address
    :param ports: List of destination ports
    """
    for port in ports:
        packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
        send(packet, verbose=False)
        time.sleep(0.2)  # Slow down to avoid overwhelming network


if __name__ == "__main__":
    TARGET_IP = "127.0.0.1"  # Change to Snort VM IP
    PORTS = list(range(20, 30))  # Sample scan range

    syn_port_scan(TARGET_IP, PORTS)
