#another_one_function
import math
def f_sin(a):
    if 0.2<=a<=0.9:
        return(math.sin(a))
    else:
        return(1)
a=float(input())
print(f_sin(a))
