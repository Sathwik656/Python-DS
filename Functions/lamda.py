def is_multiple(n):
    return not n % 5

def get_multiples(n):
    return list(filter(is_multiple,range(n)))

def get_multiples_of_five(n):
    return list(filter(lambda k: not k%5, range(n)))

map(lambda *a: a, range(3))

list(map(lambda *a: a, range(3)))

list(map(lambda *a: a, range(3), 'abc'))

list(map(lambda *a: a, range(3), 'abc', range(4,7)))

list(map(lambda *a: a, (), 'abc'))

list(map(lambda *a: a, (1,2), 'abc'))

