message = lambda: print("hello") 
message() 
 
square = lambda n:n * n  
print(square(10)) # =100 
print(square(9)) # =81 
 
sum= lambda a, b: a + b 
print(sum(0, 1))  # =1
print(sum(-25,24)) # =-1 
 
def do_operation(a, b, operation):
    result = operation(a,b) 
    print(f"Результат = "+ str(result) + "") 
do_operation(5, 4, lambda a, b: a + b) 
do_operation(5, 4, lambda a, b: a * b)
