import sqlite3

conn=sqlite3.connect("database_words.db")

def count_index():
    cur = conn.cursor()
    count = cur.execute("select count(word) from words;")
    rowcount = cur.fetchone()[0]
    return rowcount

ct=count_index()


cursor=conn.execute("select * from daily")

for row in cursor:
    conn.execute("insert into words(id, word, meaning) values(?,?,?);",(ct+1, row[1], row[2]))
    ct=ct+1

conn.commit()
conn.execute("delete from daily")
conn.commit()
conn.close()                 
            
print("DAILY TABLE RESETED")                 
