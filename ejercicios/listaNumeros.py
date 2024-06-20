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
j = f / len(a)

print(f'la media es {c:.2f}')
t = max(a)
print(t)

y = min(a)
print(y)

d = tuple(a)
print(d)


maxis = float('-inf')
i = 0
while i < len(d):
    if d[i] > maxis:
        maxis = d[i]
    i += 1
print(maxis)

minus = float('inf')
i = 0
while i < len(d):
    if d[i] < minus:
        minus = d[i]
    i += 1
print(minus)
    