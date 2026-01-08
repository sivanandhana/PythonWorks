from mysql import connector

connection = connector.connect(

    host ="localhost",
    user ="root",
    password = "Password@123",
    database ="tripwisedb",
    use_pure=True
)

cursor = connection.cursor()

query = """
create table user(
id int primary key auto_increment,
name varchar(200) not null,
email varchar(200) not null unique,
password varchar(100) not null

)
"""

cursor.execute(query)

print("table created")