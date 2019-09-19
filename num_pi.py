#Pi_num
import math
def f_Pi(c):
    return('{:.{c}f}'.format(math.pi , c=c))
a=int(input())
print(f_Pi(a))
