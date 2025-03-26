import tkinter as tk
from tkinter import messagebox, simpledialog
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hospital Management System")
        self.geometry("600x400")
        # Initialize with same data as in Main.py
        self.admin = Admin('admin', '123', 'B1 1AB')
        self.doctors = [
            Doctor('John', 'Smith', 'Internal Med.'),
            Doctor('Jone', 'Smith', 'Pediatrics'),
            Doctor('Jone', 'Carlos', 'Cardiology')
        ]
        self.patients = [
            Patient('Sara', 'Smith', 20, '07012345678', 'B1 234', ['Cough', 'Fever']),
            Patient('Mike', 'Jones', 37, '07555551234', 'L2 2AB', ['Headache']),
            Patient('David', 'Smith', 15, '07123456789', 'C1 ABC', ['Cough'])
        ]
        self.discharged_patients = []
        self.current_frame = None
        self.show_login()

    def show_login(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = LoginFrame(self)
        self.current_frame.pack(fill="both", expand=True)

    def show_main_menu(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = MainMenuFrame(self)
        self.current_frame.pack(fill="both", expand=True)

class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Admin Login", font=("Arial", 16)).pack(pady=20)
        
        tk.Label(self, text="Username").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()
        
        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()
        
        tk.Button(self, text="Login", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # For GUI login, check against the known credentials.
        if username == "admin" and password == "123":
            messagebox.showinfo("Success", "Login successful!")
            self.master.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

class MainMenuFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Main Menu", font=("Arial", 16)).pack(pady=20)
        
        # Create buttons for different operations.
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Manage Doctors", width=25, command=self.manage_doctors).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Manage Patients", width=25, command=self.manage_patients).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Assign Doctor to Patient", width=25, command=self.assign_doctor_to_patient).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Discharge Patient", width=25, command=self.discharge_patient).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="View Management Report", width=25, command=self.view_management_report).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Quit", width=25, command=self.quit_app).grid(row=2, column=1, padx=5, pady=5)

    def manage_doctors(self):
        DoctorManagementWindow(self.master)

    def manage_patients(self):
        PatientManagementWindow(self.master)

    def assign_doctor_to_patient(self):
        AssignDoctorWindow(self.master)

    def discharge_patient(self):
        DischargePatientWindow(self.master)

    def view_management_report(self):
        # This will call the management_report method from Admin,
        # which shows matplotlib charts as in your original code.
        self.master.admin.management_report(self.master.doctors, self.master.patients, self.master.discharged_patients)

    def quit_app(self):
        self.master.destroy()

class DoctorManagementWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Doctor Management")
        self.geometry("400x300")
        self.admin = master.admin
        self.doctors = master.doctors
        
        tk.Label(self, text="Doctor Management", font=("Arial", 14)).pack(pady=10)
        self.doctor_listbox = tk.Listbox(self, width=50)
        self.doctor_listbox.pack(pady=10)
        self.refresh_doctor_list()
        
        tk.Button(self, text="Register Doctor", command=self.register_doctor).pack(pady=5)
        tk.Button(self, text="Delete Selected Doctor", command=self.delete_doctor).pack(pady=5)

    def refresh_doctor_list(self):
        self.doctor_listbox.delete(0, tk.END)
        for index, doctor in enumerate(self.doctors):
            self.doctor_listbox.insert(tk.END, f"{index+1}. {doctor.full_name()} - {doctor.get_speciality()}")

    def register_doctor(self):
        first_name = simpledialog.askstring("Input", "Enter doctor's first name:", parent=self)
        if not first_name: return
        surname = simpledialog.askstring("Input", "Enter doctor's surname:", parent=self)
        if not surname: return
        speciality = simpledialog.askstring("Input", "Enter doctor's speciality:", parent=self)
        if not speciality: return
        # Check if doctor already exists
        for d in self.doctors:
            if d.get_first_name() == first_name and d.get_surname() == surname:
                messagebox.showerror("Error", "Doctor already registered.")
                return
        new_doctor = Doctor(first_name, surname, speciality)
        self.doctors.append(new_doctor)
        messagebox.showinfo("Success", "Doctor registered successfully.")
        self.refresh_doctor_list()

    def delete_doctor(self):
        selected = self.doctor_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Please select a doctor to delete.")
            return
        index = selected[0]
        del self.doctors[index]
        messagebox.showinfo("Success", "Doctor deleted successfully.")
        self.refresh_doctor_list()

class PatientManagementWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Patient Management")
        self.geometry("500x400")
        self.admin = master.admin
        self.patients = master.patients
        
        tk.Label(self, text="Patient Management", font=("Arial", 14)).pack(pady=10)
        self.patient_listbox = tk.Listbox(self, width=70)
        self.patient_listbox.pack(pady=10)
        self.refresh_patient_list()
        
        tk.Button(self, text="Register Patient", command=self.register_patient).pack(pady=5)
        tk.Button(self, text="Delete Selected Patient", command=self.delete_patient).pack(pady=5)

    def refresh_patient_list(self):
        self.patient_listbox.delete(0, tk.END)
        for index, patient in enumerate(self.patients):
            self.patient_listbox.insert(tk.END, f"{index+1}. {patient.full_name()} - Age: {patient.get_age()}")

    def register_patient(self):
        first_name = simpledialog.askstring("Input", "Enter patient's first name:", parent=self)
        if not first_name: return
        surname = simpledialog.askstring("Input", "Enter patient's surname:", parent=self)
        if not surname: return
        age = simpledialog.askinteger("Input", "Enter patient's age:", parent=self)
        if age is None: return
        mobile = simpledialog.askstring("Input", "Enter patient's mobile:", parent=self)
        if not mobile: return
        postcode = simpledialog.askstring("Input", "Enter patient's postcode:", parent=self)
        if not postcode: return
        symptoms_str = simpledialog.askstring("Input", "Enter patient's symptoms (comma separated):", parent=self)
        symptoms = [s.strip() for s in symptoms_str.split(',')] if symptoms_str else []
        new_patient = Patient(first_name, surname, age, mobile, postcode, symptoms)
        self.patients.append(new_patient)
        messagebox.showinfo("Success", "Patient registered successfully.")
        self.refresh_patient_list()

    def delete_patient(self):
        selected = self.patient_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Please select a patient to delete.")
            return
        index = selected[0]
        del self.patients[index]
        messagebox.showinfo("Success", "Patient deleted successfully.")
        self.refresh_patient_list()

class AssignDoctorWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Assign Doctor to Patient")
        self.geometry("500x400")
        self.doctors = master.doctors
        self.patients = master.patients
        
        tk.Label(self, text="Assign Doctor to Patient", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(self, text="Select Patient:").pack()
        self.patient_listbox = tk.Listbox(self, width=70)
        self.patient_listbox.pack(pady=5)
        for index, patient in enumerate(self.patients):
            self.patient_listbox.insert(tk.END, f"{index+1}. {patient.full_name()}")
            
        tk.Label(self, text="Select Doctor:").pack()
        self.doctor_listbox = tk.Listbox(self, width=70)
        self.doctor_listbox.pack(pady=5)
        for index, doctor in enumerate(self.doctors):
            self.doctor_listbox.insert(tk.END, f"{index+1}. {doctor.full_name()} - {doctor.get_speciality()}")
            
        tk.Button(self, text="Assign", command=self.assign).pack(pady=10)
 
    def assign(self):
        patient_sel = self.patient_listbox.curselection()
        doctor_sel = self.doctor_listbox.curselection()
        if not patient_sel or not doctor_sel:
            messagebox.showerror("Error", "Please select both a patient and a doctor.")
            return
        patient_index = patient_sel[0]
        doctor_index = doctor_sel[0]
        patient = self.patients[patient_index]
        doctor = self.doctors[doctor_index]
        patient.link(doctor.full_name())
        doctor.add_patient(patient)
        messagebox.showinfo("Success", f"Doctor {doctor.full_name()} assigned to {patient.full_name()} successfully.")

class DischargePatientWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Discharge Patient")
        self.geometry("500x400")
        self.master_app = master
        tk.Label(self, text="Discharge Patient", font=("Arial", 14)).pack(pady=10)
        self.patient_listbox = tk.Listbox(self, width=70)
        self.patient_listbox.pack(pady=10)
        self.refresh_patient_list()
        tk.Button(self, text="Discharge Selected Patient", command=self.discharge).pack(pady=10)

    def refresh_patient_list(self):
        self.patient_listbox.delete(0, tk.END)
        for index, patient in enumerate(self.master_app.patients):
            self.patient_listbox.insert(tk.END, f"{index+1}. {patient.full_name()}")

    def discharge(self):
        selected = self.patient_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Please select a patient to discharge.")
            return
        index = selected[0]
        patient = self.master_app.patients.pop(index)
        self.master_app.discharged_patients.append(patient)
        messagebox.showinfo("Success", f"Patient {patient.full_name()} discharged successfully.")
        self.refresh_patient_list()

if __name__ == '__main__':
    app = App()
    app.mainloop()
