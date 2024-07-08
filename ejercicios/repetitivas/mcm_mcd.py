def mcm(a, b):
    return (a * b) // mcd(a, b)



def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)
    
a = 10
b = 5
print(mcm(a, b))