# Student Evaluation System

A menu-driven, console-based Python application that lets a teacher or evaluator register students, record marks for four subjects, and generate average and CGPA reports.

## Overview

Manually calculating averages and CGPA for a class is slow and error-prone. This project stores student records in memory, validates every input, and produces overall and per-student reports on demand. It is built only with core Python (dictionaries, lists, loops, conditionals and string handling), so it runs anywhere Python 3 is installed.

## Features

- **Add a student** - rejects empty names and duplicate entries.
- **Add marks for 4 subjects** - accepts only whole numbers from 0 to 100; invalid input cancels the entry without saving partial data.
- **Reports**
  - Overall average of all recorded marks.
  - Average and CGPA of every student.
  - Average and CGPA of one selected student.
- **View all students** - lists every registered student.
- **Friendly error messages** for empty database, unknown student, incomplete marks and invalid menu choices.

CGPA is calculated as `average marks / 10` (a 10-point scale approximation).

## Technologies Used

- Python 3.8 or later (no external libraries)
- Git and GitHub for version control

## Project Structure

```
.
├── student_evaluation.py     # Main application
├── README.md                 # This file
├── statement.md              # Problem statement, scope, users, features
└── docs/
    ├── diagrams/             # Architecture, workflow, use case, sequence, component, data structure
    └── screenshots/          # Sample console sessions (sample_session.txt, edge_cases.txt)
```

## Installation and Running

1. Install Python 3 from https://www.python.org/downloads/ and confirm it works:
   ```
   python --version
   ```
2. Clone the repository:
   ```
   git clone <your-repository-url>
   cd <repository-folder>
   ```
3. Run the program:
   ```
   python student_evaluation.py
   ```
   (Use `python3` on Linux/macOS if `python` is not found.)

## How to Use

1. Choose **1** and enter a student name.
2. Choose **2**, enter the student name, then four whole-number marks (0-100).
3. Choose **3** to open the reports menu and pick report 1, 2 or 3.
4. Choose **4** to list all students.
5. Choose **5** to exit.

## Testing

The project is tested with manual validation tests. Run the program and try the cases below, or replay them with piped input.

| # | Action | Expected result |
|---|--------|-----------------|
| 1 | Add student `Asha` | `Asha added.` |
| 2 | Add `Asha` again | `That student is already in the database.` |
| 3 | Add an empty name | `Name cannot be empty.` |
| 4 | Add marks before any student exists | `The database is empty.Please add a student first.` |
| 5 | Add marks for an unknown student | `Student not found.` |
| 6 | Enter `abc`, `-5` or `7.5` as a mark | `Please enter a whole number.` |
| 7 | Enter `105` as a mark | `Marks must be between 0 and 100.` |
| 8 | Marks 85, 90, 78, 92 for Asha, then per-student report | average `86.25`, CGPA `8.62` |
| 9 | Asha (85, 90, 78, 92) + Ravi (60, 75, 80, 65), overall average | `78.12` |
| 10 | Per-student report for a student without marks | `Enter all 4 subject marks for <name> first.` |
| 11 | Menu choice `7` | `Please choose a number from 1 to 5.` |

Expected outputs from real runs are saved in `docs/screenshots/`.

## Screenshots

Console transcripts of a normal session and of edge cases are in `docs/screenshots/`. Add your own terminal screenshots there and link them here, for example:

```
![Main menu](docs/screenshots/menu.png)
```

## Limitations

- Data is stored in memory only and is lost when the program exits.
- Re-entering marks for a student replaces the earlier marks.
- Always exactly four subjects.

## Future Enhancements

Save data to a file or database, split the code into modules with unit tests, add edit/delete of students, grade classification and ranking, and a GUI or web interface.
