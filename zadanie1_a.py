try:
    a = list(map(int, input('Введите первые катеты а: ').split()))
    b = list(map(int, input('Введите вторые катеты b: ').split()))
    if len(a) >= len(b):
        max = len(a)
    else:
        max = len(b)
    for i in range(max):
        c = (a[i]**2+b[i]**2)**0.5
        S = a[i]*b[i]/2
        print(f'Треугольник {i+1} с катетами {a[i]} и {b[i]} имеет площадь {S:.1f} и гипотенузу {c:.1f}')
except ValueError:
    print('NonNumericError: Вы ввели не число')
except IndexError:
    print('InconsistentDataError: массивы с катетами имеют разную длину')
