# Project Statement - Student Evaluation System

## Problem Statement

Teachers and small institutions often record student marks on paper or in loose spreadsheets and calculate averages and CGPA by hand. This is time-consuming and error-prone: names get duplicated, marks outside the valid range slip in, and results are inconsistent. There is a need for a simple, reliable tool that stores student records, checks every input, and produces accurate average and CGPA reports instantly.

## Scope of the Project

**In scope**

- Registering students by unique name.
- Recording exactly four subject marks (whole numbers, 0-100) per student.
- Reports: overall average of all students, average and CGPA of all students, average and CGPA of one student.
- Listing all registered students.
- Input validation and clear error messages in a console interface.

**Out of scope (current version)**

- Permanent storage (files or databases); data lasts for one session.
- User login, roles or multi-user access.
- Editing or deleting students, variable subject counts, grade letters or ranking.
- Graphical or web interface.

## Target Users

- School and college teachers or evaluators who need quick class statistics.
- Students learning Python who want a clear example of dictionaries, lists, loops and validation.
- Small coaching centres needing a lightweight marks calculator.

## High-Level Features

1. Student management (add, view).
2. Marks entry with strict validation (whole numbers, 0-100, four subjects).
3. Reporting and analytics (overall average, per-student average, CGPA).
4. Menu-driven workflow with helpful error handling for every invalid action.
