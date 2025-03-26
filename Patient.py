class Patient:
    # Patient class

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms=None, family_id=None):
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'
        self.__symptoms = symptoms if symptoms else []
        self.__family_id = family_id

    def full_name(self):
        return f"{self.__first_name} {self.__surname}"

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        self.__surname = surname

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_mobile(self):
        return self.__mobile

    def set_mobile(self, mobile):
        self.__mobile = mobile

    def get_postcode(self):
        return self.__postcode

    def set_postcode(self, postcode):
        self.__postcode = postcode

    def get_doctor(self):
        return self.__doctor

    def link(self, doctor):
        self.__doctor = doctor

    def get_family_id(self):
        return self.__family_id

    def set_family_id(self, family_id):
        self.__family_id = family_id

    def get_symptoms(self):
        return self.__symptoms

    def print_symptoms(self):
        if self.__symptoms:
            print(f"Symptoms for {self.full_name()}: {', '.join(self.__symptoms)}")
        else:
            print(f"{self.full_name()} has no recorded symptoms.")

    def add_symptom(self, symptom):
        self.__symptoms.append(symptom)
        print(f"Symptom '{symptom}' added for {self.full_name()}.")

    def __str__(self):
        family_id = self.__family_id if self.__family_id is not None else ''
        symptoms = ', '.join(self.__symptoms) if self.__symptoms else 'None'
        return f'{self.full_name():^20}|{self.__doctor:^20}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}|{family_id:^10}|{symptoms:^30}'