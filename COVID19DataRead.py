#
# reading COVID-19 files & literature
#
import os
import json
import sqlite3
# print os.listdir('./data/kaggle/comm_use_subset')
trackAll = dict()
keepCount = dict()
skipWords = ["these", "could", "which", "would", "their","since", "and/or"]
ABSTRACT_WEIGHT = 5
BODY_WEIGHT = 1
TITLE_WEIGHT = 10

def filterDict(keepCount):
    newDict = dict()
    for word in sorted(keepCount, key=keepCount.get, reverse=False):
        newWord = word.replace("'","").replace('"','')
        if not "u'" in word and not "\\u0" in word:
            if keepCount[word] > 10:
                newDict[newWord] = keepCount[word]
                # print("IN SORT: " + str(newDict[word]))
    return newDict
                # print(str(word) + ": " + str(keepCount[word]))

conn = sqlite3.connect('./db/stats.db')
counter = 0
for filename in os.listdir('./data/kaggle/comm_use_subset'):
    print(filename)
    trackAll[filename] = dict()
    counter = counter + 1
    with open('./data/kaggle/comm_use_subset/' + filename, 'r') as f:
        keepCount = dict()
        jsFile = json.loads(f.read())
        body_text = ""
        abstract_text = ""
        trackAll[filename]['title'] = jsFile['metadata']['title'].replace("'","").encode('utf-8')
        # print(str(jsFile['abstract'][0]['text']).replace('"','\\"'))
        for abs in jsFile['abstract']:
            abstract_text = abstract_text + abs['text']
        abstract_text = abstract_text.replace("'","").encode('utf-8','replace')

        # print(filename)
        # print(trackAll[filename]['title'])
        # print(abstract_text)
        valArray = []
        valArray.append(str(counter))
        valArray.append(filename)
        valArray.append(abstract_text)
        valArray.append(jsFile['metadata']['title'])
        for i in range (1,4):
            try:
                valArray[i] = valArray[i].replace("'"," ").replace('"', ' ')
                valArray[i] = valArray[i].decode('utf-8','replace')
                valArray[i] = "\"" + valArray[i] + "\""
            except UnicodeEncodeError:
                valArray[i] = "\"\""

        sql = "INSERT INTO Document (ID,TITLE,ABSTRACT,FILENAME) \
        VALUES (" + valArray[0] + "," + valArray[1].encode('utf-8',"replace") + "," +  valArray[2].encode('utf-8',"replace") + "," +  valArray[3].encode('utf-8',"replace") + ")"

        try:
            conn.execute(sql)
        except:
            print(sql)

        # parsing abstract text
        # each word in abstract is weighted more heavily
        for text in jsFile['abstract']:
            abstract_text = abstract_text + str(text)
        abstract_text = abstract_text.replace('.', ' ').replace(',',' ').replace("'","").replace("}", " ").replace(")", " ")
        wordArray = abstract_text.split(' ')
        for word in wordArray:
            if word in skipWords:
                continue
            if len(word) > 4:
                if word.lower() in keepCount:
                    keepCount[word.lower()] = keepCount[word.lower()] + ABSTRACT_WEIGHT
                else:
                    keepCount[word.lower()] = ABSTRACT_WEIGHT
        # parsing body text
        for text in jsFile['body_text']:
            body_text = body_text + str(text)
        body_text = body_text.replace('.', ' ').replace(',',' ').replace("'","").replace("}", " ").replace(")", " ")
        wordArray = body_text.split(' ')
        for word in wordArray:
            if word in skipWords:
                continue
            if len(word) > 4:
                if word.lower() in keepCount:
                    keepCount[word.lower()] = keepCount[word.lower()] + BODY_WEIGHT
                else:
                    keepCount[word.lower()] = BODY_WEIGHT

        # parsing TITLE text
        title_text = ""
        for text in jsFile['metadata']['title']:
            try:
                title_text = title_text + str(text).encode('utf-8','replace')
            except:
                continue
        title_text = title_text.replace('.', ' ').replace(',',' ').replace("'","").replace("}", " ").replace(")", " ")
        wordArray = title_text.split(' ')
        for word in wordArray:
            if word in skipWords:
                continue
            if len(word) > 4:
                if word.lower() in keepCount:
                    keepCount[word.lower()] = keepCount[word.lower()] + TITLE_WEIGHT
                else:
                    keepCount[word.lower()] = TITLE_WEIGHT


    trackAll[filename]['wordtrack'] = filterDict(keepCount)
    trackAll[filename]['Document'] = counter

    if counter > 50:
        break

# print(filterDict(keepCount))
# for word in keepCount:
wordCount = 0
for filename in trackAll:
    # print(trackAll[filename]['title'])
    # for word in trackAll[filename]['wordtrack']:
    for word in sorted(trackAll[filename]['wordtrack'], key=trackAll[filename]['wordtrack'].get, reverse=False):
        wordCount = wordCount + 1
        conn.execute("INSERT INTO WordList (ID,DOCUMENT_ID,WORD,COUNT) \
        VALUES (" + str(wordCount) + "," + str(trackAll[filename]['Document']) + ",'" + str(word) + "'," + str(trackAll[filename]['wordtrack'][word]) + ")");

conn.commit()
conn.close()
        # sep = ":\t"
        # if len(word) < 7:
        #     sep = ":\t\t"
        # print(str(word) + sep + str(trackAll[filename]['wordtrack'][word]))
