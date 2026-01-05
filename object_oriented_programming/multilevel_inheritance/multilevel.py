class GrandParent:

    def properties(self):

        print("50 cent land with 1 vintage home and agriculture")

class Parent(GrandParent):

    def vehicle(self):

        print("MAClaren car")

class Child(Parent):

    def gadgets(self):

        print("Iphone , Ipad ")

child_instance=Child()

child_instance.gadgets()

child_instance.properties()

child_instance.vehicle()