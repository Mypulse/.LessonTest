# Task9

# Найти факториал числа с помощью цикла while 

# Пример:

# input: 5 
# Output: 120

n = int(input("Введите число: "))
i = 1
result = 1

while i <= n:
    result *= i
    i += 1
print(f'{n}! = {result}') # Факториал числа "n" равен ... через f-строку
 



