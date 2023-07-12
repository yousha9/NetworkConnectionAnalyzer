#! /usr/bin/python3

# Version 3.1

import psutil
import ipaddress
from colorama import Fore, Back, Style

# Get all current connections
connections = psutil.net_connections()

# Display the header
print(Fore.GREEN + Style.BRIGHT + "{:<10} {:<15} {:<25} {:<25} {:<10} {:<10} {:<25}".format(
    "Protocol", "State", "Local Address", "Remote Address", "PID",
    "Process", "Port State"
))
print(Fore.RED + Style.NORMAL + "=" * 130)
print(Style.RESET_ALL)

for conn in connections:
    if conn.status in ('ESTABLISHED', 'LISTEN', 'CLOSE_WAIT'):
        proto = conn.type.name
        state = conn.status
        local_addr = f"{conn.laddr.ip}:{conn.laddr.port}"
        remote_addr = f"{conn.raddr[0]}:{conn.raddr[1]}" if conn.raddr else "-"  # Check if raddr is empty
        pid = conn.pid
        # process = psutil.Process(pid).name()
        process = psutil.Process(pid).name() if pid is not None else "N/A"
        local_ip = conn.laddr.ip
        port_state = ipaddress.ip_address(local_ip).is_private

        values = (proto, state, local_addr, remote_addr, pid, process, port_state)
        try:
            print("{:<10} {:<15} {:<25} {:<25} {:<10} {:<10} {:<25}".format(*values))
        except Exception as e:
            print(f"Error formatting values: {e}")
            print(f"Values: {values}")
