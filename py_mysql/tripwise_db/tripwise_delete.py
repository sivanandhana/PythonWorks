from mysql import connector

connection = connector.connect(

    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "tripwisedb",
    use_pure = True
)

cursor = connection.cursor()

query =" delete from user where id =%s"

data =(2,)

cursor.execute(query,data)

connection.commit()

print("records deleted.....")

connection.close()

cursor.close()