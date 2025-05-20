#!/usr/bin/env python3
import os
import subprocess

# Dynamisch pad naar input.txt
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, "input.txt")
KEYWORD    = "Hello World"

def grep_keyword(file_path, keyword):
    result = subprocess.run(
        ["grep", "-n", keyword, file_path],
        capture_output=True, text=True
    )
    return result.stdout

def main():
    matches = grep_keyword(INPUT_FILE, KEYWORD)
    if matches:
        print("Grep-resultaten:\n")
        print(matches)
    else:
        print("Geen matches gevonden voor:", KEYWORD)

if __name__ == "__main__":
    main()
# Dit script zoekt naar de string "Hello World" in het bestand input.txt
# en print de regels waarin deze voorkomt, samen met de regelnummer.