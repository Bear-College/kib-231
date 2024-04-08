def create_user(username, is_admin=False):
    return {"username": username, "is_admin": is_admin}

def admin_required(input_function):
    def wrapper(user, *args, **kwargs):
        if user["is_admin"]:
            result = input_function(user, *args, **kwargs)
            return result
        else:
            print("Недостатньо прав для виклику функції.")

    return wrapper

@admin_required
def admin_operation(user, message):
    print(f"Операція користувача {user['username']}: {message}")

regular_user = create_user(username="Yaroslav")
admin_user = create_user(username="Nezox", is_admin=True)

admin_operation(regular_user, "не спрацює")

admin_operation(admin_user, "Перемога")