def get_filters(path):
    if path is None:
        return

    filters = []
    with open(path,'r') as f:
        for line in f.readlines():
            if '\n' in line:
                filters.append(line[:-1])
            else:
                filters.append(line)
    return filters

def main_0011():
    filters = get_filters('filtered_words.txt')
    while 1:
        tmp = input('plz input: ')
        if tmp == "0":
            print("Exit")
            break
        for i in filters:
            if i in tmp:
                print("Freedom")
            else:
                print("Human Rights")

def main_0012():
    filters = get_filters('filtered_words.txt')
    while 1:
        tmp = input('plz input:')
        for i in filters:
            if i in tmp:
                tmp = tmp.replace(i, '*' * len(i))
        print(tmp)

if __name__ == '__main__':

    main_0012()