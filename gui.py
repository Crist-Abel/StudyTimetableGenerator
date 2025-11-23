import tkinter as tk
from tkinter import messagebox
from analytics import Analyzer
from optimizer import Optimizer


def run_timetable():
    subjects_input = entry_subjects.get()
    difficulties_input = entry_difficulties.get()
    hours_input = entry_hours.get()

    if not subjects_input or not difficulties_input or not hours_input:
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        subjects = [s.strip() for s in subjects_input.split(",")]
        difficulties = [int(x.strip()) for x in difficulties_input.split(",")]
        total_hours = float(hours_input)
    except:
        messagebox.showerror("Error", "Invalid input! Check difficulties and hours.")
        return

    if len(subjects) != len(difficulties):
        messagebox.showerror("Error", "Subjects and difficulties count must match.")
        return

    data = {"subjects": subjects, "difficulties": difficulties}
    analyzer = Analyzer(data)
    optimizer = Optimizer(analyzer)

    result = optimizer.run(total_hours)

    output_text.delete("1.0", tk.END)
    for subject, time in result.items():
        output_text.insert(tk.END, f"{subject}: {time:.2f} hours\n")


root = tk.Tk()
root.title("Study Timetable Generator")
root.geometry("430x400")
root.resizable(False, False)

tk.Label(root, text="Subjects (comma-separated):", font=("Arial", 11)).pack()
entry_subjects = tk.Entry(root, width=50)
entry_subjects.pack(pady=5)

tk.Label(root, text="Difficulty (comma-separated, e.g. 5,3,2):", font=("Arial", 11)).pack()
entry_difficulties = tk.Entry(root, width=50)
entry_difficulties.pack(pady=5)

tk.Label(root, text="Total Hours Available:", font=("Arial", 11)).pack()
entry_hours = tk.Entry(root, width=20)
entry_hours.pack(pady=5)

tk.Button(root, text="Generate Timetable", command=run_timetable, width=25, height=2, bg="#4CAF50", fg="white").pack(pady=10)

output_text = tk.Text(root, width=50, height=10, font=("Arial", 10))
output_text.pack(pady=5)

root.mainloop()
