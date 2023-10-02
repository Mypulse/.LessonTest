# Дан список чисел, определите сколько в нем встречается различных чисел
# input [1,1,2,0,-1,3,4,4]
# output: 6

a = [1, 1, 2, 0, -1, 3, 4, 4]
b = []

### Решение 1

# b = set(a)
# print(len(b)) 

### Решение 2 

for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(len(b))

