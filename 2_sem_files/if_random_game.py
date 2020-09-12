import random
s=random.randint(1,4)
print('Введите случайное число от одного до четырёх: ')
a=int(input())
if s==a:
    print('Воу, да ты угадал!')
elif s>a:
    print('Нее, наше число побольше!')
else:
    print('Нее, наше число поменьше!')


