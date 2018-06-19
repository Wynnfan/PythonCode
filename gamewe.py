'''
GameName:Heroes
beta-0.1

'''
#血量
Hp = 100
#魔法值
Mp = 50

print("Welcome Heroes World!")
print("input your name:")

while True:
    name = input()
    #判断角色名是否为空
    if name.strip() == "":
        print("Error! Please input again:")
    else:
        break
#人物信息
usermsg = [name,Hp,Mp]
print(usermsg)