try:
    a = list(map(int, input('Введите катеты: ').split()))
    for i in range(0, len(a), 2):
        c = (a[i]**2+a[i+1]**2)**0.5
        S = a[i]*a[i+1]/2
        print(f'Треугольник {i+1} с катетами {a[i]} и {a[i+1]} имеет площадь {S:.1f} и гипотенузу {c:.1f}')
except ValueError:
    print('NonNumericError: Вы ввели не число')
except IndexError:
    print('InconsistentDataError: массивы с катетами имеют разную длину')
