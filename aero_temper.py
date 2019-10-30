f=dict()
a=open('temper.txt','r')
b=[line.strip() for line in a]
mx=-1000
mn=1000
su=0
for i in b:
    mx=max(mx,float(i))
    su+=float(i)
    mn=min(mn,float(i))
    if f.get(i,'qq')=='qq':
        f[i]=1
    else:
        f[i]+=1
    
    
print(f)
print(su/len(b))
print('max = ', mx, 'min = ',mn)
a.close()
