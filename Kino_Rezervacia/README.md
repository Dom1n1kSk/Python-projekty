Cinema Ticket & Snack Booking System (Python)

A Python command-line application for booking movie tickets and selecting snack add-ons with dynamic price calculation and formatted receipt generation.

How it Works & Features:

- Dynamic Movie Listing: Iterates over a list of available movies (`"Spiderman"`, `"Avatar"`, `"Matrix"`) using `enumerate()` to display numbered options to the user.
- Ticket Availability Check: Verifies if the requested number of tickets exceeds available seats (capacity set to 100) before confirming the order.
- Snack & Concession Upselling: Offers 3 options for snacks (No snacks, Popcorn, Combo menu) and updates the total order cost accordingly.
- Receipt Formatting: Prints a cleanly aligned summary ticket showing the chosen movie, ticket quantity, snack selection, and the final total price in EUR.

Technologies & Concepts Used:

- Language: Python 3.12+
- Data Structures: Lists (`filmy = [...]`)
- Built-in Functions: `enumerate()`, `int()`, `input()`, `print()`
- Control Flow: Nested `if / elif / else` conditional statements for movie indexing, seat availability, and snack choices
- Arithmetic Logic: Real-time calculation of total ticket costs, snack additions, and remaining seat capacity

How to Run:

1. Make sure Python 3 is installed.
2. Run the script: https://github.com/Dom1n1kSk/Python-projekty/blob/main/Kino_Rezervacia/Kino%20rezerv%C3%A1cia.py
