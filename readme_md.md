# Mess Feedback System

A simple, console-based Python project for managing and analyzing student mess feedback in school or college hostels. Built using fundamental Python file-handling concepts without any external module dependencies.

---

## Features

- **Add Feedback:** Collects student registration number, name, mess name, meal choice (Breakfast, Lunch, High Tea, Dinner), rating (1-5), and comments.
- **Display All Feedback:** Reads and displays all stored reviews in a clean, formatted layout.
- **Search Feedback:** Looks up reviews instantly using a student's registration number.
- **Mess Average Rating:** Computes the average score for any specific mess hall and categorizes its performance status.
- **Meal Average Rating:** Analyzes ratings across specific meal types.
- **Delete Feedback:** Removes specific records securely using registration numbers.
- **Zero Imports:** Completely dependency-free (no `pickle`, no `os`, or third-party libraries required).

---

## Project Structure

```text
├── mess_feedback_system.py   # Main Python source code
├── feedback.txt              # Text file created automatically for data storage
└── README.md                 # Project documentation
```

---

## How to Run

1. Make sure you have Python installed on your computer.
2. Download or copy the `mess_feedback_system.py` script.
3. Open your terminal or command prompt in the project folder and run:
   ```bash
   python mess_feedback_system.py
   ```
4. Follow the on-screen menu prompts to add, view, search, or analyze feedback.

---

## Requirements

- Python 3.x (Standard library only; no extra packages needed).

---

## Author

Developed as a school computer science project.