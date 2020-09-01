
'''
a = int(input("请输入你的年龄："))
if a > 18:
    print("尽情的熬夜吧！")
else:
    print("你还在长个，快滚去睡觉！")
'''
'''
x = "论迹不论心，论心无完人！"
y = "完人"
if y in x:
    print("y在x中")
else:
    print("y不在x中")

m = "许是天仙狂醉，乱把白云揉碎！"
n = "白云"
if n is m:
    print("m和n一样")
else:
    print("m和n不一样")
'''

'''
# 初级版
a = int(input("请输入一个整数："))
if a > 18:
    print("黄花大闺女")
else:
    print("钢铁直男")
# 进阶版
b = len(input("请输入一个字符串："))
if b > 6:
    print("合格")
else:
    print("不合格")
'''

# 作业
# 2.输入一个账号，输入一个密码，要求判断账号的长度大于5位，并且小于8位，
# 如果输入账号为张三12345，密码为123456就可以登录成功，否则就登录失败
username = input("请输入账号：")
password = input("请输入密码：")
if len(username) > 5 and len(username) < 8:
    if username == "张三12345" and password == "123456":
        print("登录成功！")
    else:
        print("登录失败！")
else:
    print("登录失败！")
