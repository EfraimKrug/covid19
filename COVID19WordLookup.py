#
# reading COVID-19 files & literature
#
import os
import json
import sqlite3
import colorama
from colorama import Fore
import sys
# print os.listdir('./data/kaggle/comm_use_subset')
trackAll = dict()
keepCount = dict()

conn = sqlite3.connect('./db/stats.db')
cur = conn.cursor()

def most_used(word):
    popular_count = dict()
    # print(word)

    sql = "SELECT * FROM WordList WHERE WORD = '" + str(word) + "'"
    cur.execute(sql)
    rs = cur.fetchall()
    for rec in rs:
        popular_count[rec[1]] = rec[3]

    # print(popular_count)
    return popular_count

def word_lookup(word):
    doc_list = most_used(word)
    # print(doc_list)
    doc_array = []
    for w in sorted(doc_list, key=doc_list.get, reverse=True):
        doc_array.append([w, doc_list[w]])
    # print(doc_array)
    return doc_array

def print_list(doc_array):
    color_flip = 0
    for e in doc_array:
        sql = "SELECT * FROM Document WHERE ID = " + str(e[0])
        cur.execute(sql)
        rs = cur.fetchall()
        for rec in rs:
            if(rec[3]):
                if(color_flip):
                    sys.stdout.write(Fore.BLUE + '\n' + str(rec[3]))
                    color_flip = 0
                else:
                    sys.stdout.write(Fore.RED + '\n' + str(rec[3]))
                    color_flip = 1

        sys.stdout.write(Fore.WHITE)

input_word = raw_input("\n\nSearch: ")
while input_word:
        return_list = word_lookup(input_word.lower())
        print_list(return_list)
        input_word = raw_input("\n\nSearch: ")

conn.close()
