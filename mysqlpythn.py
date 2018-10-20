import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="anonymous001",  		  # your password
                     db="psosm")          # name of the data base

# you must create a Cursor object. It will let you execute all the queries you need.traverse the database

cursor = db.cursor()

#cursor will help you to execute the queries
#Let us query the data base we created yesterdday

#query = "SELECT * FROM tutorial"
#cursor.execute(query)
#rows = cursor.fetchall()

#print rows


query = "INSERT into tutorial (id, name) values (6,'shubhi')"

cursor.execute(query)
db.commit()


name = "Divyansh"
age = 22
affiliation = "NSIT"
interest = "Programming" #Difficult to store a list in a single column. Relational databases are designed specifically to store one value per row/column combination. 


#Let's create a new table where we will add the detailed presenter info


# query = "Create table detailed_participants ( name varchar(20) NOT NULL, age INT NOT NULL, affiliation varchar(10), interest varchar(20))"
# cursor.execute(query)
# db.commit()
# cursor.close()



query = "insert into detailed_participants (name,age,affiliation,interest) values (%s,%s,%s,%s)"

cursor.execute(query, (name, age, affiliation, interest))
db.commit()


query = "update detailed_participants set name = 'Divyansh Agarwal' where name = 'Divyansh'"
cursor.execute(query)
db.commit()

db.close()  #Closes the connection

