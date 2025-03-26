from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    The main function to be run when the program starts.
    """

    # Initializing the actors
    admin = Admin('admin', '123', 'B1 1AB')  # username: 'admin', password: '123'
    doctors = [Doctor('John', 'Smith', 'Internal Med.'), Doctor('Jone', 'Smith', 'Pediatrics'), Doctor('Jone', 'Carlos', 'Cardiology')]
    patients = [Patient('Sara', 'Smith', 20, '07012345678', 'B1 234', ['Cough', 'Fever']), Patient('Mike', 'Jones', 37, '07555551234', 'L2 2AB', ['Headache']), Patient('David', 'Smith', 15, '07123456789', 'C1 ABC', ['Cough'])]
    discharged_patients = []

    # Login process
    while True:
        try:
            if admin.login():
                running = True
                break
        except Exception as e:
            print(e)

    while running:
        print('\nChoose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Register/view/update/delete patient')
        print(' 3- Discharge patients')
        print(' 4- View discharged patients')
        print(' 5- Assign doctor to a patient')
        print(' 6- Relocate doctor to a patient')
        print(' 7- Group patients by Family ID')
        print(' 8- View patients grouped by Family ID')
        print(' 9- View Patients grouped by symptoms')
        print('10- Management report')
        print('11- Save patients text file')
        print('12- Extract data from patient text file')
        print('13- Update admin details')
        print('14- Quit')

        op = input('Option: ')

        if op == '1':
            admin.doctor_management(doctors)

        elif op == '2':
            admin.patient_management(patients)

        elif op == '3':
            admin.view_patient(patients)
            while True:
                choice = input('Do you want to discharge a patient (Y/N): ').lower()
                if choice in ['y', 'yes']:
                    admin.discharge(patients, discharged_patients)
                elif choice in ['n', 'no']:
                    break
                else:
                    print('Please answer with yes or no.')

        elif op == '4':
            admin.view_discharge(discharged_patients)

        elif op == '5':
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '6':
            admin.relocating_doctor(patients, doctors)

        elif op == '7':
            admin.assign_family_id(patients)

        elif op == '8':
            admin.group_by_family_id(patients)

        elif op == '9':
            admin.group_by_symptoms(patients)

        elif op == '10':
            admin.management_report(doctors, patients, discharged_patients)

        elif op == '11':
            admin.save_patients_text_file(patients)

        elif op == '12':
            admin.extract_patient_data_from_file()

        elif op == '13':
            admin.update_details()

        elif op == '14':
            print('Exiting program...')
            running = False

        else:
            print('Invalid option. Try again.')

if __name__ == '__main__':
    main()
