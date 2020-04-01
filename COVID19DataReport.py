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

sql = "SELECT * FROM Document"
cur.execute(sql)
rs = cur.fetchall()
for rec  in rs:
    print(rec[3])
    sql2 = "SELECT * FROM WordList WHERE DOCUMENT_ID = " + str(rec[0])
    # print(sql2)
    cur2.execute(sql2)
    rs2 = cur2.fetchall()
    for rec2 in rs2:
        try:
            print(str(rec2[2]).encode('utf-8','replace') + " --> " + str(rec2[3]).encode('utf-8','replace'))
        except:
            continue
