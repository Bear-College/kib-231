def countdown():
    n = 4
    def count():
        nonlocal n
        n -= 1
        print(n)
    
    return count

c = countdown()

c()
c()
c()

def sum(n): 
    def plus(m): return n+m
    return plus

op = sum(6)

print(op(4))
print(op(7))

def minus(n):return lambda m: n-m

min = minus(9)

print(min(6))
print(min(3))  