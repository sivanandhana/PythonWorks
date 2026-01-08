from mysql import connector

connection = connector.connect(

    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "tripwisedb",
    use_pure =True
)

cursor = connection.cursor()

query = "update user set name = %s,password =%s where id = %s"

data = ("Amalabincy","Amala@898",5)

cursor.execute(query,data)

connection.commit()

print("record updated......")

connection.close()

cursor.close()

