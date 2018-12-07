import MySQLdb
conn = MySQLdb.connect("localhost","sammy","Pkp82@82","exam")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Pages2(id INTEGER not null PRIMARY KEY auto_increment)''')
conn.commit();
cur.close();
