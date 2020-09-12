#smth_about_smth(lesson_5)
#Программу сделал немного иначе: в случае поражения мне было крайне лень перезапускать игру снова и снова, а потому вы играете до победного конца!
import random

ff=0
while ff==0:
    a=['Самовар','Весна','Лето']
    q= a[random.randint(0,len(a)-1)]
    w=random.randint(0,len(q)-1)
    print(q[:w]+'?'+q[w+1:])
    r=input()
    if r==q[w]:
        print('Да, ты прав!')
        ff=1
    else:
        print('нет, увы, пробуй еще!')

    

