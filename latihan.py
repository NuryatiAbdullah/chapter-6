from math import ceil

def isPythagoras(a, b, c):
    if (c**2) == (a**2) + (b**2):
        return True
    return False

def starFormation1(n):
    i = 0
    while i < n:
        i+=1
        print("*"*i)

def starFormation2(n):
    while n:
        print('*'*n)
        n-=1

def starFormation3(n):
    starFormation1(int(n / 2))
    if n / 2 > int(n / 2):
        print('*' * ceil(n / 2))
    starFormation2(int(n / 2))

def faktorial(n):
    if n > 2:
        return n * faktorial(n - 1)
    return n

print(faktorial(10))
