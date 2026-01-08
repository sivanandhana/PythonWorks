from mysql import connector

connection = connector.connect(

    host ="localhost",
    user = "root",
    password = "Password@123",
    database ="tripwisedb",
    use_pure = True
)

cursor = connection.cursor()

query = """
insert into user (name,email,password) values(%s,%s,%s)

"""
data = [
    ("arya","arya@gmail.com","Arya@23"),
    ("arun","arun@gmail.com","Arun@0505"),
    ("neenu","neenu@gmail.com","Neenu@56"),
    ("amala","amala@gmail.com","Amala@123"),
]

cursor.executemany(query,data)



connection.commit()

print("query executed......")

cursor.close()

connection.close()