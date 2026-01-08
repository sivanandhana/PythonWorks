from mysql import connector

class Vehicle:

    def __init__(self):
        
        try:

            self.connection = connector.connect(

                host = "localhost",
                user = "root",
                password ="Password@123",
                database ="gosells_db",
                use_pure = True
            )

            self.cursor = self.connection.cursor()

            print("db connection ok....")

        except Exception as e:

            print(e)

    def add_vehicle(self,**kwargs):

        try:

            column =""
            values =""

            for k,v in kwargs.items():
                column+= k+","
                values+= "%s"+","

            column =column.rstrip(",")
            values =values.rstrip(",")

            query =f"""
            
                insert into vehicle ({column}) values ({values})
       
            """
            data =[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

            print("record inserted")

        except Exception as e:

            print(e)

    def list_vehicle(self):

        try:

            query="select * from vehicle"

            self.cursor.execute(query)

            record = self.cursor.fetchall()

            for row in record:

                 print(row)
        except Exception as e:

            print(e)

    def retrieve_vehicle(self,id=None):

        try:

            query ="""select * from vehicle where id =%s"""

            data =(id,)

            self.cursor.execute(query,data)

            records =self.cursor.fetchone()

            print(records)

        except Exception as e:

            print(e)

    def delete_vehicle(self,id=None):

        try:

            query ="delete from vehicle where id =%s"

            data=(id,)

            self.cursor.execute(query,data)

            self.connection.commit()

            print("record deleted....")

        except Exception as e:

            print (e)

    def update_vehicle(self,id=None,**kwargs):

        try:

            place_holder =""

            for k,v in kwargs.items():

              place_holder += k+"="+"%s"+","

            place_holder = place_holder.rstrip(",")

            query =f"update vehicle set {place_holder} where id ={id}"

            data = [v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

            print("record updated......")

        except Exception as e:

            print(e)





vehicle_instance = Vehicle()

# vehicle_instance.add_vehicle(name="passion pro",price=65000,year=2025,fuel_type="petrol",comments="good condition",running_km=2500,owner_type="single",owner="sreya",location="kochi")

# vehicle_instance.list_vehicle()

vehicle_instance.retrieve_vehicle(id = 3)

# vehicle_instance.delete_vehicle(id=2)

vehicle_instance.update_vehicle(id=3,fuel_type="diesel",price=45000)

vehicle_instance.retrieve_vehicle(id=3)