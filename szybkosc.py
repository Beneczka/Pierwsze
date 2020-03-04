import time

def czas(f, n):
    wynik=[]
    for e in n:
        t0=time.time()
        w=f(e)
        t1=time.time()
        wynik.append(t1-t0)
    return wynik

def silnia1(n):
    if n is not 1:
        return n*silnia1(n-1)
    else:
        return 1
def silnia2(n):
    wynik=1
    for e in range(1, n+1):
        wynik*=e
    return wynik

def Fib_rek(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return Fib_rek(n-1)+Fib_rek(n-2)

def Fib_it(n):
    wynik=0
    a=0
    b=1
    if n == 0:
        return 0
    else:
        for e in range(1, n):
            wynik=a+b
            a=b
            b=wynik
        return wynik

#print(Fib_rek(3), Fib_it(3))
print("Czas wykonywania pierwszej funkcji:", czas(Fib_rek, [10, 35]))
print("Czas wykonywania drugiej funkcji:", czas(Fib_it, [10, 35]))
