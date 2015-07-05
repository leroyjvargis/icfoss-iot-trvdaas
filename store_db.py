import MySQLdb as mdb

def init(loc_coord, loc_name, offense):
	con = mdb.connect('localhost', 'root', 'root', 'TRVDaA')
	with con:
		cur = con.cursor()
		cur.execute("INSERT INTO db (loc_coord, loc_name, offense) VALUES (%s, %s, %s);", (loc_coord, loc_name, offense))
		con.commit()
	if con:
		con.close()

