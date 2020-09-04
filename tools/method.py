
import pymysql


def query(sql):
    db = pymysql.connect(host="118.24.105.78",user="root",password="1qaz!QAZ123***123",db="ljtestdb")
    cur = db.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    db.close()
    return res


# result = query("select price from t_goods where id = 1")
# print(result)
# print("------------------------------------")
# a = result[0][0]
# if a > 5488:
#     print("买不起")
# else:
#     print("买买买")