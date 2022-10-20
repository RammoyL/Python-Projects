
import sqlite3

conn = sqlite3.connect('FileList.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_FileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT)")
    conn.commit()


conn = sqlite3.connect('FileList.db')

#tuple list
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
#loop through each oject in tuple to find the docs that end in '.txt'.
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        #will denote a one element tuple for each name ending with .txt
            cur.execute("INSERT INTO tbl_FileList (col_fname) VALUES (?)", (x,))
            print(x)

conn.close()

