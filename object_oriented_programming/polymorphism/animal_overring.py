class Animal:

    def __init__(self,name):

        self.name = name

       

        def sound(self):

            print(self.name,"sound")

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def sound(self):

        print(self.name,"bow..!")

class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def sound(self):

        print(self.name,"meow...!")


dog_instance=Dog("tobby")

cat_instance=Cat("miki")

dog_instance.sound()

cat_instance.sound()




        