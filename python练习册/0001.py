import random,string

f=open('激活码.txt', 'w')
for n in range(200):
    chars = string.ascii_letters + string.digits #生成大小写字母及数字
    s = [random.choice(chars) for i in range(10)] #随机生成大小写数字10个
    f.write('{0}\n'.format(''.join(s)))
f.close()