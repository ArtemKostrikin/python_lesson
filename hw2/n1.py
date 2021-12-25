my_list = [5, 1.1, 'text', None, True]

for i, item in  enumerate(my_list, 1):
    print(list(map(type, my_list)))