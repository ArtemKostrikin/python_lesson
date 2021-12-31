from random import randint
from time import perf_counter

my_list = [randint(-10, 10) for _ in range(20)]


uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(uniq_list)

start = perf_counter()
check = set()
uniq = set()
for el in my_list:
    if el not in check:
        check.add(el)
        uniq.add(el)
    else:
        if el in uniq:
            uniq.remove(el)
print(perf_counter() - start)

print(uniq, uniq_list)