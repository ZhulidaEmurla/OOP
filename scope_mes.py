x = "global"

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        nonlocal x
        x = "global: changed!"
        print(x)

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
