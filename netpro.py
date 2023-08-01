import socket
import subprocess

def is_host_reachable(host):
    """Check if the target host is reachable using ICMP (ping).
    Args:
        host (str): The target host IP address or hostname.
    Returns:
        bool: True if the host is reachable, False otherwise.
    """
    try:
        subprocess.check_output(['ping', '-c', '1', host])
        print(f"Host {host} is reachable.")
        return True
    except subprocess.CalledProcessError:
        print(f"Host {host} is not reachable.")
        return False

def scan_port(host, port):
    """Scan a specific port on a target host.
    Args:
        host (str): The target host IP address or hostname.
        port (int): The port to scan.
    Returns:
        bool: True if the port is open, False otherwise.
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        # Connect to the specified port on the target host
        result = sock.connect_ex((host, port))

        # Check if the connection was successful (port is open)
        if result == 0:
            print(f"Port {port} is open on {host}")
            return True
        else:
            return False
    except Exception:
        return False

def scan_all_ports(host):
    """Scan all common ports (1 to 1024) on a target host.
    Args:
        host (str): The target host IP address or hostname.
    """
    print(f"Scanning all common ports on {host}...")
    open_ports = []
    for port in range(1, 1025):
        if scan_port(host, port):
            open_ports.append(port)

    if len(open_ports) > 0:
        print(f"Open ports on {host}: {open_ports}")
    else:
        print(f"No open ports found on {host}.")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address or hostname: ")

    # Check if the host is reachable using ICMP
    if is_host_reachable(target_ip):
        # Proceed with permission from the user
        permission = input("Do you have permission to scan this host? (y/n): ").lower()
        if permission == 'y':
            scan_all_ports(target_ip)
        else:
            print("Scanning aborted. Please get permission before scanning.")
    else:
        print("Cannot proceed with scanning. The host is not reachable.")
