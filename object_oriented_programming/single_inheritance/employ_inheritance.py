class Employee:
    def __init__(self,id,department,salary):

        self.id=id

        self.department=department

        self.salary=salary

    def display(self):

        print(f"id : {self.id} department : {self.department} salary : {self.salary}")

class Developer(Employee):

    def __init__(self,id,department,salary,programming_language,framework):
        
        super().__init__(id,department,salary)

        self.programming_language=programming_language

        self.framework=framework

    def display(self):

        super().display()

        print(f"programming_language : {self.programming_language} framework : {self.framework}")

child_instance=Developer(500,"web developer",500000,"python","django")

child_instance.display()



