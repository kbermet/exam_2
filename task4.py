input_data = [(5, 3, 1), 5.7, 'thirteen', 10, {1: 10}]
def func(*args):
    try:
        res = sum(args)
    except KeyError:
        pass
    return res

print(func(5, 1, 7))
print(func(input_data))
