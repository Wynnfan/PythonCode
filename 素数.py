def prime_numbers():
    for i in range(2,101):
        flag = 0
        for j in range(2,i-1):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            print(i)
def BubbleSort():
    sort = [32,15,4,25,6,53]
    length = len(sort)-1
    for i in range(length):
        for j in range(length):
            if sort[j] > sort[j+1]:
                k = sort[j]
                sort[j] = sort[j+1]
                sort[j+1] = k

    print(sort)
def SelectionSort():
    sort = [32, 3, 64, 2, 5]
    length = len(sort)
    for i in range(length):
        k = i
        for j in range(i+1, length):
            if sort[j] < sort[k]:
                k = j
        if k != i:
            sort[k], sort[i] = sort[i], sort[k]
    print(sort)

def fun(n):
    if n==1:
        return 1
    else:
        return n * fun(n-1)
# 创建 create 插入 insert 查询 select 更新 update 删除 delete
'''
import pymysql

db = pymysql.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'root123',
            db = 'TESTDB',
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor
        )

cursor = db.cursor()


# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
 
cursor.execute(sql)

# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Dell', 'peter', 35, 'W', 600)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 执行sql语句
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# SQL查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '{}'" .format(1000)
try:
   # 执行SQL语句
    cursor.execute(sql)

   # 获取所有记录列表
    results = cursor.fetchall()
    print(results)

except:
    print("Error: unable to fetch data")

db.close()
#print(fun(4))

BubbleSort()
SelectionSort()
'''
