import socket

def check_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((host, port))
        print(f"Port {port} is open")
        s.close()
        return True
    except socket.error as e:
        print(f"Port {port} is closed")
        s.close()
        return False

def check_ports(host, ports):
    for port in ports:
        check_port(host, port)

ports = [4897, 4998, 4776]
hostname = socket.gethostname()
check_ports(hostname, ports)
