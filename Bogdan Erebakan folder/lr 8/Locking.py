def multiply(n):
    def inner(m):return n+m
    return inner

fn=multiply(8)
print(fn(8))
print(fn(9))
print(fn(10))
