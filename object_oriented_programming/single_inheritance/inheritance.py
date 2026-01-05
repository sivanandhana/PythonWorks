class Parent():
    def vehicles(self):
        print("jupiter")

class Child(Parent):
    def mobile(self):
        print("samsung")

child_instance=Child()

child_instance.mobile()

child_instance.vehicles()
