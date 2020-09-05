

'''
# 1.计算1000之内偶数的个数
def fangfa(a):
    m = 0
    n = 0
    x = []
    y = []
    for i in range(a):
        if i%2 == 0:
            x.append(i)
            m = m + 1
        else:
            y.append(i)
            n = n + 1
    print("----------------这个整数序列共有{}个偶数，它们分别是：----------".format(m))
    print(x)
    print("----------------这个整数序列共有{}个奇数，它们分别是：----------".format(n))
    print(y)
fangfa(1000)
'''

'''
# 2.将一个数组逆序输出【22,33,1,4,5,6,7】
a = [22,33,1,4,5,6,7]
a.reverse()
print(a)
'''

'''
# 3.输入一个整数，判断该整数的因数有哪些？
def yinshu(c):
    m = 0
    x = []
    for i in range(2,c,1):      # 1和数字本身不算作因数，从2开始除，到c-1结束
        if int(a)%i == 0:
            x.append(i)
            m = m + 1
    print("-----------该整数共有{}个因数，分别是：---------".format(m))
    print(x)

a = input("请输入一个整数：")
yinshu(int(a))
'''


# 4.把这个字典中带“美”的名字复制到一个新的字典中。 
# {"username1":"乔美丽","username2":"刘美丽","username3"：“郭美丽”,"username4:"郭然然""}
meiming = {"username1":"乔美丽","username2":"刘美丽","username3":"郭美丽","username4":"郭然然"}
m = "美"
zuimei = {}
for i in meiming:
    if m in meiming[i]:
        aa = {i:meiming[i]}
        zuimei.update(aa)
print(zuimei)
        

