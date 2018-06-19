# -*- coding: utf-8 -*-
class IntSet(object):
    def __init__(self):
        self.vals = []

    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    def member(self, e):

        return e in self.vals
    def remove(self, e):

        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + 'not found')

    def getMember(self):
        return self.vals[:]
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'
def triangles():
    target = [1]
    n = 0
    while n<10:
        yield target
        target = [1] + [target[i] + target[i + 1] for i in range(len(target) - 1)] + [1]
        n += 1

def normalize(name):
    return name.lower().title()

if __name__ == '__main__':
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)
    #s = IntSet()
    #s.insert(3)
    #s.insert(5)
    #print(s)
