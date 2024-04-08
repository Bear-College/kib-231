def my_decorator_with_params(param):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator received parameter: {param}")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

def my_decorator_with_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Decorator received function result: {result}")
        return result
    return wrapper

@my_decorator_with_params("Decorator Parameter A")
@my_decorator_with_result
def example_function_A(x, y):
    result = x + y
    print(f"Function A call with result: {result}")
    return result

@my_decorator_with_params("Decorator Parameter B")
@my_decorator_with_result
def example_function_B(x, y, z):
    result = x * y + z
    print(f"Function B call with result: {result}")
    return result

result_A = example_function_A(3, 4)
result_B = example_function_B(2, 5, 1)
