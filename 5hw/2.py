# Вероятность выпадения красного
Pn_red = 18/37
# Вероятность черного
Pn_black = 18/37
# Вероятность зеро
Pn_0 = 1/37
#Вероятность выпадения любого числа
P = Pn_red+Pn_black+Pn_0
print(P)

import random
import matplotlib.pyplot as plt
x=[]
for i in range (0,9):
    x.append(sum(random.sample(range(100), 10)))
print(x)
plt.hist(x, bins='auto')
plt.show()