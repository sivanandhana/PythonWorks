class Person:

    def __init__(self,name,age,gender):

        self.name=name

        self.age=age

        self.gender=gender

    @property   #decorator

    def get_age(self):

        print(self.age)

    @property  #decorator

    def get_gender(self):

        print(self.gender)

person_instance1 = Person("amal",20,"male")

person_instance1.get_age






