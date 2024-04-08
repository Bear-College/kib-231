def create_user(input_function):
    def output_function(*args):
        login = args [0]
        password = args [1]
        if password == 123:
            password = 12345678
        input_function(login, password)
    return output_function

@create_user
def user_info(login, password):
    print(f"Логін: {login} \t Пароль: {password}")

user_info("Dima","abcd123")
user_info("Dima", 123)

def check_to_parity(input_function) :
    def output_func(*args):
        result = input_function(*args)
        if result == 0: result = "Так"
        else: result = "Ні"
        return result
    return output_func

@check_to_parity
def op(a):
    return a%2

result1 = op(14)
print(result1)

result2 = op(11)
print(result2)    



