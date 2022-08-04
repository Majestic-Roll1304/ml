import sqlite3
conn = sqlite3.connect('StudentInfo') 
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS student')
cur.execute('CREATE TABLE student (name TEXT, rno INTEGER)')
cur.execute('INSERT INTO student (name, rno) VALUES (?, ?)',('Mahesh', 45))
cur.execute('INSERT INTO student (name, rno) VALUES (?, ?)',('Rahul', 30))
cur.execute('SELECT * FROM student')
#print ("Data in the table using fetchall() function:")
print (cur.fetchall())
conn.close()
#OUTPUT: [('Mahesh', 45), ('Rahul', 30)]
