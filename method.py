
import pymysql


def query(sql):
    db = pymysql.connect(host="47.104.229.22",user="root",password="123456",db="db_morning")
    cur = db.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    db.close()
    return res
result = query("select * from tb_account where ACCOUNT_ID = 1")
print(result)