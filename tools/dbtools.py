import pymysql # 要想用pymysql，就必须要导入它


def query(sql):
    # 固定的方法
    db = pymysql.connect(host='192.144.148.91', user='ljtest', password="Lj123456+", db='ljtestdb')
    # 获取查询窗口：游标
    cur = db.cursor()
    # 执行sql语句
    cur.execute(sql)
    # 获取所有的结果
    res = cur.fetchall()
    db.close()
    return res

if __name__ == "__main__":
    a = query("select * from t_user where id = 1111")
    print(a)