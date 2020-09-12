#BIG_LIST_func

def rwf():
    from random import randint as rr
    a=[]
    ff=0
    for i in range(1000):
        a.append(rr(-1000,1000))
        if i==0:
            mx=a[-1]
            if a[-1]<0:
                ff=1
        if i==1:
            (mn, mx)=(min(mx,a[-1]), max(mx,a[-1]))
            if a[-1]<0:
                ff+=1
        if i>1:
            if max(a[-1],mx)==a[-1]:
                mx=a[-1]
                if a[-1]<0:
                    ff+=1
            if min(a[-1],mn)==a[-1]:
                mn=a[-1]
                if a[-1]<0:
                    ff+=1
            if mx-a[-1]>=mn:
                if a[-1]<0:
                    ff+=1
    return(ff)
print(rwf())
    
