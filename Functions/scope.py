x = 1
def foo():
    global x
    x = 11
    y = 12
    print(x)
    print(y)

def bar():
    print(f"x in bar{x}")

foo()
bar()
print(x)

# normal order
x = 1
def outer():
    x = 2
    def inner():
        x = 3
        print(f"inner sees x equal to {x}")
        return
    inner()
    print(f"outer sees x equalt to {x}")
    return
outer()
print(f"Global sees x equal to {x}")

# changing global from inner
x = 1
def outer():
    x = 2
    def inner():
        global x
        x = 3
        print(f"inner sees x equal to {x}")
        return
    inner()
    print(f"outer sees x equalt to {x}")
    return
outer()
print(f"Global sees x equal to {x}")

#changing local from inner using nonlocal
x = 1
def outer():
    x = 2
    def inner():
        nonlocal x
        x = 3
        print(f"inner sees x equal to {x}")
        return
    inner()
    print(f"outer sees x equalt to {x}")
    return
outer()
print(f"Global sees x equal to {x}")

#changing all 3 scopes (x=3) using global method
x = 1
def outer():
    global x
    x = 2
    def inner():
        global x
        x = 3
        print(f"inner sees x equal to {x}")
        return
    inner()
    print(f"outer sees x equalt to {x}")
    return
outer()
print(f"Global sees x equal to {x}")