# print("hello world!")

'''
a = len(input("请输入你想输入的内容："))
print(a)
b = a%2
print(b)
if b == 0:
    print("您输入的字数是双数")
if b == 1:
    print("您输入的字数是单数")
'''

'''
b = ("你好","乒乓球")
a = (1,2,333,9999,"shafhl","龙猫",b,"世界很奇妙")
print(a[-2][-1])

print(a.index(b("乒乓球")))
print(a.count(2))
'''
b = ("你好","乒乓球")
a = [333,9999,"shafhl","龙猫",b,]
a.append("nnnbbb")
print(a)
zf = "哈哈"
a.insert(1,zf)
print(a)

yy = a.pop(4)
print(yy,a)





