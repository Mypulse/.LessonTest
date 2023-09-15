# Найти самый длинный период в котором держалась положиьельная тимпература 
# Например 

# -8, -7, -15, 3, 38, -4
# Ответ: 2

n = int(input("Введите период для вычислений: "))
count = 0
max_count = 0

for i in range (n):
    temp = int(input())
    if temp > 0:
        count += 1
    else:
        count = 0
    if count > max_count:
        max_count = count
print(f'Результат = {max_count}')

