x = 4

def myfunc():
    x = 3
    print(x)        # 3
    def inner():
        nonlocal x
        x = 9
        print(x)    # 9
    inner()
    print(x)        # 9

myfunc()
print(x)            # 4
    
