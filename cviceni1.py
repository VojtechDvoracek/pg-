def add(a, b):
    c = a + b
    print(c)
    return c

def mul(a,b,c):
    y=a*b*c
    return y

def div(a,b):
    if b==0:
        return 0
    else:
        z=a/b
        return z
def delennibezezbytku(a,b):
    if a%b==0:
        return "je delitelne bezezbytku"
    else:
        return "neni delitelne bezezbytku"
def je_delitelne_3(a):
    if delennibezezbytku(a,3) == "je delitelne bezezbytku":
        return "je delitelne 3"
    else:
        return "neni delitelne 3"

if __name__ == "__main__":
    print("Hello World!")
    add(1,2)
    x= mul(1,2,3)
    print(x)
    a=div(10,0)
    print(a)
    b=delennibezezbytku(10,3)
    print(b)
    vysledek= je_delitelne_3(10)
    print(vysledek)