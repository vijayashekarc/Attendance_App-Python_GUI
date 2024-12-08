import tkinter as tk
from tkinter import messagebox
import csv
from datetime import date

today = date.today().strftime("%d-%m-%y")

f = open("attendance.csv", "r")
stu = list(csv.reader(f))

ff = open("CSE_A04_" + today + ".csv", "a")
ff.write("Name,Reg_NO,Attendance\n")

pre, ab = 0, 0
current_student = 0

def mark_attendance(attendance):
    global pre, current_student
    stu_name = stu[current_student][2]
    stu_reg = stu[current_student][1]
    ff.write(f"{stu_name},{stu_reg},{attendance}\n")
    if attendance == 'P':
        pre += 1

    current_student += 1

    if current_student < len(stu):
        name_label.config(text=stu[current_student][2])
    else:
        ff.close()
        messagebox.showinfo("Attendance", f"Attendance on {today}\nTotal: {len(stu)}\nPresent: {pre}\nAbsent: {len(stu) - pre}")
        root.destroy()


root = tk.Tk()
root.title("Attendance System")

name_label = tk.Label(root, text=stu[current_student][2], font=("Arial", 36))
name_label.pack(pady=20)

present_button = tk.Button(root, text="Present", font=("Arial", 18), width=10, command=lambda: mark_attendance(' '))
present_button.pack(pady=10)

absent_button = tk.Button(root, text="Absent", font=("Arial", 18), width=10, command=lambda: mark_attendance('A'))
absent_button.pack(pady=10)

root.mainloop()
