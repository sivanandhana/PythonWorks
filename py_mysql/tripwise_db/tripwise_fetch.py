from mysql import connector

connection = connector.connect(

    host ="localhost",
    user = "root",
    password = "Password@123",
    database ="tripwisedb",
    use_pure = True
)

cursor = connection.cursor()

query = "select * from user "


cursor.execute(query)

records = cursor.fetchall()

for row in records:

    print(row)

connection.close()

cursor.close()

