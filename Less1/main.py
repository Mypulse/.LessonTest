n = int (input("Введите трёхзначное число :"))

while n < 100 or n > 999:
    n = int (input("Вы ошиблись! Введите трёхзначное число :"))
print(n)
n1 = n // 100
n2 = (n % 100) // 10
n3 = n % 10
print(n1 + n2 + n3)
