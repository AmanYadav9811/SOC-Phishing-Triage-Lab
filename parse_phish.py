import re

with open("raw_email.eml", "r") as f:
    content = f.read()

# Extract IPs
ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', content)
# Extract URLs
urls = re.findall(r'https?://[^\s]+', content)
# Extract Domains
domains = re.findall(r'@([\w\.-]+)', content)

print("=== SOC INCIDENT TRIAGE: AUTOMATED IOC EXTRACTION ===")
print(f"[+] Originating IPs Found: {list(set(ips))}")
print(f"[+] Suspicious Domains:   {list(set(domains))}")
print(f"[+] Malicious URLs:       {list(set(urls))}")
