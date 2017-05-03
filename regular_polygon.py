import turtle
def nuhelnik(cislo,strana=50):
    if cislo > 2 :
        for i in range(int(cislo)):
            turtle.forward(float(strana))
            turtle.left(180-(cislo*180-360)/cislo)
def test(n):
    for i in range(3, n+1):
        nuhelnik(i)

            
        
