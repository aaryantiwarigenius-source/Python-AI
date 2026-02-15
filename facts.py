import requests
import json
from colorama import Fore, init

init(autoreset=True)

API_URL = "https://uselessfacts.jsph.pl/random.json?language=en"
FILE_NAME = "facts.json"

def fetch_fact():
    try:
        r = requests.get(API_URL, timeout=5)
        return r.json().get("text") if r.status_code == 200 else None
    except:
        return None
    
def menu():
    print(Fore.CYAN + "\n=== Random Fact Explorer ===")
    print(Fore.YELLOW + "[1] Get a new random fact")
    print(Fore.YELLOW + "[q] Quit")

def main():
    while True:
        menu()
        choice = input(Fore.WHITE + "Select: ").strip().lower()

        if choice == "q":
            break

        if choice == "1":
            fact = fetch_fact()
            if not fact:
                print(Fore.RED + "Failed to retrieve fact.")
                continue

            print(Fore.CYAN + "\n" + fact)

        else:
            print(Fore.RED + "Invalid selection.")

if __name__ == "__main__":
    main()