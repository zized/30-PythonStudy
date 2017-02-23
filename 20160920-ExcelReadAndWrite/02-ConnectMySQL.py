import mysql.connector
import codecs

cnx = mysql.connector.connect(user = 'jacky', password = '1qaz!QAZ',
                              host = '127.0.0.1',
                              database = 'world')

cursor = cnx.cursor()
print(cursor)
query = ("SELECT Name FROM city")

cursor.execute(query)

for(CITY) in cursor:
    print(CITY[0].encode("GB18030"))
    
cursor.close()
cnx.close()


