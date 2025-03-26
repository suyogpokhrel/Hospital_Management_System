from Doctor import Doctor
from Patient import Patient
import matplotlib
import matplotlib.pyplot as plt

class Admin:
    # A class that deals with the Admin operations
    def __init__(self, username, password, address=''):
        self.__username = username
        self.__password = password
        self.__address = address

    def view(self, a_list):
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self):
        # Handles admin login
        print("-----Login-----")
        username = input('Enter the username: ')
        password = input('Enter the password: ')

        if username == self.__username and password == self.__password:
            print("Login successful!")
            return username
        else:
            raise Exception("Invalid username or password.")

    def find_index(self, index, items):
        if 0 <= index < len(items):
            return items[index]
        else:
            return None

    def view_patient(self, patients):
        # Displays list of patients
        print("-----View Patients-----")
        print(' ID|     Full Name      | Doctor`s Full Name | Age |    Mobile     | Postcode | Family ID|           Symptoms   ')
        self.view(patients)

    def view_discharge(self, discharged_patients):
        # Displays list of discharged patients
        print("-----View Discharged Patients-----")
        if discharged_patients:
            print(' ID|     Full Name      | Doctor`s Full Name | Age |    Mobile     | Postcode | Family ID|           Symptoms   ')
            self.view(discharged_patients)
        else:
            print("No discharged patients to display.")

    def discharge(self, patients, discharged_patients):
        # Discharges a patient
        print("-----Discharge Patient-----")
        print(' ID|     Full Name      | Doctor`s Full Name | Age |    Mobile     | Postcode | Family ID|           Symptoms   ')
        self.view(patients)
        try:
            patient_index = int(input("Enter patient ID to discharge: ")) - 1
            patient = self.find_index(patient_index, patients)

            if patient:
                discharged_patients.append(patients.pop(patient_index))
                print(f"Patient {patient.full_name()} discharged successfully.")
            else:
                print("Invalid patient ID.")

        except ValueError:
            print("Invalid input. Please enter a valid patient ID.")

    def assign_doctor_to_patient(self, patients, doctors):
        # Assigns a doctor to a patient
        print("-----Assign Doctor to Patient-----")
        print(' ID|     Full Name      | Doctor`s Full Name | Age |    Mobile     | Postcode | Family ID|           Symptoms   ')
        self.view(patients)
        try:
            patient_index = int(input("Enter patient ID: ")) - 1
            patient = self.find_index(patient_index, patients)

            if not patient:
                print("Invalid patient ID.")
                return

            print(' ID|          Full name           |  Speciality')
            self.view(doctors)
            doctor_index = int(input("Enter doctor ID: ")) - 1
            doctor = self.find_index(doctor_index, doctors)

            if doctor:
                patient.link(doctor.full_name())
                doctor.add_patient(patient)
                print(f"Doctor {doctor.full_name()} assigned to {patient.full_name()} successfully.")
            else:
                print("Invalid doctor ID.")

        except ValueError:
            print("Invalid input. Please enter a valid ID.")

    def get_doctor_details(self):
        first_name = input("Enter doctor's first name: ")
        surname = input("Enter doctor's surname: ")
        speciality = input("Enter doctor's speciality: ")
        return first_name, surname, speciality

    def doctor_management(self, doctors):
        print("-----Doctor Management-----")
        op = input("Choose the operation (1 - Register, 2 - View, 3 - Update, 4 - Delete): ")

        if op == '1':
            print("-----Register-----")
            first_name, surname, speciality = self.get_doctor_details()

            if any(d.get_first_name() == first_name and d.get_surname() == surname for d in doctors):
                print("Doctor already registered.")
                return

            doctors.append(Doctor(first_name, surname, speciality))
            print("Doctor registered successfully.")

        elif op == '2':
            print("-----List of Doctors-----")
            print(' ID|          Full name           |  Speciality')
            self.view(doctors)

        elif op == '3':
            print("-----Update Doctor's Details-----")
            print(' ID|          Full name           |  Speciality')
            self.view(doctors)
            try:
                index = int(input('Enter the ID of the doctor: ')) - 1
                doctor = self.find_index(index, doctors)

                if doctor:
                    print('Choose the field to be updated:')
                    print(' 1 First name')
                    print(' 2 Surname')
                    print(' 3 Speciality')

                    op = input('Input: ')

                    if op == '1':
                        new_first_name = input('Enter new first name: ')
                        doctor.set_first_name(new_first_name)
                        print("Doctor's first name updated successfully.")

                    elif op == '2':
                        new_surname = input('Enter new surname: ')
                        doctor.set_surname(new_surname)
                        print("Doctor's surname updated successfully.")

                    elif op == '3':
                        new_speciality = input('Enter new speciality: ')
                        doctor.set_speciality(new_speciality)
                        print("Doctor's speciality updated successfully.")

                    else:
                        print("Invalid option selected.")
                else:
                    print("Doctor not found.")

            except ValueError:
                print('The ID entered is incorrect')

        elif op == '4':
            print("-----Delete Doctor-----")
            print(' ID|          Full name           |  Speciality')
            self.view(doctors)
            doctor_index = int(input("Enter the ID of the doctor to delete: ")) - 1

            if self.find_index(doctor_index, doctors):
                del doctors[doctor_index]
                print("Doctor deleted successfully.")
            else:
                print("Doctor not found.")

    def patient_management(self, patients):
        print("-----Patient Management-----")
        op = input("Choose the operation (1 - Register, 2 - View, 3 - Update, 4 - Delete): ")

        if op == '1':
            first_name = input("Enter patient's first name: ")
            surname = input("Enter patient's surname: ")
            age = int(input("Enter patient's age: "))
            mobile = input("Enter patient's mobile: ")
            postcode = input("Enter patient's postcode: ")
            symptoms = input("Enter patient's symptoms (comma separated): ").split(',')

            patients.append(Patient(first_name, surname, age, mobile, postcode, symptoms))
            print("Patient registered successfully.")

        elif op == '2':
            print("-----View Patients-----")
            print(' ID|     Full Name      | Doctor`s Full Name | Age |    Mobile     | Postcode | Family ID|           Symptoms   ')
            self.view(patients)

        elif op == '3':
            print("-----Update Patients-----")
            print(' ID|     Full Name      | Doctor`s Full Name | Age |    Mobile     | Postcode | Family ID|           Symptoms   ')
            self.view(patients)
            index = int(input('Enter the ID of the patient: ')) - 1
            patient = self.find_index(index, patients)

            if patient:
                print('Choose the field to be updated:')
                print(' 1 First name')
                print(' 2 Surname')
                print(' 3 Age')
                print(' 4 Mobile')
                print(' 5 Postcode')
                print(' 6 Symptoms')

                op = input('Input: ')

                if op == '1':
                    new_first_name = input('Enter new first name: ')
                    patient.set_first_name(new_first_name)
                elif op == '2':
                    new_surname = input('Enter new surname: ')
                    patient.set_surname(new_surname)
                elif op == '3':
                    new_age = input('Enter new age: ')
                    patient.set_age(new_age)
                elif op == '4':
                    new_mobile = input('Enter new mobile: ')
                    patient.set_mobile(new_mobile)
                elif op == '5':
                    new_postcode = input('Enter new postcode: ')
                    patient.set_postcode(new_postcode)
                elif op == '6':
                    new_symptoms = input('Enter new symptoms (comma separated): ').split(',')
                    patient.update_symptoms(new_symptoms)
                else:
                    print("Invalid option selected.")

                print("Patient details updated successfully.")

            else:
                print("Patient not found.")

        elif op == '4':
            print("-----Delete Patients-----")
            print(' ID|     Full Name      | Doctor`s Full Name | Age |    Mobile     | Postcode | Family ID|           Symptoms   ')
            self.view(patients)
            while True:
                try:
                    patient_index = int(input("Enter the ID of the patient to delete: ")) - 1
                    if 0 <= patient_index < len(patients):
                        break
                    else:
                        print("Invalid ID. Please enter a valid patient ID from the list.")
                except ValueError:
                    print("Invalid input. Please enter a numeric ID.")

            if self.find_index(patient_index, patients):
                del patients[patient_index]
                print("Patient deleted successfully.")
            else:
                print("Patient not found.")


    def relocating_doctor(self, patients, doctors):
        print("-----Relocate Doctor to Patient-----")
        print(' ID|     Full Name      | Doctor`s Full Name | Age |    Mobile     | Postcode | Family ID|           Symptoms   ')
        self.view(patients)
        patient_index = int(input("Enter patient ID: ")) - 1
        patient = self.find_index(patient_index, patients)

        if not patient:
            print("Invalid patient ID.")
            return

        print(' ID|          Full name           |  Speciality')
        self.view(doctors)
        doctor_index = int(input("Enter new doctor ID: ")) - 1
        doctor = self.find_index(doctor_index, doctors)

        if doctor:
            patient.link(doctor.full_name())
            doctor.add_patient(patient)
            print("Doctor relocated successfully.")
        else:
            print("Invalid doctor ID.")

    def assign_family_id(self, patients):
        print("-----Assign Family ID-----")
        print(' ID|     Full Name      | Doctor`s Full Name | Age |    Mobile     | Postcode | Family ID|           Symptoms   ')
        self.view(patients)
        family_id = input("Enter Family ID: ")
        surname = input("Enter the surname to assign Family ID to: ")

        for patient in patients:
            if patient.get_surname() == surname:
                patient.set_family_id(family_id)
                print(f"Assigned Family ID {family_id} to {patient.full_name()}.")

    def group_by_family_id(self, patients):
        print("-----Patients Grouped by Family ID-----")
        family_groups = {}
        for patient in patients:
            family_id = patient.get_family_id()
            if family_id:
                family_groups.setdefault(family_id, []).append(patient)

        for family_id, members in family_groups.items():
            print(f"Family ID {family_id}: {', '.join(p.full_name() for p in members)}")

    def group_by_symptoms(self, patients):
        print("-----Patients Grouped by Symptoms-----")
        symptom_groups = {}
        for patient in patients:
            for symptom in patient.get_symptoms():
                symptom_groups.setdefault(symptom, []).append(patient)

        for symptom, patients_list in symptom_groups.items():
            print(f"Symptom: {symptom}")
            for patient in patients_list:
                print(f" - {patient.full_name()}")

    def save_patients_text_file(self, patients, filename="active_patients.txt"):
        with open(filename, 'w') as file:
            file.write("     Full Name      | Doctor`s Full Name | Age |    Mobile     | Postcode | Family ID|           Symptoms\n")
            for patient in patients:
                file.write(str(patient) + '\n')
        print("Active patient data exported successfully.")

    def extract_patient_data_from_file(self, filename="active_patients.txt"):
        print("-----Extract Patient Data from File-----")
        try:
            with open(filename, 'r') as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("File not found.")

    def management_report(self, doctors, patients, discharged_patients):
        print("-----Management Report-----")
        
        # Total number of doctors
        total_doctors = len(doctors)
        print(f"Total number of doctors: {total_doctors}")
        
        # Total number of patients per doctor
        doctor_patient_count = {doctor.full_name(): 0 for doctor in doctors}
        for patient in patients:
            if patient.get_doctor() in doctor_patient_count:
                doctor_patient_count[patient.get_doctor()] += 1
        print("\nTotal number of patients per doctor:")
        for doctor, count in doctor_patient_count.items():
            print(f"{doctor}: {count} patients")
        
        # Total number of appointments per month per doctor
        doctor_appointments = {}
        print("\nTotal number of appointments per month per doctor:")
        for doctor in doctors:
            appointment_counts = doctor.get_appointments_per_month()
            doctor_appointments[doctor.full_name()] = appointment_counts
            print(f"{doctor.full_name()}:")
            for month, count in appointment_counts.items():
                print(f"  {month}: {count} appointments")
        
        # Total number of patients based on illness type
        illness_counts = {}
        for patient in patients:
            for symptom in patient.get_symptoms():
                final_symptom = symptom.lower().capitalize()
                illness_counts[final_symptom] = illness_counts.get(final_symptom, 0) + 1
        print("\nTotal number of patients based on illness type:")
        for illness, count in illness_counts.items():
            print(f"{illness}: {count} patients")
        
        # Generate charts using the computed metrics
        self.generate_report_charts(total_doctors, doctor_patient_count, doctor_appointments, illness_counts)


    def generate_report_charts(self, total_doctors, doctor_patient_count, doctor_appointments, illness_counts):
        # Generates visual charts for management reports
        plt.figure(figsize=(12, 10))
        
        # Bar chart - Patients per doctor
        plt.subplot(2, 2, 1)
        plt.bar(list(doctor_patient_count.keys()), list(doctor_patient_count.values()), color='skyblue')
        plt.xlabel("Doctors")
        plt.ylabel("Number of Patients")
        plt.title("Total Patients Per Doctor")
        plt.xticks(rotation=45)
        
        # Line chart - Appointments per month per doctor
        plt.subplot(2, 2, 2)
        for doctor, months in doctor_appointments.items():
            if months:
                months_sorted = sorted(months.items())
                months_labels, counts = zip(*months_sorted)
                plt.plot(months_labels, counts, marker='o', label=doctor)
        plt.xlabel("Months")
        plt.ylabel("Appointments")
        plt.title("Appointments Per Month Per Doctor")
        plt.legend()
        plt.xticks(rotation=45)
        
        # Pie chart - Patients based on illness type
        plt.subplot(2, 2, 3)
        if illness_counts:
            plt.pie(list(illness_counts.values()), labels=list(illness_counts.keys()), 
                    autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        plt.title("Patients Based on Illness Type")
        
        # Bar chart - Total number of doctors
        plt.subplot(2, 2, 4)
        plt.bar(["Total Doctors"], [total_doctors], color='lightgreen')
        plt.ylabel("Count")
        plt.title("Total Number of Doctors")
        
        plt.tight_layout()
        plt.show()

    def update_details(self):
        # Allows the admin to update their username, password, or address
        print("-----Update Admin Details-----")
        print("1. Update Username")
        print("2. Update Password")
        print("3. Update Address")
        option = input("Enter the number of the field to update: ")
        
        if option == '1':
            new_username = input("Enter new username: ")
            self.__username = new_username
            print("Username updated successfully.")
        elif option == '2':
            new_password = input("Enter new password: ")
            self.__password = new_password
            print("Password updated successfully.")
        elif option == '3':
            new_address = input("Enter new address: ")
            self.__address = new_address
            print("Address updated successfully.")
        else:
            print("Invalid option. Please select a valid number.")
