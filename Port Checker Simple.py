import socket

def check_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        return True
    except:
        return False
    finally:
        s.close()

host = input("Enter the host IP address: ")
port = int(input("Enter the port number: "))

if check_port(host, port):
    print(f"Port {port} on host {host} is open")
else:
    print(f"Port {port} on host {host} is closed")
