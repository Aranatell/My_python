a=[int(s) for s in input().split()]
c=[]
for i in range(len(a)-4):
    b=[a[(i+j)] for j in range(5)]
    if sum(b)>sum(c):
        c=b
print(c)
