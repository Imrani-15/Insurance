import mysql.connector
import traceback
def data_update(Firstname,Policy_No,Date,incident_reason):
    Ins = mysql.connector.connect(user='root',password='Imri@100$',host='127.0.0.1',database='rasa_db',auth_plugin='mysql_native_password')
    mycursor = Ins.cursor()
    table = "CREATE TABLE insurance1 (Firstname VARCHAR(255),Policy_No VARCHAR(255),Date VARCHAR(255),incident_reason VARCHAR(255));"
    table = "INSERT INTO insurance1 (Firstname,Policy_No,Date,incident_reason) VALUES ('{0}','{1}','{2}','{3}');".format(Firstname,Policy_No,Date,incident_reason)
    mycursor.execute(table)
    Ins.commit()
    print(mycursor.rowcount, "row inserted.")
    Ins.close()

if __name__=="__main__":

    data_update("sita", 789456, "15-08-2010", "It was car accident")

def getData(query:str):
    try:
        Ins = mysql.connector.connect(user='root',password='Imri@100$',host='127.0.0.1',database='rasa_db',auth_plugin='mysql_native_password')
        cursor = Ins.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except:
        print("Error occured while connecting to database or fetching data from database. Error Trace: {}".format(traceback.format_exc()))
        return []
