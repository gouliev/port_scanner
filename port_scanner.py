import socket
import concurrent.futures

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        return f"Port {port} is open"
    except (socket.timeout, socket.error):
        return f"Port {port} is closed"

def main():
    host = input("Enter the IP to scan: ")
    port_range = [80, 443]  # Define your port range here
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan, host, port) for port in range(port_range[0], port_range[1]+1)]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    main()
