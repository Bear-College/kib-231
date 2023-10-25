def do_operation(a,b, operatoin):
    result=operatoin(a,b)
    print(f"result={result}")

do_operation(7,4,lambda a,b:a+b)
do_operation(9,4, lambda a,b:a*b)