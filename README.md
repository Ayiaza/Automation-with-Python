# 📁 Daily Log File Generator

This Python script automates the creation of a personalized weekly log folder — saving you time by generating structured daily task files in just a few seconds. It's a beginner-friendly project that bridges the gap between Python basics and real-world file management.

---

## 🛠️ Technologies Used

- **Python 3** — The core programming language powering the entire script
- **`os` module** — A built-in Python library used to interact with the operating system, handle folder creation, check paths, and build file paths in a cross-platform way
- **File I/O (`open`, `write`)** — Python's built-in file handling system used to create and write content into `.txt` files
- **`input()` function** — Python's standard way to capture real-time input from the user in the terminal

---

## ✨ Features

- **Custom Folder Creation** — Prompts the user to name their own folder; creates it only if it doesn't already exist (no accidental overwrites)
- **Automated File Generation** — Automatically creates 5 `.txt` files, one for each weekday (Monday through Friday)
- **Personalized Content** — Asks the user for a unique task entry for each day and writes it directly into that day's file
- **Structured Format** — Each file is pre-formatted with a header and a task label for clean, readable output
- **Success Feedback** — Prints confirmation messages in the terminal after each file is saved and a final success message when all files are done

---

## 🔄 How It Works — Step by Step

1. **User inputs a folder name** — The script uses `input()` to ask for a folder name and stores it in `folder_name`
2. **Folder existence check** — `os.path.exists()` checks if the folder already exists; if not, `os.makedirs()` creates it
3. **Day list is defined** — A hardcoded list of weekday names (`["Monday", ..., "Friday"]`) is set up for iteration
4. **Loop runs for each day** — A `for` loop iterates over each day in the list
5. **File path is built** — `os.path.join()` combines the folder name and day name to create a proper file path
6. **User enters a task** — `input()` prompts the user for their main task for that specific day
7. **File is created and written** — Python opens the file in write mode (`"w"`) and writes a formatted header along with the user's task
8. **Confirmation is printed** — A success message appears in the terminal for each file created
9. **Final message displayed** — Once the loop finishes, a completion message confirms all 5 files were generated

---

## 📚 What I Learned

- How to use Python's `os` module to interact with the file system — creating folders, checking paths, and joining directory names safely
- How to combine user input, loops, and file I/O to build a small but fully functional automation tool from scratch

---

## ✅ Conclusion

This project demonstrates how even a short Python script can automate repetitive tasks and produce real, usable output. It's a solid foundation for anyone learning Python who wants to go beyond theory and build something practical.
## Run the Project <br>

https://github.com/user-attachments/files/29333636/output.html
