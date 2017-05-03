def vyhledat(cislo):
    delitele=[]
    for i in range(1, cislo+1):
        if cislo % i == 0:
            delitele.append(i)
    return delitele

def vyprskni(a):
    for prvek in a:
        print(prvek, end=" ")
    
    
        
