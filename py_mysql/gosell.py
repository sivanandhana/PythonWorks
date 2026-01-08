
from mysql import connector

class Vehicles:

    def __init__(self):
        
        try:

            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="Password@123",
                database = "gosells_db"

            )

            self.cursor = self.connection.cursor()

            print("db connection ok....")

        except Exception as e:

            print(e)


    def add_vehicles(self,**kwargs):

        try:

            columns=""
            values=""

            for k,v in kwargs.items():

                columns+=k+","
                values+="%s"+","

            columns= columns.rstrip(",")
            values = values.rstrip(",")

            query = f"""
            insert into vehicle ({columns}) values({values})
            """
            
            data=[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

            print("record inserted")

        except Exception as e:

            print(e)

    def list_vehicles(self):

        try:

            query = "select * from vehicle"

            self.cursor.execute(query)

            records=self.cursor.fetchall()

            for row in records:

                print(row)
        
        except Exception as e:

            print(e)

    def retrieve_vehicles(self,id):

        try:

            query = "select * from vehicle where id = %s"

            data =(id,)

            self.cursor.execute(query,data)

            records = self.cursor.fetchone()

            print(records)

        except Exception as e:

            print(e)

    def delete_vehicles(self,id=None):

        try:

            query = "delete from vehicle where id = %s"

            data = (id,)

            self.cursor.execute(query,data)

            self.connection.commit()

            print("record deleted.....")

        except Exception as e:

            print(e)

    def update_vehicles(self,id,**kwargs):

        try:

            place_holder = ""

            for k,v in kwargs.items():

                place_holder+=k+"="+"%s"+","

            place_holder = place_holder.rstrip(",")

            query = f"update vehicle set {place_holder} where id={id}"

            data = [v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

        except Exception as e:

            print(e)

           



    

vehicle_instance = Vehicles()

#vehicle_instance.add_vehicles(name="thar",price=700000,year=2025,fuel_type="diesel",comments="well maintained",running_km=1400,owner_type="single",owner="abhilash",location="goa")

#vehicle_instance.list_vehicles()

#vehicle_instance.retrieve_vehicles(6)

#vehicle_instance.delete_vehicles(id=8)

#vehicle_instance.list_vehicles()

vehicle_instance.retrieve_vehicles(6)

vehicle_instance.update_vehicles(id=6,year=2022,fuel_type="petrol")

vehicle_instance.retrieve_vehicles(id=6)