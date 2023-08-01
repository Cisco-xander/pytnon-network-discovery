import whois
import socket

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        print("WHOIS Information:")
        print("Domain Name:", w.domain_name)
        print("Registrar:", w.registrar)
        print("Creation Date:", w.creation_date)
        print("Expiration Date:", w.expiration_date)
        print("Name Servers:", w.name_servers)
    except Exception as e:
        print("Error retrieving WHOIS information:", str(e))

def get_dns_records(domain):
    try:
        print("DNS Records for", domain)
        ip = socket.gethostbyname(domain)
        print("IP Address:", ip)
        print("Name Servers:")
        nameservers = socket.gethostbyaddr(ip)[0]
        for ns in nameservers:
            print("-", ns)
    except Exception as e:
        print("Error retrieving DNS records:", str(e))

# Example usage
website = "example.com"

get_whois_info(website)
print()
get_dns_records(website)
