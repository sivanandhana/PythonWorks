import csv

class Toyota:
    def __init__(self):

        file_path = "tasks\\toyota\\toyota.csv"

        fr = open(file_path,"r")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def total_cars(self):

        print(len(self.data))

    def petrol_diseal_count(self):

        co=[f.get("fuelType")for f in self.data]

        fuel_count={f:co.count(f) for f in co}

        print(fuel_count)

    def highest_prices(self):

       

        price=[p.get("model") for p in self.data if int(p.get("price"))>20000]

        print(price)

    def tax_sum(self):

        total_tax = [int(t.get("tax"))for t in self.data]

        print(sum(total_tax))


    def engine(self):

        big_engine = [e.get("model")for e in self.data if float(e.get("engineSize"))>1.8]

        print(big_engine)

    def transmission_type(self):

        transmission = [t.get("transmission")for t in self.data]

        transmission_count = {t:transmission.count(t)for t in transmission}

        print(transmission_count)



        
        



        





data_instance = Toyota()

# data_instance.total_cars()

# data_instance.petrol_diseal_count()

# data_instance.prices()

# data_instance.tax_sum()

# data_instance.engine()

# data_instance.transmission_type()



        

    
