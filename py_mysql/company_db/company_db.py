from mysql import connector

class Company:

    def __init__(self):
        
        try:
            self.connection = connector.connect(

                host ="localhost",
                user ="root",
                password ="Password@123",
                database ="company_db",
                use_pure = True
            )

            self.cursor=self.connection.cursor()
            print("db connect.....")

        except Exception as e:

            print(e)

    def add_employee(self,**kwargs):

        try:
            column =""
            values  =""

            for k,v in kwargs.items():
                column+= k+","
                values+= "%s"+","

            column =column.rstrip(",")
            values =values.rstrip(",")

            query =f"insert into employee ({column})values({values})"

            data =[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

            print("record inserted.....")

        except Exception as e:
            
            print(e)

    def list_all_employees(self):

        try:
            query = "select * from employee"

            self.cursor.execute(query)

            record = self.cursor.fetchall()

            for row in record:
                print("list all records....",row)

        except Exception as e:
            print(e)

    def fetch_employee_record(self,id):

        try:
            query ="select * from employee where id =%s"

            data =(id,)

            self.cursor.execute(query,data)

            record = self.cursor.fetchone()

            print("records fetched success...",record)

        except Exception as e:

            print(e)

    def delete_employee(self,id):

        try:

            query = "delete from employee where id =%s"

            data =(id,)
            
            self.cursor.execute(query,data)

            self.connection.commit()

            print("record deleted....")

        except Exception as e:

            print(e)

    def update_employee(self,id,**kwargs):

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
        

company_instance = Company()

company_instance.add_employee(name="kavya",age="28",email="kavya@gmail.com",department="HR",gender="female",salary="56000",experience="5",location="kochi")

company_instance.list_all_employees()

company_instance.fetch_employee_record(1,)

company_instance.delete_employee(3,)

company_instance.update_employee(1,salary=50000,duty_shift="day shift")


