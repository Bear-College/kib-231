message = lambda: print("hello") 
message() 
 
square = lambda n:n * n  
 
print(square(4)) # 16 
print(square(5)) # 25 
 
def square2(n):return n * n 
 
sum= lambda a, b: a + b 
 
print(sum(4, 5))  # 9 
print(sum(5,6)) # 11 
 
def do_operation(a, b, operation):
    result = operation(a,b) 
    print(f"result = (result)") 
do_operation(5, 4, lambda a, b: a + b) 
do_operation(5, 4, lambda a, b: a * b)
