# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

# a1=int(input("Enter the first element: "))
# num=int(input("Enter the number of elements: "))
# d=int(input("Enter step: "))
# res =[]
# for i in range(1,num+1):
#       res.append(a1+(i-1)*d)
# print(res)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# сделала через генератор списков, чтобы учитывалось каждое вхождение элемента

# import random
# arr=[random.randint(-20,21) for i in range(10)]
# print(arr)
# a=int(input("Enter the minimum value: "))
# b=int(input("Enter the maximum value: "))
# res=list(filter(lambda x: a<=x and x<=b ,arr))
# print(res)
# ind=[i for i in range(0,len(arr))if arr[i] in res]
# print(ind)


