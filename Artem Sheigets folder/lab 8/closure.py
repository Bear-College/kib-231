def outer():
    n = 5

    def inner():
        nonlocal n
        n += 1
        print(n)
    
    return inner

fn = outer()
fn()
fn()
fn()