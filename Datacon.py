import pymssql
onnect(server='wtt\wtt',user='sa',password='perfect',database='df')
cur=conn.cursor()
cur.execute('select top 5 * from [dbo].[tempG]')
print (cur.fetchall())

cur.close()

conn.close()
