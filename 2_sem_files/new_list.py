#3_lists
from math import sqrt 
a=[2,4,9,16,25]
#1
b=[]
for i in range(len(a)):
    print(a[i])
    b.append(sqrt(a[i]))
print(b)
#2
c=map(sqrt,a)
print(list(c))
#3
print( list (sqrt(i) for i in a))

