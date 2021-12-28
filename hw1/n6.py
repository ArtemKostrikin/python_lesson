while True:
    days = 1
    start_km = float(input('Начальный результат - "))
    target_km = float(input('Финальный результат" -))
    if start_km <= 0 or target_km < 0
        print('Результаты должны быть больше нуля! Стартовое значение !=0')
    else:
        while start_km < target_km:
            start_km *= 1.1
            days += 1
            print(f'Спортсмен добьётся результата за {days} дней')