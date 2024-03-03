class Perosn:
    def __init__(self,name,age,rollno) -> None:
        self.name = name
        self.age = age
        self._rollno= rollno
    def display(self):
        print(f"Name is {self.name}")
        print(f"age is {self.age}")
        print(f"roll no is {self._rollno}")
class Student(Perosn):
    def __init__(self, name, age, rollno,marks) -> None:
        super().__init__(name, age, rollno)
        self.marks   = marks
    def diplay(self):
        super().display()
        print(f"marks are {self.marks}")

p1 = Perosn("zaid",45,109)
p1.display()

p2 = Student("unknown",45,40,456)
p2.display()



print("zaid")
