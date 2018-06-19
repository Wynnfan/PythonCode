# -*- coding: utf-8 -*-


if __name__ == '__main__':
    expect = [{
        'name': 'leijun',
        'corp_name': 'jobs'
    }, {
        'name': 'yangmi',
        'corp_name': 'bill'
    }, {
        'name': 'zhouxun',
        'corp_name': 'jobs'
    }]
    actual = [{
        'id': 1,
        'name': 'zhouxun',
        'corp_name': 'jobs'
    }, {
        'id': 2,
        'name': 'leijun',
        'corp_name': 'jobs'
    }, {
        'id': 3,
        'name': 'yangmi',
        'corp_name': 'bill'
    }]

    def assert_list(e, a):
        count = 0
        for i in e:
            for j in a:
                if all((k in j and j[k]==v) for k,v in i.items()):
                    count += 1
                    break
        if count == len(e):
            return True
        else:
            return False


    print(assert_list(expect, actual))
    #print(assert_list(expect, actual))