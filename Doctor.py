class Doctor:
    # A class that deals with the Doctor operations

    def __init__(self, first_name, surname, speciality):
        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = {}

    def full_name(self):
        return f"{self.__first_name} {self.__surname}"

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def get_surname(self):
        return self.__surname

    def set_surname(self, new_surname):
        self.__surname = new_surname

    def get_speciality(self):
        return self.__speciality

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality

    def add_patient(self, patient):
        self.__patients.append(patient)

    def remove_patient(self, patient):
        # Removes a patient from the doctor's list of patients
        if patient in self.__patients:
            self.__patients.remove(patient)
            print(f"Patient {patient.full_name()} has been removed from Dr. {self.full_name()}'s list.")
        else:
            print(f"Patient {patient.full_name()} is not assigned to Dr. {self.full_name()}.")

    def view_patients(self):
        # Displays all patients assigned to this doctor
        if self.__patients:
            print(f"Patients under Dr. {self.full_name()}:\n")
            for patient in self.__patients:
                print(f"- {patient.full_name()}")
        else:
            print(f"No patients currently assigned to Dr. {self.full_name()}.")

    def add_appointment(self, month):
        # Adds an appointment count for a specific month
        if month in self.__appointments:
            self.__appointments[month] += 1
        else:
            self.__appointments[month] = 1

    def get_appointments_per_month(self):
        # Returns a dictionary of appointments per month
        return self.__appointments

    def __str__(self):
        return f'{self.full_name():^30}|{self.__speciality:^15}'
