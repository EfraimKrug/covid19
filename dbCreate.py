#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('./db/stats.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE Document
         (ID INT PRIMARY KEY     NOT NULL,
         TITLE           TEXT    NOT NULL,
         ABSTRACT        TEXT    NOT NULL,
         FILENAME        TEXT    NOT NULL);''')
print "Table created successfully";

conn.execute('''CREATE TABLE WordList
         (ID INT PRIMARY KEY    NOT NULL,
         DOCUMENT_ID    INT     NOT NULL,
         WORD           TEXT    NOT NULL,
         COUNT          INT     NOT NULL);''')
print "Table created successfully";

conn.close()
