import requests
from ai_analyzer import classify_response

def load_payloads():
    with open("payloads.txt") as f:
        return [line.strip() for line in f.readlines()]

def scan_url(url):
    payloads = load_payloads()
    print(f"[+] Scanning {url} with {len(payloads)} payloads...\n")

    for payload in payloads:
        test_url = f"{url}?input={payload}"
        try:
            response = requests.get(test_url, timeout=5)
            if classify_response(response.text):
                print(f"[!!] AI detected SQLi at: {test_url}\n")
            else:
                print(f"[OK] Safe: {test_url}\n")
        except Exception as e:
            print(f"[Error] Could not connect: {e}\n")

if __name__ == "__main__":
    target = input("Enter target URL (e.g., http://localhost/test.php): ")
    scan_url(target)
