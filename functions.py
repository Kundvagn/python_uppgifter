# double(n)
# Funktionen double(n) tar ett heltal n som argument och skall returnera det dubbla värdet av n.

# triple(n)
# Funktionen triple(n) tar ett heltal n som argument och skall returnera det trippla värdet av n.

# quadruple(n)
# Funktionen quadruple(n) tar ett heltal n som argument och skall returnera det 
# kvadrupla värdet av n. För att beräkna returvärdet måste du använda funktionen double(n) två gånger.

# funky(n, m)
# Funktionen funky(n, m) tar två heltal n och m som argument och skall returnera det trippla värdet av n plus det 
# kvadrupla värdet av m. För att beräkna returvärdet måste du använda funktionerna triple(n) och quadruple(n).

def double(n):
    return 2*n

def triple(n):
    return 3*n

def quadruple(n):
    return 4*n

def funky(n, m):
    return triple(n) + quadruple(m)

a = 3
b = 14

d1 = double(a)       # 6
d2 = double(b)       # 28

t1 = triple(a)       # 9
t2 = triple(b)       # 42

q1 = quadruple(a)    # 12
q2 = quadruple(b)    # 56

f1 = funky(a, b)     # 65
f2 = funky(b, a)     # 54

print(d1)
print(d2)
print(t1)
print(t2)
print(q1)
print(q2)
print(f1)
print(f2)