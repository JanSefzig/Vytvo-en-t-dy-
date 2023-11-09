class Student:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.hodnoceni = []

    def zobraz_informace(self):
        print(f"Jméno: {self.jmeno}")
        print(f"Příjmení: {self.prijmeni}")
        print("Hodnocení:", self.hodnoceni)


student1 = Student("Jan", "Novák")
student1.hodnoceni = [85, 90, 78, 92]


student1.zobraz_informace()
