message = lambda: print("hello") 
message() 
 
square = lambda n:n * n  
print(square(8)) 
print(square(3))  
 
sum= lambda a, b: a + b 
print(sum(0, 1))  
print(sum(-54,24)) 
 
def do_operation(a, b, operation):
    result = operation(a,b) 
    print(f"result = "+ str(result) + "") 
do_operation(5, 4, lambda a, b: a + b) 
do_operation(5, 4, lambda a, b: a * b)
