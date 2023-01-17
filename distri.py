import psycopg2
connection=psycopg2.connect(user="postgres",password="1234",port="5432",database="bubt")
connection.autocommit=True
cursor=connection.cursor()
sql = copy employeetable from 'C:\Users\User\Desktop\proteus\data.csv' delimiter ',' csv header;
cursor.execute(sql)
connection.commit()
cursor.close()