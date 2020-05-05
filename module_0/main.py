# Программа "Угадай число" - компьютер загадывает случайно число от 1 до 100, а написанный алгоритм должен его угадать
# c 10 попыток 
# Задачу будем решать методом половинного деления интервалов 

range_max = 100
from random import randint, seed
num_of_attempts = 10
number = None
seed()
# Компьютер загадал число:
num_comp = randint(1, range_max);


def median(x1,x2):
# Функция medians возвращает среднее арифметическое между числами x1 и x2      
    return x1+int((x2-x1)/2)

 
num1 = 1
num2 = range_max
for j in range(1, num_of_attempts + 1):
    number = median(num1,num2)    
    if number > num_comp:
        num2 = number 
    elif number < num_comp:
        num1 = number
    else:
        print('Вы выиграли! Загаданнное компьютером число:', num_comp, 'совпало с найденным:', number, 'с', j, 'попыток')
        break
    if num_of_attempts == j:
        print('Количество попыток исчерпано!')
        break