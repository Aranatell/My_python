#Planchul
a=None
v=None
b=None
r=0
while not a:
    try:
        a=int(input('Введите первое число: '))
    except ValueError as v:
        print('Некорректный ввод одного из аргументов. Просьба повторить ввод')
    
while not b:
    try:
        b=int(input('Введите второе число: '))
    except ValueError as v:
        print('Некорректный ввод одного из аргументов. Просьба повторить ввод')
while r!=1:
    c=input('Введите операнд')
    if (c== '+'):
        print(a+b)
        r=1
    elif c=='-':
        print(a-b)
        r=1
    elif c=='*':
        print(a*b)
        r=1
    elif c=='/':
            try:
                print(a/b)
            except ZeroDivisionError as D:
                print('Ошибка! Недопустимо желение на ноль!')
            else: r=1
    else:
        print('Неккоретный ввод операнда! Повторите попытку')
