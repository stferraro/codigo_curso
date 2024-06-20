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

max = float('-inf')
i = 0
while i < len(d):
    if d[i] > max:
        max = d[i]
    i += 1
print(max)

min = float('inf')
i = 0
while i < len(d):
    if d[i] < min:
        min = d[i]
    i += 1
print(min)
    