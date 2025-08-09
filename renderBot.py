
print(r"""
         ^
       //                        ___   ___
     (*)     "O"                /  _   _  \
    (*)                           / \ / \
   (*)    "O"                    |   |   |    |\
  //                             |O  |O  |___/  \     ++
 //                               \_/ \_/    \   | ++
//                              _/      __    \  \
/     /|   /\                  (________/ __   |_/
     / |  |  |                   (___      /   |    |\
    / /  /   |                     \     \|    |___/  |
   |  | |   /                       \_________      _/   ++++
  /   | |  |                      ++           \    |
 |   / /   |                              ++   |   /  +++
/   /  |   |                               ++ /__/
~~~ ~~~~   ~~~~~~~~~~~~  ~~~~~~~~~~~~~  ~~~~        ~~+++~~~~ ~
coded by rayane-neko-dev""")
import requests
import random
import time
import concurrent.futures

# URL of your Render site
TARGET_URL = "https://gaza-aid-encyclopedia.onrender.com"  # put here your render url pirate

# Proxy list API (HTTPS only)
PROXY_API = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=8000&country=all"

# Thread pool size
THREADS = 50

def fetch_proxies():
    """Fetch raw proxy list from ProxyScrape."""
    print("[*] Fetching proxies...")
    try:
        res = requests.get(PROXY_API, timeout=15)
        res.raise_for_status()
        proxies = [p.strip() for p in res.text.splitlines() if p.strip()]
        print(f"[+] Got {len(proxies)} raw HTTPS proxies")
        return proxies
    except Exception as e:
        print(f"[!] Failed to fetch proxies: {e}")
        return []

def test_proxy(proxy):
    """Test if a proxy works for HTTPS."""
    try:
        proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        r = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=15)
        if r.status_code == 200:
            print(f"[OK] {proxy}")
            return proxy
    except:
        pass
    return None

def get_working_proxies():
    """Fetch and test proxies using multiple threads."""
    raw_proxies = fetch_proxies()
    working = []
    print("[*] Testing proxies...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        results = executor.map(test_proxy, raw_proxies)
        for proxy in results:
            if proxy:
                working.append(proxy)
    print(f"[+] Found {len(working)} working HTTPS proxies")
    return working

def main():
    working_proxies = get_working_proxies()
    if not working_proxies:
        print("[!] No working proxies found. Exiting.")
        return

    while True:
        if not working_proxies:
            print("[*] Refreshing proxy list...")
            working_proxies = get_working_proxies()
            if not working_proxies:
                time.sleep(60)
                continue

        proxy = working_proxies.pop(0)
        try:
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
            r = requests.get(TARGET_URL, proxies=proxies, timeout=15)
            print(f"[REQ] {proxy} -> {r.status_code}")
        except Exception as e:
            print(f"[FAIL] {proxy} -> {e}")

        delay = random.randint(0, 30)
        print(f"[*] Sleeping for {delay} seconds...")
        time.sleep(delay)

if __name__ == "__main__":
    main()
