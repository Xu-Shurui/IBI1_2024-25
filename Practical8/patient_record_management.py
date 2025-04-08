class patient:
    def __init__(self, name, age, admission_date, medical_history):
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.medical_history = medical_history
    def print_patient_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Admission Date: {self.admission_date}")
        print(f"Medical History: {self.medical_history}")
patient1 = patient("John Doe", 30, "2024-10-01", "No known allergies")
patient2 = patient("Jane Smith", 25, "2024-10-02", "Allergic to penicillin")
patient1.print_patient_info()
patient2.print_patient_info()