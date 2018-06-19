# -*- coding: utf-8 -*-

def main():
    for i in range(100,200):
        flag = 1
        for j in range(2,i-1):
            if(i%j==0):
                flag=0
                break
        if flag:
            print(i)
if __name__ == '__main__':
    main()