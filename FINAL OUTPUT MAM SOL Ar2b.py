import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# =========================
# MAIN WINDOW
# =========================
root = tk.Tk()
root.title("Student Management System")
root.geometry("700x500")
root.configure(bg="#E8EAF6")


# =========================
# COLORS
# =========================
BG_COLOR = "#E8EAF6"
TITLE_COLOR = "#3949AB"
LABEL_COLOR = "#5C6BC0"
ENTRY_BGN = "#FFFFFF"

ADD_COLOR = "#43A047"
UPDATE_COLOR = "#1E88E5"
DELETE_COLOR = "#E53935"
CLEAR_COLOR = "#757575"

BUTTON_NEXT = "white"
BUTTON_ACTIVE = "#E8EAF6"


# =========================
# FUNCTIONS
# =========================

def add_student():
    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()

    if name == "" or age == "" or course == "":
        messagebox.showwarning(
            "Warning",
            "Please fill in all fields."
        )
        return

    tree.insert(
        "",
        tk.END,
        values=(len(tree.get_children()) + 1, name, age, course)
    )

    clear_fields()

    messagebox.showinfo(
        "Success",
        "Student added successfully!"
    )


def update_student():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a student to update."
        )
        return

    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()

    if name == "" or age == "" or course == "":
        messagebox.showwarning(
            "Warning",
            "Please fill in all fields."
        )
        return

    item = tree.item(selected[0])
    student_id = item["values"][0]

    tree.item(
        selected[0],
        values=(student_id, name, age, course)
    )

    clear_fields()

    messagebox.showinfo(
        "Success",
        "Student updated successfully!"
    )


def delete_student():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a student to delete."
        )
        return

    tree.delete(selected[0])

    clear_fields()

    messagebox.showinfo(
        "Success",
        "Student deleted successfully!"
    )


def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)


# =========================
# TITLE
# =========================
title_label = tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 18, "bold"),
    bg=BG_COLOR,
    fg=TITLE_COLOR
)

title_label.pack(pady=10)


# =========================
# INPUT FRAME
# =========================
input_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

input_frame.pack(pady=10)


# =========================
# NAME
# =========================
tk.Label(
    input_frame,
    text="Name:",
    bg=BG_COLOR,
    fg=LABEL_COLOR
).grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)

name_entry = tk.Entry(
    input_frame,
    width=30,
    bg=ENTRY_BGN
)

name_entry.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)


# =========================
# AGE
# =========================
tk.Label(
    input_frame,
    text="Age:",
    bg=BG_COLOR,
    fg=LABEL_COLOR
).grid(
    row=1,
    column=0,
    padx=5,
    pady=5
)

age_entry = tk.Entry(
    input_frame,
    width=30,
    bg=ENTRY_BGN
)

age_entry.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)


# =========================
# COURSE
# =========================
tk.Label(
    input_frame,
    text="Course:",
    bg=BG_COLOR,
    fg=LABEL_COLOR
).grid(
    row=2,
    column=0,
    padx=5,
    pady=5
)

course_entry = tk.Entry(
    input_frame,
    width=30,
    bg=ENTRY_BGN
)

course_entry.grid(
    row=2,
    column=1,
    padx=5,
    pady=5
)


# =========================
# BUTTON FRAME
# =========================
button_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

button_frame.pack(pady=10)


# =========================
# ADD BUTTON
# =========================
tk.Button(
    button_frame,
    text="Add",
    width=10,
    bg=ADD_COLOR,
    fg=BUTTON_NEXT,
    activebackground=BUTTON_ACTIVE,
    activeforeground="black",
    command=add_student
).grid(
    row=0,
    column=0,
    padx=5
)


# =========================
# UPDATE BUTTON
# =========================
tk.Button(
    button_frame,
    text="Update",
    width=10,
    bg=UPDATE_COLOR,
    fg=BUTTON_NEXT,
    activebackground=BUTTON_ACTIVE,
    activeforeground="black",
    command=update_student
).grid(
    row=0,
    column=1,
    padx=5
)


# =========================
# DELETE BUTTON
# =========================
tk.Button(
    button_frame,
    text="Delete",
    width=10,
    bg=DELETE_COLOR,
    fg=BUTTON_NEXT,
    activebackground=BUTTON_ACTIVE,
    activeforeground="black",
    command=delete_student
).grid(
    row=0,
    column=2,
    padx=5
)


# =========================
# CLEAR BUTTON
# =========================
tk.Button(
    button_frame,
    text="Clear",
    width=10,
    bg=CLEAR_COLOR,
    fg=BUTTON_NEXT,
    activebackground=BUTTON_ACTIVE,
    activeforeground="black",
    command=clear_fields
).grid(
    row=0,
    column=3,
    padx=5
)


# =========================
# TABLE
# =========================
tree = ttk.Treeview(
    root,
    columns=("ID", "Name", "Age", "Course"),
    show="headings"
)

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Course", text="Course")

tree.column("ID", width=50)
tree.column("Name", width=200)
tree.column("Age", width=80)
tree.column("Course", width=200)

tree.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# =========================
# RUN PROGRAM
# =========================
root.mainloop()
