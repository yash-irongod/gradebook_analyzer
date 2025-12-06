#!/usr/bin/env python3
"""
Name : Yash Kaushik
Title: GradeBook Analyzer - Analysing and Reporting Student Grades

Course: Programming for Problem Solving using Python
Mini Assignment: Analysing and Reporting Student Grades
"""

import csv
import statistics
import os
from typing import Dict, List, Tuple

# -------------------------
# Task 3: Statistical functions
# -------------------------
def calculate_average(marks_dict: Dict[str, float]) -> float:
    """Return average (mean) of marks. Returns 0.0 for empty dict."""
    if not marks_dict:
        return 0.0
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict: Dict[str, float]) -> float:
    """Return median of marks. Uses statistics.median for correctness."""
    if not marks_dict:
        return 0.0
    return statistics.median(list(marks_dict.values()))

def find_max_score(marks_dict: Dict[str, float]) -> Tuple[str, float]:
    """Return (name, score) of the student with highest score. If tie returns first encountered."""
    if not marks_dict:
        return ("", 0.0)
    name = max(marks_dict, key=marks_dict.get)
    return (name, marks_dict[name])

def find_min_score(marks_dict: Dict[str, float]) -> Tuple[str, float]:
    """Return (name, score) of the student with lowest score. If tie returns first encountered."""
    if not marks_dict:
        return ("", 0.0)
    name = min(marks_dict, key=marks_dict.get)
    return (name, marks_dict[name])

# -------------------------
# Task 4: Grade assignment
# -------------------------
def assign_grade(score: float) -> str:
    """Assign letter grade from numeric score."""
    # A: 90+, B: 80–89, C: 70–79, D: 60–69, F: <60
    try:
        s = float(score)
    except Exception:
        return "F"
    if s >= 90:
        return "A"
    elif s >= 80:
        return "B"
    elif s >= 70:
        return "C"
    elif s >= 60:
        return "D"
    else:
        return "F"

def assign_grades(marks_dict: Dict[str, float]) -> Dict[str, str]:
    """Return a new dict mapping student -> letter grade."""
    return {name: assign_grade(score) for name, score in marks_dict.items()}

def grade_distribution(grades: Dict[str, str]) -> Dict[str, int]:
    """Count number of students per grade A-F."""
    distribution = {g: 0 for g in ["A", "B", "C", "D", "F"]}
    for grade in grades.values():
        if grade in distribution:
            distribution[grade] += 1
        else:
            # unexpected grade label fallback
            distribution.setdefault(grade, 0)
            distribution[grade] += 1
    return distribution

# -------------------------
# Task 5: Pass/Fail list comprehension
# -------------------------
def passed_failed_lists(marks_dict: Dict[str, float], pass_mark: float = 40.0) -> Tuple[List[str], List[str]]:
    """Return (passed_students, failed_students) lists of names using list comprehensions."""
    passed_students = [name for name, score in marks_dict.items() if score >= pass_mark]
    failed_students = [name for name, score in marks_dict.items() if score < pass_mark]
    return passed_students, failed_students

# -------------------------
# Task 2: Data entry / CSV import
# -------------------------
def read_from_csv(file_path: str) -> Dict[str, float]:
    """
    Read student name and mark pairs from CSV.
    Expected CSV columns: name,marks  (header optional)
    """
    marks = {}
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            # allow header row detection (if 'name' or 'marks' present)
            first = row[0].strip().lower()
            if first in ("name", "student", "student name"):
                continue
            # support rows like "Alice,78" or "Alice, 78"
            try:
                name = row[0].strip()
                score = float(row[1].strip())
            except Exception:
                # skip malformed rows
                continue
            marks[name] = score
    return marks

def manual_entry() -> Dict[str, float]:
    """Prompt user for manual entry of names and marks. Stop when blank name entered."""
    print("\nEnter student details. Leave name blank and press Enter to finish.")
    marks = {}
    while True:
        name = input("Student name: ").strip()
        if name == "":
            break
        raw_score = input(f"Mark for {name}: ").strip()
        try:
            score = float(raw_score)
            if score < 0:
                print("Warning: negative mark entered; storing as-is.")
        except ValueError:
            print("Invalid mark. Please enter a number. Skipping this student.")
            continue
        marks[name] = score
    return marks

# -------------------------
# Task 6: Table print, CSV export, and CLI loop
# -------------------------
def print_results_table(marks_dict: Dict[str, float], grades: Dict[str, str]) -> None:
    """Prints formatted Name | Marks | Grade table."""
    if not marks_dict:
        print("\nNo student data to display.\n")
        return
    name_w = max(len(name) for name in marks_dict.keys()) + 2
    print("\nName".ljust(name_w) + "Marks".ljust(8) + "Grade")
    print("-" * (name_w + 8 + 6))
    for name, score in marks_dict.items():
        print(f"{name.ljust(name_w)}{str(score).ljust(8)}{grades.get(name,'')}")
    print()  # blank line

def export_to_csv(marks_dict: Dict[str, float], grades: Dict[str, str], filename: str = "grades_output.csv") -> None:
    """Export final grade table to CSV with header: name,marks,grade"""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "marks", "grade"])
        for name, score in marks_dict.items():
            writer.writerow([name, score, grades.get(name, "")])
    print(f"Grades exported to {filename}")

def analyze_and_report(marks: Dict[str, float]) -> None:
    """Run full analysis pipeline on marks dict and print results."""
    if not marks:
        print("No data provided for analysis.")
        return

    avg = calculate_average(marks)
    med = calculate_median(marks)
    max_name, max_score = find_max_score(marks)
    min_name, min_score = find_min_score(marks)

    grades = assign_grades(marks)
    distribution = grade_distribution(grades)
    passed, failed = passed_failed_lists(marks, pass_mark=40.0)

    # Print summary
    print("\nANALYSIS SUMMARY")
    print(f"Total students: {len(marks)}")
    print(f"Average (mean): {avg:.2f}")
    print(f"Median: {med:.2f}")
    print(f"Highest score: {max_score} ({max_name})")
    print(f"Lowest score: {min_score} ({min_name})")
    print("\nGrade distribution:")
    for g in ["A", "B", "C", "D", "F"]:
        print(f"  {g}: {distribution.get(g, 0)}")

    print(f"\nPassed students ({len(passed)}): {', '.join(passed) if passed else 'None'}")
    print(f"Failed students ({len(failed)}): {', '.join(failed) if failed else 'None'}")

    # Results table
    print_results_table(marks, grades)

    # Ask about CSV export (bonus)
    choice = input("Export results to CSV? (y/N): ").strip().lower()
    if choice == "y":
        fname = input("Enter output filename [grades_output.csv]: ").strip() or "grades_output.csv"
        export_to_csv(marks, grades, fname)
    print("Analysis complete.\n")

def main_menu_loop() -> None:
    """Main CLI loop allowing repeated analyses."""
    print("Welcome to GradeBook Analyzer")
    while True:
        print("\nMenu:")
        print("  1) Manual entry of student marks")
        print("  2) Load marks from CSV file")
        print("  3) Exit")
        choice = input("Choose an option (1/2/3): ").strip()
        if choice == "1":
            marks = manual_entry()
            analyze_and_report(marks)
        elif choice == "2":
            path = input("Enter CSV file path (name,marks): ").strip()
            try:
                marks = read_from_csv(path)
                if not marks:
                    print("No valid rows found in CSV.")
                analyze_and_report(marks)
            except FileNotFoundError as fe:
                print(fe)
            except Exception as e:
                print("Error reading CSV:", e)
        elif choice == "3":
            print("Exiting GradeBook Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main_menu_loop()
