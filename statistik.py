def sum(*n):
    res = 0
    for i in n:
        res+=i
    return res
    
def average(*n):
    ttl = len(n)
    res = 0
    for i in n:
        res+=i
    return res / ttl

def maks(*n):
    hsl = 0
    for i in n:
        hsl = i if i > hsl else hsl
    return hsl

def min(*n):
    hsl = n[0]
    for i in n:
        hsl = i if i < hsl else hsl
    return hsl


