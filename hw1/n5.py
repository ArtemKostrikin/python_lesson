revenue = float(input("Введите значение выручки "))
costs = float(input("Введите значение издержек "))
result = revenue - costs
if result > 0
    print(f"Поздравляю ваша компания работает с прибылью {result} !")
    print(f"Рентабельность выручки - {result / revenue:.3f}")
    persons = int(input("Сколько счастливых сотрудников работает в вашей компании ? - "))
    print(f"Прибыль на одного сотрудника - {result / persons:.2f}")
elif result < 0:
    print(f"Вы работаете с убытком - {-result}")
else:
    print(f"Ноль это тоже хороший результат! Зато стабильно")