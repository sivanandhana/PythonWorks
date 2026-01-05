class Father:

    def father_skill(self):

        print("cricket")

class Mother:

    def mother_skill(self):

        print("cooking skill")

class Child(Father,Mother):

    pass

child_instance=Child()

child_instance.father_skill()

child_instance.mother_skill()