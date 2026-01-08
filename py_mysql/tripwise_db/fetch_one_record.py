from mysql import connector

connection = connector.connect(

    host ="localhost",
    user ="root",
    password = "Password@123",
    database = "tripwisedb",
    use_pure = True
)

cursor = connection.cursor()

query = "select * from user where id =%s"

data = (3,)

cursor.execute(query,data)

records = cursor.fetchone()

print(records)

connection.close()

cursor.close()