def outer():
    n = 1

    def inner():
        nonlocal n
        n += 1
        print(n)
    
    return inner

fn = outer()
fn() #2
fn() #3
fn() #4