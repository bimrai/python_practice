// practicing returning multiple values

def f():
    a = 5
    b = 6
    c = 7
    # return a, b, c
    return {'a': a, 'b': b, 'c': c}

a, b, c = f()

return_tuple = f()
print(a, b, c)
print(return_tuple)

pull_six = f()
print(pull_six['b'])
