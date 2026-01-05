import csv

class Dog:

    def __init__(self):

        file_path="tasks\\dog\\dog_breeds.csv"

        fr=open(file_path,"r")

        reader=csv.DictReader(fr)

        self.data=[row for row in reader]


    def all_breads(self):

        print(len(self.data))


    def breads(self):

        bread=[d.get("Breed")for d in self.data]

        bread_count={d:bread.count(d) for d in bread}

        print(bread_count)

    def brown_eye_dogs(self):

        # brown_eyes=[eye.get("Breed")for eye in self.data if eye.get("Color of Eyes")=="Brown"]
        brown_eyes=[eye.get("Breed")for eye in self.data if "Brown"in eye.get("Color of Eyes")]

        print(brown_eyes)


    def france_bread(self):


        france_bread =[b.get("Breed")for b in self.data if b.get("Country of Origin")=="France"]

        print(france_bread)


    def countrys(self):

        country = [c.get("Country of Origin")for c in self.data]

        country_cout={c:country.count(c) for c in country }

        print(country_cout)


    def fur_red(self):

        # fur_color_red =[r.get("Breed")for r in self.data if r.get("Fur Color")=="Red"]
        fur_color_red =[r.get("Breed")for r in self.data if "Red" in r.get("Fur Color")]

        print(fur_color_red)


    def Longevity (self):

        Longevitys = [l.get("Breed") for l in self.data if l.get("Longevity (yrs)")=="10-12"]

        print(Longevitys)

    def brown_eye_china_dogs(self):

        china_dog=[d.get("Breed") for d in self.data if d.get("Color of Eyes")=="Brown" and  d.get("Country of Origin")=="China"]

        print(china_dog)
        







dog_instance = Dog()

# dog_instance.all_breads()

# dog_instance.breads()

# dog_instance.brown_eye_dogs()

# dog_instance.france_bread()

dog_instance.countrys()

dog_instance.fur_red()

# dog_instance.Longevity()

# dog_instance.brown_eye_china_dogs()




        