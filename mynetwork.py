import socket

def scan_network(network_range, ports):
    """Scans a network for hosts and open ports.

    Args:
        network_range: The IP address range to scan (e.g., '192.168.0.0/24').
        ports: A list of ports to scan for open connections.

    Returns:
        A list of hosts that are up and running on the network.
    """
    hosts = []
    for ip in range_ip_addresses(network_range):
        for port in ports:
            if is_port_open(ip, port):
                hosts.append(ip)
                break

    return hosts

def range_ip_addresses(network_range):
    """Generates a range of IP addresses from a given network range.

    Args:
        network_range: The IP address range to generate IP addresses from.

    Yields:
        The next IP address in the range.
    """
    ip_start, subnet = network_range.split('/')
    ip_parts = ip_start.split('.')
    start = int(ip_parts[-1])
    subnet = int(subnet)
    ip_base = '.'.join(ip_parts[:-1])

    for i in range(2 ** (32 - subnet)):
        yield ip_base + '.' + str(start + i)

def is_port_open(ip_address, port):
    """Checks if a port is open on a given IP address.

    Args:
        ip_address: The IP address to check.
        port: The port to check.

    Returns:
        True if the port is open, False otherwise.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        sock.connect((ip_address, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    finally:
        sock.close()

def main():
    """Scans the local network for hosts and open ports."""
    network_range = '192.168.1.0/24'
    ports = [80, 443, 22]  # Example ports to scan

    hosts = scan_network(network_range, ports)

    # Print the list of hosts
    for host in hosts:
        print(host)

if __name__ == "__main__":
    main()
