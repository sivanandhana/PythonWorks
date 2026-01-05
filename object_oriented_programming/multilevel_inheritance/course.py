class Course:

    def __init__(self,course_name):

        self.course_name = course_name

    def display(self):

        print(f"course_name : {self.course_name}")

class Module(Course):

    def __init__(self,course_name,module_name):

        super().__init__(course_name)

        self.module_name=module_name

    def display(self):

        print(f"module_name : {self.module_name}")

        super().display()

class Lesson(Module):

    def __init__(self, course_name, module_name,lesson_name):
        
        super().__init__(course_name,module_name)

        self.lesson_name = lesson_name

    def display(self):

        print(f"lesson_name : {self.lesson_name}")

        super().display()

lesson_instance=Lesson("pythan-django","oops","constructor")

lesson_instance.display()

        
        


 