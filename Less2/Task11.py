# # Дано натуральное число А > 1. Определите, каким по счету числом Фибоначи оно является, 
# # т.н. введите такое число n, что f(n) = A. Если А не является числом Фибоначи, выведите -1.  

# Элементы числовой последовательности 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711

# Пример: 
# # input: 5 
# # Output: 6

n = int(input("Введите число: "))
n0 = 0 #Данное значение будет выполнять поверку, которая указана в цикле While (По сути это последующие число Фибоначи, которое мы будем находить.
# в нашем случее оно третье, т.к. первые два уже известны (a0 и a1)).
a0 = 0 # Заведем начальное значение 
a1 = 1 # Равна также еденице
i = 2 #  i равно 2, потому что первые два числа Фибоначи нам уже известны (a0 и a1)
while n0 < n:  # Как только n0 привысит значение n - это будет означать, что такого числа Фибоначи нет! (Пока n0 меньше n, мы будем выполнять блок кода, указанный ниже.) Если нутри этого блока
# встретилось такое условие, что n0 оказалось больше чем n (строка 22), то в данном случае такое число не может являтся числом Фибоначи и мы указываем что i = 0.     
    n0 = a0 + a1 # Далее мы ищем каждое последующее число Фибоначи, которое равно сумме двух предидущих. 
    a0 = a1 # При этом нам необходимо выполнить замену 
    a1 = n0 # писвоем занечине а0 переменной а1 и так же значение а1 присвоем переменной n0, тем самым бедет искаться значение, которое нам необходимо.
    i += 1 # Переменную i будем при каждой итерации увеличивать на 1, потому что мы переходим уже к следующему числу фибоначи. 
    if n0 > n: # Далее указываем, если число n0 привысело число n внутри програмного кода, который указан выше.  
        i = 0  # То в данном случае мы указываем, что i = 0, а цикл будет завершен самостоятельно. 
if i  != 0: # Далее проверяем, если значение i не было равно нулю, значит мы отыскали необходимое для нас число.          
    print(i) # Выводим i
else:             # В любом другом случае: 
    print(-1)  #  Выводим -1 
    

