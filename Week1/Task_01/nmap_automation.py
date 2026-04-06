"""
Automated Nmap Scanner using python-nmap

This script:
1. Takes a target IP or hostname as input
2. Performs a SYN scan (-sS) with service version detection (-sV)
3. Extracts:
   - Host IP
   - Open ports
   - Service names and versions
4. Saves results into a text report file
"""

import nmap
from datetime import datetime

# Create Nmap scanner object
scanner = nmap.PortScanner()

# Take target input from user
target = input("Enter target IP or hostname: ")

print("\n[+] Starting Nmap Scan...\n")

# Perform SYN scan (-sS) with service version detection (-sV)
scanner.scan(hosts=target, arguments='-sS -sV')

# Get current timestamp for report
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Open report file for writing
report_file = open("scan_report.txt", "w")

# Write header information
report_file.write("=== NMAP SCAN REPORT ===\n")
report_file.write(f"Scan Time: {timestamp}\n")
report_file.write(f"Target: {target}\n")
report_file.write("=" * 40 + "\n\n")

# Process scan results
for host in scanner.all_hosts():
    report_file.write(f"Host IP: {host}\n")
    report_file.write(f"State: {scanner[host].state()}\n\n")

    report_file.write("Open Ports:\n")
    report_file.write("-" * 40 + "\n")
    report_file.write("Port\tService\tVersion\n")
    report_file.write("-" * 40 + "\n")

    # Loop through protocols (tcp/udp)
    for proto in scanner[host].all_protocols():
        ports = scanner[host][proto].keys()

        for port in ports:
            port_data = scanner[host][proto][port]

            # Check if port is open
            if port_data['state'] == 'open':
                service = port_data['name']
                version = port_data['version']

                report_file.write(f"{port}\t{service}\t{version}\n")

    report_file.write("\n")

# Write completion note
report_file.write("=" * 40 + "\n")
report_file.write("Scan Completed Successfully.\n")

# Close file
report_file.close()

print("[+] Scan completed!")
print("[+] Report saved as: scan_report.txt")
