import requests
import socket
import ssl
import os
import subprocess
from urllib.parse import urlparse

# URL to test (can be modified according to your needs)
TARGET_URL = 'https://localhost:5000'

# Function to test if an HTTP service is active
def test_http_service():
    try:
        print(f"Testing HTTP service at {TARGET_URL}...")
        response = requests.get(TARGET_URL, timeout=5)
        if response.status_code == 200:
            print("HTTP service is running successfully.")
        else:
            print(f"HTTP service returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error during HTTP service check: {e}")

# Function to test for SSL/TLS vulnerabilities (e.g., SSLv2, SSLv3)
def test_ssl_vulnerabilities():
    try:
        print("Testing SSL/TLS vulnerabilities...")
        # Parsing URL to extract host and port
        parsed_url = urlparse(TARGET_URL)
        host = parsed_url.hostname
        port = parsed_url.port if parsed_url.port else 443  # Default to 443 if no port is specified

        context = ssl.create_default_context()
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                print(f"SSL certificate for {TARGET_URL} is valid.")
                # You could also analyze the encryption strength or deprecated algorithms here
    except Exception as e:
        print(f"SSL vulnerability test failed: {e}")

# Function to test software versions using banner grabbing
def test_banner_grabbing():
    try:
        print(f"Testing banner grabbing for {TARGET_URL}...")
        parsed_url = urlparse(TARGET_URL)
        ip = socket.gethostbyname(parsed_url.hostname)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # Added timeout to avoid hanging
        sock.connect((ip, 80))  # Port 80 for HTTP
        sock.send(b"GET / HTTP/1.1\r\n")
        banner = sock.recv(1024)
        sock.close()
        print(f"Received banner: {banner.decode(errors='ignore')}")
    except Exception as e:
        print(f"Banner grabbing failed: {e}")

# Function to analyze application configuration errors (e.g., exposed paths)
def test_configuration_errors():
    print("Testing for potential configuration errors...")
    errors = []
    
    # Checking for the existence of sensitive files (e.g., .env, .git, etc.)
    sensitive_files = ['.git', '.env', 'config.php']
    for file in sensitive_files:
        if os.path.exists(file):
            errors.append(f"Sensitive file found: {file}")
    
    if errors:
        print("Potential configuration errors detected:")
        for error in errors:
            print(error)
    else:
        print("No configuration errors detected.")

# Function to test for specific vulnerabilities (e.g., exposed admin pages)
def test_specific_vulnerabilities():
    print("Testing for known vulnerabilities...")
    
    # Example: Check if an admin page is exposed (specific to certain CMS, frameworks, etc.)
    try:
        response = requests.get(f"{TARGET_URL}/admin", timeout=5)
        if response.status_code == 200:
            print("Admin page exposed! Check for potential vulnerabilities.")
        else:
            print("Admin page not exposed.")
    except requests.exceptions.RequestException as e:
        print(f"Error checking admin page: {e}")

# Main function to execute the security tests
def run_security_tests():
    test_http_service()
    test_ssl_vulnerabilities()
    test_banner_grabbing()
    test_configuration_errors()
    test_specific_vulnerabilities()

if __name__ == '__main__':
    print("Starting security scan...\n")
    run_security_tests()
    print("\nSecurity scan completed.")
