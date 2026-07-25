Persistent Warehouse Inventory Manager (Python & JSON)

A Python command-line application for managing warehouse stock with persistent JSON file storage and CRUD (Create, Read, Update, Delete) functionality.

How it Works & Features:

- Data Persistence with JSON: Automatically loads inventory data from a local `sklad.json` file upon startup and updates the file whenever items are added or removed.
- Graceful Error Handling: If `sklad.json` does not exist on the first run, the app catches `FileNotFoundError` and initialises default stock items automatically.
- View Stock: Displays current inventory items with capitalised names (`.capitalize()`) and formatted prices in EUR.
- Add & Update Stock: Allows adding new items or updating existing item prices, immediately syncing changes to the JSON file.
- Safe Item Removal: Checks if an item exists in the inventory (`if ... in sklad`) before deleting it to prevent runtime errors.

Technologies & Concepts Used:

- Language: Python 3.12+
- Modules: `json` (`json.load`, `json.dump`)
- Data Structures: Dictionaries (`sklad = {...}`) for key-value pair mapping (Item -> Price)
- File Handling & Persistence: Context managers (`with open(...)`) for safe reading and writing to disk
- Exception Handling: `try / except FileNotFoundError` block
- Control Flow: Interactive `while True` main menu loop with conditional branching (`if / elif / else`)

How to Run:

1. Make sure Python 3 is installed.
2. Run the script: https://github.com/Dom1n1kSk/Python-projekty/blob/main/Skladovy_Manazer/Skladov%C3%BD%20mana%C5%BE%C3%A9r.py
