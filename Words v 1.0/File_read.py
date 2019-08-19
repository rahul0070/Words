import sqlite3
import sys

conn=sqlite3.connect("database_words.db")
lines = []
file_str="GRE_words.txt"
with open(file_str) as filex:
    for line1 in filex:
        line1 = line1.replace(':', '.')
        #line1 = line1.strip()
        lines.append(line1)
filex.close()

len=len(lines)
conn.execute("delete from words")
conn.commit()
for i in range(len):
    wx=lines[i].split('.')
    print(wx[0]+'  '+wx[1]+'  '+wx[2])
    conn.execute("insert into words(id, word, meaning) values(?,?,?);",(wx[0],wx[1],wx[2]))
    conn.commit()

print("*DATABASE UPDATED*")
