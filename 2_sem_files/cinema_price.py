#cinema_time
f=input()
d=input()
t=int(input())
s=int(input())
prc=0
ff=0

if (f=='Пятница' and t==12) or (f=='Чемпионы' and t==10):
    ff=250
elif (f=='Пятница' and t==16) or (f=='Чемпионы' and t==13) or (f=='Пернатая банда' and t==10):
    ff=350
elif (f=='Пятница' and t==20) or (f=='Пернатая банда' and (t==14 or t==18)):
    ff=450
if s>=20:
    prc+=0.2
if d=='Завтра':
    prc+=0.05
print(ff*s*(1-prc))

                               
