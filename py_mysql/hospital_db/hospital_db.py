from mysql import connector

class Hospitals:

    def __init__(self):
        
        try:
            self.connection = connector.connect(

                host ="localhost",
                user ="root",
                password ="Password@123",
                database ="hospital_management_db",
                use_pure = True
            )

            self.cursor=self.connection.cursor()
            print("db connect.....")

        except Exception as e:

            print(e)


    def post(self,**kwargs):

        try:

            coloumns=""
            values=""

            for k,v in kwargs.items():
                coloumns+=k+","
                values+="%s"+","

            coloumns=coloumns.rstrip(",")
            
            values= values.rstrip(",")


            query=f"insert into hospital({coloumns})values({values})"

            data=[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

            print("records inserted....")

        except Exception as e:

            print(e)


    def get(self):

        try:

            query="select * from hospital"

            self.cursor.execute(query)

            records=self.cursor.fetchall()

            for row in records:

                print("list all records...",row)

        except Exception as e:

            print(e)

    def get(self,patient_id=None):
            
        try:

            query="select * from hospital where patient_id=%s"
            data=(patient_id,)
            self.cursor.execute(query,data)

            records=self.cursor.fetchone()

            print("records fetched success...",records)

        except Exception as e:

            print(e)

    def delete(self,patient_id=None):

        try:

            query="delete from hospital where patient_id=%s"
            data=(patient_id,)
            self.cursor.execute(query,data)
            self.connection.commit()
            print("record deleted...")

        except Exception as e:

            print(e)
            
    def put(self,patient_id,**kwargs):

        try:

            placeholder =""

            for k,v in kwargs.items():

                placeholder+= k+"="+"%s"+","

            placeholder=placeholder.rstrip(",")

            query =f"update hospital set {placeholder} where id ={patient_id}"

            data =[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

            print("record updated.....")

        except Exception as e:

            print(e)

hospital_instance = Hospitals()

# hospital_instance.post(name ="sreyas",age=24,gender ="male",doctor_name="navas",phone =8975643210)
# hospital_instance.post(name ="ram",age=21,gender ="male",doctor_name="surya",phone =9568754623)
# hospital_instance.post(name ="rahul",age=18,gender ="male",doctor_name="hima",phone =9875632145)
# hospital_instance.post(name ="gokul",age=15,gender ="male",doctor_name="smitha",phone =7563298546)

# hospital_instance.get(2)

# hospital_instance.get()

# hospital_instance.put(patient_id=3,age=20)
