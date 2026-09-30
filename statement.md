# 5.2 Project Statement

## Problem Statement

Managing student marks and calculating academic performance manually can take time and may lead to calculation errors. The Student Evaluation System provides a simple menu-driven program to keep student names and marks for four subjects, then calculate and display averages and CGPA values.

## Scope of the Project

The project is a basic, command-line student evaluation application. It allows the user to:

- Add students using their names.
- Enter whole-number marks for four subjects, with each mark restricted to the range 0–100.
- View the names of all students currently in the system.
- Generate the overall average across marks entered for all students.
- View each student's average and CGPA, or request these results for one student.

The current program stores information only while it is running. It does not save records to a file or database. It supports one set of four subject marks per student and does not include editing, deleting, authentication, or a graphical interface.

## Target Users

- Teachers who need a small, straightforward tool to record marks and review student performance.
- Students or learners practising basic programming and wanting to understand how marks, averages, and CGPA can be handled in a program.
- Small classroom or demonstration settings where a simple command-line solution is sufficient.

## High-Level Features

1. **Student registration** — Add a student by name and reject blank or duplicate names.
2. **Marks entry and validation** — Enter marks for four subjects; accept only whole numbers from 0 to 100.
3. **Student list** — Display the names of students added during the current session.
4. **Overall average report** — Calculate the average of all subject marks entered for all students.
5. **Performance reports** — Show a student's average and CGPA, or generate those results for all students with marks.
6. **Menu-driven interaction** — Choose actions from a text menu and exit the program when finished.

*For this program, CGPA is calculated as the student's four-subject average divided by 10.*
