# while 条件:

'''
i = 0
score = [78,46,55,88,100,86]
while i < len(score):
    if score[i] >= 60:
        print(score[i],"--该成绩及格")
    else:
        print(score[i],"--该成绩不合格!")
    i = i + 1
'''

'''
# 红绿灯练习  红灯35秒，绿灯20秒，黄灯5秒
i = 1
while i < 61:
    if i > 0 and i < 36:
        print("红灯")
    if i >= 36 and i < 56:
        print("绿灯")
    if i >= 56 and i < 61:
        print("黄灯")
    i = i + 1
'''

'''
# 遍历
zhanghao = {"username":"龙猫","password":"123456"}
for i in zhanghao:
    print(i)
    print(zhanghao[i])
print("-----------------------------")
for i in zhanghao.keys():                 #只取key值
    print(i)
print("------------------------------")
for i in zhanghao.values():               #只取value值
    print(i)
print("------------------------------")
for i,j in zhanghao.items():              #同时取key,value
    print(i,j)
print("------------------------------")
'''


t_user = [{"username":"zhangsan","password":"123456"},{"username":"芜湖","password":"999888"}]
u = input("请输入用户名：")
p = input("请输入密码：")
a = 1
for i in t_user:
    if i.get("username") == u and i.get("password") == p:
        print("登录成功")
        break
    else:
        if len(t_user) == a:
            print("登录失败")
    a = a + 1


# 作业：注册题目。  数组去重   数组中元素排序
