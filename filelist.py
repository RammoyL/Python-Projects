
import sqlite3

conn = sqlite3.connect('FileList.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_FileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_ftype TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('FileList.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_FileList(col_fname, col_ftype) VALUES (?,?)", \
                ('information', '.docx'))
    cur.execute("INSERT INTO tbl_FileList(col_fname, col_ftype) VALUES (?,?)", \
                ('Hello', '.txt'))
    cur.execute("INSERT INTO tbl_FileList(col_fname, col_ftype) VALUES (?,?)", \
                ('myImage', '.png'))
    cur.execute("INSERT INTO tbl_FileList(col_fname, col_ftype) VALUES (?,?)", \
                ('myMovie', '.mpg'))
    cur.execute("INSERT INTO tbl_FileList(col_fname, col_ftype) VALUES (?,?)", \
                ('World', '.txt'))
    cur.execute("INSERT INTO tbl_FileList(col_fname, col_ftype) VALUES (?,?)", \
                ('data', '.pdf'))
    cur.execute("INSERT INTO tbl_FileList(col_fname, col_ftype) VALUES (?,?)", \
                ('myPhoto', '.jpg'))
    conn.commit()
conn.close()



conn = sqlite3.connect('FileList.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname, col_ftype FROM tbl_FileList WHERE col_ftype = '.txt'")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "File Name: {} \nFile Type: {}".format(item[0],item[1])
    print(msg)
