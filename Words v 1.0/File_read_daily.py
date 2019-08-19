import sqlite3
import sys
import os

x = input('Enter number of the file:')
file_str = 'daily_'+x+'.txt'
pr = os.getcwd()
os.chdir(r'Daily_folder')

lines = []
with open(file_str) as filex:
    for line1 in filex:
        line1 = line1.replace(':', '.')
        #line1 = line1.strip()
        lines.append(line1)
filex.close()

os.chdir(pr)
print(pr)
print(os.getcwd())

len=len(lines)
conn=sqlite3.connect("database_words.db")
conn.execute("delete from daily")
conn.commit()
for i in range(len):
    wx=lines[i].split('.')
    print(wx[0]+'  '+wx[1]+'  '+wx[2])
    conn.execute("insert into daily(id, word, meaning) values(?,?,?);",(wx[0],wx[1],wx[2]))
    conn.commit()

print("*DATABASE UPDATED*")
