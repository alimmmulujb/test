import tkinter as tk

class StudentForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("teacher")

        self.records = []

     
        tk.Label(self, text='Fname:').grid(row=0, column=0, sticky='w')
        self.entry_fname = tk.Entry(self)
        self.entry_fname.grid(row=0, column=1)

        tk.Label(self, text='Lname:').grid(row=0, column=2, sticky='w')
        self.entry_lname = tk.Entry(self)
        self.entry_lname.grid(row=0, column=3)


        gender_frame = tk.LabelFrame(self, text="Gender")
        gender_frame.grid(row=1, column=0, columnspan=4, sticky='w', padx=5, pady=5)

        self.gender_var = tk.StringVar()
        self.gender_var.set('male')
        tk.Radiobutton(gender_frame, text='Male', variable=self.gender_var, value='male').grid(row=0, column=0, padx=10, pady=5)
        tk.Radiobutton(gender_frame, text='Female', variable=self.gender_var, value='female').grid(row=0, column=1, padx=10, pady=5)

        courses_frame = tk.LabelFrame(self, text="Courses")
        courses_frame.grid(row=2, column=0, columnspan=4, sticky='w', padx=5, pady=5)

        self.course_python_var = tk.BooleanVar()
        self.course_csharp_var = tk.BooleanVar()
        self.course_java_var = tk.BooleanVar()

        tk.Checkbutton(courses_frame, text='Python', variable=self.course_python_var).grid(row=0, column=0, padx=10, pady=5)
        tk.Checkbutton(courses_frame, text='C#', variable=self.course_csharp_var).grid(row=0, column=1, padx=10, pady=5)
        tk.Checkbutton(courses_frame, text='Java', variable=self.course_java_var).grid(row=0, column=2, padx=10, pady=5)


        self.submit_btn = tk.Button(self, text='Submit', command=self.submit)
        self.submit_btn.grid(row=3, column=1, pady=10)

        self.listbox = tk.Listbox(self, width=70)
        self.listbox.grid(row=4, column=0, columnspan=4, pady=10)

    def submit(self):
        fname = self.entry_fname.get()
        lname = self.entry_lname.get()
        gender = self.gender_var.get()
        courses = []
        if self.course_python_var.get():
            courses.append('Python')
        if self.course_csharp_var.get():
            courses.append('C#')
        if self.course_java_var.get():
            courses.append('Java')

        record = f"{fname}, {lname}, {gender}, {', '.join(courses)}"
        self.records.append(record)
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for idx, rec in enumerate(self.records, 1):
            self.listbox.insert(tk.END, f"{idx} - {rec}")

if __name__ == "__main__":
    app = StudentForm()
    app.mainloop()
