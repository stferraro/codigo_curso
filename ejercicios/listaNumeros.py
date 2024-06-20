a = []
b = 0

while len (a)  != 10:
    n = float(input("introduce un valor : "))
    a.append(n)
    b += n
    
print (a)
print(b)
f = sum(a)
print(f)
c = b / len(a)
print(f'la media es {c:.2f}')
t = max(a)
print(t)
y = min(a)
print(y)
 

d = tuple(a)
print(d)