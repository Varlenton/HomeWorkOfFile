def add_everything_up(a, b):
    try:
        summed = a + b
        return summed
    except TypeError:
        summed = str(a) + str(b)
        return summed


print(add_everything_up(10, 'word'))
print(add_everything_up(10, 10))
print(add_everything_up('world', 10.5))
