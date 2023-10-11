#Список квадратов
#n = int(input())
#x = 1
#while a**2 <= n:
#    print(x**2)
#    x+=1

#Степень двойки
#n = int(input())
#st = 3
#k = 1
#p = 1
#while k < n:
#    for i in range(st):
#        p *= 2
#        print(p)
#    k = p
#    st += 1
#    print(k)
#    p = 1
#print(st)

#Утренняя пробежка
#x = int(input())
#y = int(input())
#l = x
#d = 0
#while l <= y:
#    l += 0.1*l
#    d += 1
#    print(d)

#длина последовательности
#a = 0
#while int(input()) != 0:
#    a += 1
#print(a)

#ряд 1
#a = int(input())
#b = int(input())
#if a <= b:
#    for i in range(a, b + 1):
#        print(i)

#ряд 2
#a = int(input())
#b = int(input())
#if a < b:
#    for i in range(a, b + 1):
#        print(i, end=' ')
#else:
#    for i in range(a, b - 1, -1):
#        print(i, end=' ')

# сумма н чисел
#n = int(input())
#summa = 0
#for i in range(n):
#    summa += int(input())
#print(summa)

#факториал
#a = 1
#n = int(input())
#for i in range(1, n + 1):
#    a *= i
#print(a)

#лесенка
#n = int(input())
#for i in range(1, n + 1):
#    for s in range(1, i + 1):
#        print(s, sep='', end='')
#    print()


#Количество элементов, которые больше предыдущего
#was = int(input())
#a = 0
#
#while was != 0:
#    next = int(input())
#    if next != 0 and was < next:
#        a += 1
#    was = next
#print(a)

#Второй максимум
#one_max = int(input())
#two_max = int(input())
#if one_max < two_max:
#    one_max, two_max = two_max, one_max
#w = int(input())
#while w != 0:
#    if w > one_max:
#        two_max, one_max = one_max, w
#    elif w > two_max:
#        two_max = w
#    w = int(input())
#print(two_max)

#Числа Фибоначчи
#e = int(input())
#if e == 0:
#    print(0)
#else:
#    a, b = 0, 1
#    for i in range(2, e + 1):
#        a, b = b, a + b
#    print(b)

#Максимальное число идущих подряд равных элементов


#Четные индексы
#a = input().split()
#for i in range(0, len(a), 2):
#    print(a[i])

#Больше предыдущего
#a = [int(i) for i in input().split()]
#for i in range(1, len(a)):
#    if a[i] > a[i - 1]:
#        print(a[i])

#Наибольший элемент
#index = 0
#a = [int(i) for i in input().split()]
#for i in range(1, len(a)):
#    if a[i] > a[index]:
#        index = i
#print(a[index], index)

#Шеренга
#a = [int(i) for i in input().split()]
#x = int(input())
#petya = 0
#while petya < len(a) and a[petya] >= x:
#    petya += 1
#print(petya + 1)

#Переставить соседние


#Переставить min и max


#Удалить элемент


#Вставить элемент


#Ферзи