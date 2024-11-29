import time
from zapv2 import ZAPv2

# Initialize ZAP instance
target_url = "http://127.0.0.1:5000"  # URL of your Flask app
zap = ZAPv2()

# Start ZAP spidering
def start_spider(target_url):
    print(f"Spidering target: {target_url}")
    zap.spider.scan(target_url)
    while int(zap.spider.status) < 100:
        print(f"Spider progress: {zap.spider.status}%")
        time.sleep(2)

# Start ZAP active scan
def start_active_scan(target_url):
    print(f"Starting active scan on target: {target_url}")
    zap.ascan.scan(target_url)
    while int(zap.ascan.status) < 100:
        print(f"Active Scan progress: {zap.ascan.status}%")
        time.sleep(2)

# Get the alerts found by ZAP
def get_alerts():
    alerts = zap.core.alerts(baseurl=target_url, start=0, count=10)
    print("Found Alerts:")
    for alert in alerts:
        print(f"Alert: {alert}")

# Main function
if __name__ == '__main__':
    print("Starting security scan...")

    # Run spidering
    start_spider(target_url)

    # Run active scan
    start_active_scan(target_url)

    # Fetch and print alerts
    get_alerts()

    print("Security scan completed.")
