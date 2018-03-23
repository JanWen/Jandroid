import sqlite3

conn = sqlite3.connect('bunker_xp.db')
c = conn.cursor()

def setup_db():
	c.execute('''CREATE TABLE membership
	             (user_id integer, gang_id integer)''')
	
	c.execute('''CREATE TABLE gang_xp
				(gang_id integer, gang_xp integer, gang_owner integer)''')

	conn.commit()
#setup_db()

def delete_xp():
	with conn:
		c.execute("drop table xp")


def make_entry(table_name, fst_int, snd_int):
	with conn:
		c.execute("INSERT INTO "+table_name+" VALUES (?,?)",(fst_int,snd_int))

def update_user(user_id, gang_id):
	with conn:
		c.execute(""""
			update membership
			set gang_id=?
			where user_id=?
		""", (user_id, gang_id))

def update_xp(gang_id, new_xp):
	c.execute("select * from gang_xp where gang_id = ?",(gang_id))
	old_xp = c.fetchone()
	with conn:
		c.execute(""""
			update membership
			set gang_xp=?
			where gang_id=?
		""", (old_xp+new_xp, gang_id))

def gen_dump(table_name):
	for i in c.execute("select * from "+table_name):
		yield(i)

def fst_int():
	for i in gen_dump():
		yield i[0]

