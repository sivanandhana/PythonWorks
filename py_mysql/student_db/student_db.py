from mysql import connector

class Student:

    def __init__(self):
        
        try:
            self.connection = connector.connect(

                host ="localhost",
                user ="root",
                password ="Password@123",
                database ="student_db",
                use_pure = True
            )

            self.cursor=self.connection.cursor()
            print("db connect.....")

        except Exception as e:

            print(e)

    def POST(self,**kwargs):

        try:

            coloumns=""
            values=""

            for k,v in kwargs.items():
                coloumns+=k+","
                values+="%s"+","

            coloumns=coloumns.rstrip(",")
            
            values= values.rstrip(",")


            query=f"insert into student({coloumns})values({values})"

            data=[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

            print("records inserted")

        except Exception as e:

            print(e)


    def GET(self):

        try:

            query="select * from student"

            self.cursor.execute(query)

            records=self.cursor.fetchall()

            for row in records:

                print("list all records...",row)

        except Exception as e:

            print(e)

    def GET(self,id=None):
            
        try:

            query="select * from student where id=%s"
            data=(id,)
            self.cursor.execute(query,data)

            records=self.cursor.fetchone()

            print("records fetched success...",records)

        except Exception as e:

            print(e)

    def DELETE(self,id=None):

        try:

            query="delete from student where id=%s"
            data=(id,)
            self.cursor.execute(query,data)
            self.connection.commit()
            print("record deleted...")

        except Exception as e:

            print(e)
            
    def UPDATE(self,id,**kwargs):

        try:

            placeholder =""

            for k,v in kwargs.items():

                placeholder+= k+"="+"%s"+","

            placeholder=placeholder.rstrip(",")

            query =f"update employee set {placeholder} where id ={id}"

            data =[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

            print("record updated.....")

        except Exception as e:

            print(e)
        
student_insatance=Student()

# student_insatance.POST(name="arya",age=18,email="arya@gamil.com",department="btech",fees=600000)
student_insatance.POST(name="vishnu",age=20,email="vishnu@gmail.com",department="auto_mobile",fees=3500000)
student_insatance.POST(name="kavya",age=18,email="kavya@gamil.com",department="BBA",fees=300000)
student_insatance.POST(name="rahul",age=18,email="rahul@gamil.com",department="BCA",fees=500000)
student_insatance.POST(name="arun",age=18,email="arun@gamil.com",department="Bsc computer science",fees=500000)
student_insatance.POST(name="nila",age=18,email="nila@gamil.com",department="Bsc maths",fees=500000)

# student_insatance.GET()


# student_insatance.GET(2)

# student_insatance.DELETE(3)



# student_insatance.PUT(5,fee=600000)

# student_insatance.select_one(5)