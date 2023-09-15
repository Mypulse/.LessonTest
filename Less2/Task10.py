# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# # Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# # вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# # 5 -> 1 0 1 1 0
# # 2

count = int(input("Введите колличество монет: "))
side_eagle = 0
side_tails = 0

for i in range(count):
    x = int(input('choose: eagle(1) end tails(0): '))
    if x == 1:
        side_eagle += 1
    else:
        side_tails += 1

if side_eagle < side_tails:    
    print(f'Переворачиваем {side_eagle} монет')
elif side_eagle == side_tails:
    print(f'равное колличество монет: {side_eagle}')
else:
    print((f'Переворачиваем {side_tails}'))    