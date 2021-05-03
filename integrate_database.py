import mysql.connector
#import traceback
def dataupdate(name,policy):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Imri@100$",
        database="rasa_db",
        auth_plugin = 'mysql_native_password'
    )
    mycursor = mydb.cursor()

#    table = "CREATE TABLE connect (name VARCHAR(255),policy VARCHAR(255));"
    table = "INSERT INTO connect (name,policy) VALUES ('{0}','{1}');".format(name,policy)

    mycursor.execute(table)

    mydb.commit()

    print(mycursor.rowcount, "row inserted.")

if __name__=="__main__":
    dataupdate("pooja",786954)








#    myresult = mycursor.fetchall()
#    for x in myresult:
#        print(x)
