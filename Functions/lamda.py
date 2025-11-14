def is_multiple(n):
    return not n % 5

def get_multiples(n):
    return list(filter(is_multiple,range(n)))

def get_multiples_of_five(n):
    return list(filter(lambda k: not k%5, range(n)))

    