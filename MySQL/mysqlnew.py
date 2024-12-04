# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root",
#   database="smec"
# )
# mycursor = mydb.cursor()
# # mycursor.execute("select * from orders")
# # for x in mycursor:
# #   print(x[0])

# sql = "INSERT INTO orders (oid, amount) VALUES (5,5000)"   
# # val = ("John", "Highway 21")
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")