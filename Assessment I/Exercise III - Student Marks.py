import tkinter as tk
from tkinter import ttk, messagebox

def load_students(filename):
    students = []
    try:
        with open(filename, "r") as file:
            student_count = int(file.readline().strip())
            for line in file:
                data = line.strip().split(",")
                student_id = data[0]
                name = data[1]
                coursework = list(map(int, data[2:5]))
                exam_mark = int(data[5])
                total_coursework = sum(coursework)
                total_score = total_coursework + exam_mark
                percentage = (total_score / 160) * 100
                if percentage >= 70:
                    grade = "A"
                elif percentage >= 60:
                    grade = "B"
                elif percentage >= 50:
                    grade = "C"
                elif percentage >= 40:
                    grade = "D"
                else:
                    grade = "F"
                students.append({
                    "id": student_id,
                    "name": name,
                    "coursework": total_coursework,
                    "exam": exam_mark,
                    "total": total_score,
                    "percentage": percentage,
                    "grade": grade,
                })
        return students
    except FileNotFoundError:
        messagebox.showerror("Error", "studentMarks.txt file not found!")
        return []

def format_student(student):
    return (
        f"Name: {student['name']}\n"
        f"Number: {student['id']}\n"
        f"Coursework Total: {student['coursework']}\n"
        f"Exam Mark: {student['exam']}\n"
        f"Overall Percentage: {student['percentage']:.2f}%\n"
        f"Grade: {student['grade']}\n"
    )

def show_all_students():
    output_box.delete(1.0, tk.END)
    total = 0
    for s in students:
        output_box.insert(tk.END, format_student(s) + "\n")
        total += s['percentage']
    avg = total / len(students)
    output_box.insert(tk.END, f"Total Students: {len(students)}\n")
    output_box.insert(tk.END, f"Average Percentage: {avg:.2f}%\n")

def show_highest():
    highest = max(students, key=lambda s: s['total'])
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, "Highest Scoring Student:\n\n")
    output_box.insert(tk.END, format_student(highest))

def show_lowest():
    lowest = min(students, key=lambda s: s['total'])
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, "Lowest Scoring Student:\n\n")
    output_box.insert(tk.END, format_student(lowest))

def show_individual():
    selected = student_dropdown.get()
    if not selected:
        messagebox.showwarning("Warning", "Please select a student.")
        return
    student = next(s for s in students if f"{s['name']} ({s['id']})" == selected)
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, format_student(student))

students = load_students("studentMarks.txt")

root = tk.Tk()
root.title("Student Manager")
root.geometry("900x600")
root.config(bg="#e8eff6")

title_label = tk.Label(
    root,
    text="Student Manager",
    font=("Arial", 22, "bold"),
    bg="#e8eff6"
)
title_label.pack(pady=20)

button_frame = tk.Frame(root, bg="#e8eff6")
button_frame.pack(pady=10)

btn_all = tk.Button(
    button_frame,
    text="View All Student Records",
    width=22,
    command=show_all_students,
    font=("Arial", 12),
)
btn_all.grid(row=0, column=0, padx=10)

btn_high = tk.Button(
    button_frame,
    text="Show Highest Score",
    width=22,
    command=show_highest,
    font=("Arial", 12),
)
btn_high.grid(row=0, column=1, padx=10)

btn_low = tk.Button(
    button_frame,
    text="Show Lowest Score",
    width=22,
    command=show_lowest,
    font=("Arial", 12),
)
btn_low.grid(row=0, column=2, padx=10)

dropdown_frame = tk.Frame(root, bg="#e8eff6")
dropdown_frame.pack(pady=20)

lbl = tk.Label(
    dropdown_frame,
    text="View Individual Student Record:",
    font=("Arial", 12),
    bg="#e8eff6",
)
lbl.grid(row=0, column=0, padx=5)

student_dropdown = ttk.Combobox(
    dropdown_frame,
    width=40,
    values=[f"{s['name']} ({s['id']})" for s in students],
)
student_dropdown.grid(row=0, column=1, padx=5)

btn_view = tk.Button(
    dropdown_frame,
    text="View Record",
    command=show_individual,
    width=15,
    font=("Arial", 12),
)
btn_view.grid(row=0, column=2, padx=5)

output_box = tk.Text(root, width=100, height=20, font=("Consolas", 10))
output_box.pack(pady=10)

root.mainloop()
