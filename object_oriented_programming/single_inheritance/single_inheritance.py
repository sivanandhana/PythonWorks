class Person:
    def __init__(self,name,age,gender):

        self.name= name

        self.age= age

        self.gender= gender

    def display(self):

        print(f"name  : {self.name} age : {self.age} gender : {self.gender}")

class Student(Person):

    roll_no : str

    course : str

    def __init__(self, name, age, gender,roll_no,course):

        super().__init__(name, age, gender)

        self.roll_no=roll_no

        self.course=course

    def display(self):

        super().display()

        print(f"roll no : {self.roll_no} course : {self.course}")

child_instance1=Student("arun",24,"male",506,"django")

child_instance2=Student("kavya",20,"female",506,"data science")

child_instance1.display()


child_instance2.display()


        