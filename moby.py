with open('moby.txt','r') as file:
    b= [a.split() for a in file]
    for i in b:
        print(i.strip())
    
        
        
    
