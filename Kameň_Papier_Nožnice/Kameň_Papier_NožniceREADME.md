Rock, Paper, Scissors with Match History (Python)

A command-line implementation of the classic Rock, Paper, Scissors game built in Python.

How it Works & Features:

- Player vs. Computer: The player inputs their choice (`kameň`, `papier`, `nožnice`), and the computer selects a move randomly using Python's `random.choice()`.
- Match History Tracking: Every match result ("Remíza", "Výhra", "Prehra") is saved into a list.
- Game Exit & Summary: Entering `'koniec'` terminates the game loop and prints out the entire match history list for the session.
- Case Insensitive Input: Uses `.lower()` so player inputs work regardless of capitalization.

Technologies & Concepts Used:

- Language: Python 3.12+
- Modules: `random` (`random.choice`)
- Data Structures: Lists (`historia = []` for tracking results)
- Control Flow: `while True` loop, `if / elif / else` conditional statements, string methods (`.lower()`)

How to Run:

1. Make sure Python 3 is installed.
2. Run the script: https://github.com/Dom1n1kSk/Python-projekty/blob/main/Kame%C5%88_Papier_No%C5%BEnice/Kame%C5%88%20papier%20no%C5%BEnice.py
