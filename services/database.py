import mysql.connector

host = "sql10.freesqldatabase.com",
port = 3306,
database = "sql10589148",
user = "sql10589148"
password = "RZz8yY1HCn"

cnx = mysql.connector.connect(
    host="sql10.freesqldatabase.com",
    port=3306,
    user="sql10589148",
    password="RZz8yY1HCn")

cursor = cnx.cursor()
