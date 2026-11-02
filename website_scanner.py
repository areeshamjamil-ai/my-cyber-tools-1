# Areesha Jamil - Website Security Scanner
import requests

url = input("Enter website URL (https://example.com): ")
print(f"Scanning {url}...")

try:
    r = requests.get(url, timeout=5)
    print(f"Status Code: {r.status_code}")
    
    headers = r.headers
    checks = ["X-Frame-Options", "Content-Security-Policy", "X-XSS-Protection"]
    
    for h in checks:
        if h in headers:
            print(f"{h}: Found - Secure")
        else:
            print(f"{h}: Missing - Not Secure")
    
    print("Scan Complete!")
except:
    print("Website not reachable!")
