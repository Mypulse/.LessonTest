# Задача 16: 

# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 

# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# 5               - колличество элементов в списке 
# 1 2 3 4 5       - элементы списка   
# 3               - элемент который нужно посчитать  
# -> 1            - колличество раз которое попадается этот элемент в списке
# для этого всего есть специальный метод

# N = abs(int(input('Введите количество элементов списка А: ')))
# A_array = input("Введите элементы списка: ").split()
# A_num = list(map(int, A_array))

# if len(A_num) != N:
#     print('Введенные элементы не соответствуют заявленному количеству!')
# else:
#     X = int(input('Введите число X, которое необходимо найти в списке: '))
#     count = 0
#     for i in range(N):
#         if A_num[i] == X:
#             count += 1
#     print(f'Число {X} встречается в списке A {count} раз') 
n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))
x = int(input())
print(lst.count(x))