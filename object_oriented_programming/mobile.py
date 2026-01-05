class Mobile:

    title:str

    price:int

    brand: str

    features:str

    def __init__(self,title,price,brand,features):

        self.title=title

        self.price=price

        self.brand=brand

        self.features=features

    def display(self):

        print(f"title : {self.title} price : {self.price} brand : {self.brand} features : {self.features}")

mobile_instance1=Mobile("Samsung Galaxy A17",20000,"Galaxy","Battery perfomance")
mobile_instance2=Mobile("Iphone 17",1500000,"Apple","Camera Quality")

mobile_instance1.display()
mobile_instance2.display()
        

