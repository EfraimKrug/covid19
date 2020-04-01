#
# reading COVID-19 files & literature
#
import os
import json
import sqlite3
# print os.listdir('./data/kaggle/comm_use_subset')
trackAll = dict()
keepCount = dict()

conn = sqlite3.connect('./db/stats.db')
cur = conn.cursor()
cur2 = conn.cursor()

sql = []

sql.append("SELECT * FROM WordList WHERE WORD LIKE '{%'  OR  WORD LIKE '[%' ")
sql.append("SELECT * FROM WordList WHERE WORD IN ('uend:', 'utext:', 'uref_id:', 'ucite_spans:', 'uref_spans:', 'usection:')")
sql.append("SELECT * FROM WordList WHERE WORD LIKE 'u%(%'")
sql.append("SELECT * FROM WordList WHERE WORD LIKE 'u%'")

for sql_statement in sql:
    cur.execute(sql_statement)
    rs = cur.fetchall()
    for rec  in rs:
        # print(rec[2])
        sql_delete = "DELETE FROM WordList WHERE ID = " + str(rec[0])
        # print(sql2)
        conn.execute(sql_delete)

conn.commit()
conn.close()
