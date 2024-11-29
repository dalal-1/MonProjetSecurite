import requests
import socket
import ssl
import os
import subprocess

# URL à tester (peut être modifiée selon ton besoin)
TARGET_URL = 'https://localhost:5000'

# Fonction pour tester si un service HTTP est actif
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

# Fonction pour tester la présence d'une vulnérabilité SSL/TLS (e.g., SSLv2, SSLv3)
def test_ssl_vulnerabilities():
    try:
        print("Testing SSL/TLS vulnerabilities...")
        # Connexion SSL pour tester les versions vulnérables
        context = ssl.create_default_context()
        with socket.create_connection((TARGET_URL.split('//')[1], 443)) as sock:
            with context.wrap_socket(sock, server_hostname=TARGET_URL.split('//')[1]) as ssock:
                print(f"SSL certificate for {TARGET_URL} is valid.")
                # On pourrait aussi analyser ici la force du chiffrement ou les algorithmes obsolètes
    except Exception as e:
        print(f"SSL vulnerability test failed: {e}")

# Fonction pour tester les versions de logiciels à l'aide de banner grabbing
def test_banner_grabbing():
    try:
        print(f"Testing banner grabbing for {TARGET_URL}...")
        ip = socket.gethostbyname(TARGET_URL.split('//')[1])
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, 80))  # Port 80 pour HTTP
        sock.send(b"GET / HTTP/1.1\r\n")
        banner = sock.recv(1024)
        sock.close()
        print(f"Received banner: {banner.decode(errors='ignore')}")
    except Exception as e:
        print(f"Banner grabbing failed: {e}")

# Fonction pour analyser les erreurs de configuration dans l'application (par exemple, chemins exposés)
def test_configuration_errors():
    print("Testing for potential configuration errors...")
    errors = []
    
    # Vérification de l'existence de fichiers sensibles (ex: .env, .git, etc.)
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

# Fonction pour tester des vulnérabilités spécifiques à un CMS, un framework, etc.
def test_specific_vulnerabilities():
    print("Testing for known vulnerabilities...")
    
    # Exemple : vérifier si un script particulier existe (peut être spécifique à un CMS, etc.)
    try:
        response = requests.get(f"{TARGET_URL}/admin", timeout=5)
        if response.status_code == 200:
            print("Admin page exposed! Check for potential vulnerabilities.")
        else:
            print("Admin page not exposed.")
    except requests.exceptions.RequestException as e:
        print(f"Error checking admin page: {e}")

# Fonction principale d'exécution des tests de sécurité
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
