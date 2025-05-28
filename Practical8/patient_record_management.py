class Patient:
    def __init__(self, name, age, admission_date, medical_history):
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.medical_history = medical_history

    def print_patient_info(self):
        print(f"Patient: {self.name}, Age: {self.age}, Admission Date: {self.admission_date}, Medical History: {self.medical_history}")

# Example usage
patient1 = Patient("John Doe", 30, "2024-10-01", "No known allergies")
patient2 = Patient("Jane Smith", 25, "2024-10-02", "Allergic to penicillin")

patient1.print_patient_info()  # Output: Patient: John Doe, Age: 30, Admission Date: 2024-10-01, Medical History: No known allergies
patient2.print_patient_info()  # Output: Patient: Jane Smith, Age: 25, Admission Date: 2024-10-02, Medical History: Allergic to penicillin