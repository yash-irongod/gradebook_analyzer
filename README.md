# GradeBook Analyzer
A Python-based command-line tool to input, analyze, grade, and report student marks.  
This project is developed for the course: **Programming for Problem Solving using Python**.

---

## 📘 Project Overview
The GradeBook Analyzer automates the work of lecturers by:
- Accepting student marks from manual input or a CSV file
- Computing average, median, highest, and lowest marks
- Assigning grade letters (A–F)
- Listing pass/fail students using list comprehensions
- Printing a formatted report table
- Optionally exporting results to CSV
- Allowing repeated analysis through a CLI menu

This project implements all 6 tasks defined in the assignment.

---

## 📁 Folder Structure

gradebook_analyzer/ 
│── gradebook.py 
│── README.md 
│── requirements.txt 
│── .gitignore 
│── grades_output.csv       (example file) 

---

## 🧩 Features Implemented (as per Assignment Tasks)

### ✔ **Task 1 – Project Setup**
- `gradebook.py` created with author header  
- CLI welcome menu with options:
  - (1) Manual Entry  
  - (2) Load CSV  

---

### ✔ **Task 2 – Data Entry / CSV Import**
- Manual input of names + marks  
- CSV loading with the Python `csv` module  
- Data stored as dictionary:  
  `marks = {"Alice": 78, "Bob": 92, ...}`  

---

### ✔ **Task 3 – Statistical Analysis**
Custom functions implemented:
- `calculate_average(marks_dict)`
- `calculate_median(marks_dict)`
- `find_max_score(marks_dict)`
- `find_min_score(marks_dict)`

---

### ✔ **Task 4 – Grade Assignment**
Grade logic:
- A : 90+
- B : 80–89
- C : 70–79
- D : 60–69
- F : <60

Grades stored:
`grades = {"Alice": "C", "Bob": "A", ...}`

Also prints:
- Count per grade category  
- Highest and lowest performers  

---

### ✔ **Task 5 – Pass/Fail List Comprehension**
List comprehension used:

passed_students = [name for name, m in marks.items() if m >= 40] failed_students = [name for name, m in marks.items() if m < 40]

Output includes:
- Number passed  
- Number failed  
- Names in each group  

---

### ✔ **Task 6 – Results Table + Menu Loop**
- Formatted table with:

Name     Marks    Grade

Alice     78        C Bob       92        A

- `while True:` loop for repeating analysis  
- Optional CSV export function  

---

## 🔄 CSV Export
After analysis, user can export results to:

exported_results.csv

This file will include:

name,marks,grade Alice,78,C Bob,92,A ...

---

## 📄 Example CSV file (grades_output.csv)
[grades_output](grades_output.csv)


---
