# Data-base-management-system

A simple command-line student evaluation program written in Python. It lets you add students, record marks for four subjects, view the student list, and generate average and CGPA reports.

## Requirements

- Python 3
- No third-party packages are required

## Run the program

Open a terminal in the folder containing `vityarthi project.py`, then run:

```bash
python "vityarthi project.py"
```

On systems where Python is invoked as `python3`:

```bash
python3 "vityarthi project.py"
```

## How to use it

At the main menu, choose an option by entering its number:

1. **Add a student** — enter a non-empty name. Duplicate names are rejected.
2. **Add marks for 4 subjects** — select an existing student and enter a whole-number mark from 0 to 100 for each subject.
3. **Reports** — choose one of the available reports:
   - Overall average across all marks entered
   - Average and CGPA for each student with marks
   - Average and CGPA for one selected student
4. **View all students** — list the names currently in the session.
5. **Exit** — quit the program.

The average is calculated from the four subject marks. CGPA is calculated as `average / 10`. If a student's marks are entered again, the new four marks replace the previous set.

## Data storage

Student records are kept in memory while the program runs. They are not saved to a file or database, so the records are cleared when you exit.
