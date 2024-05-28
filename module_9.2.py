def create_operation(operation):
    if operation == "div":
        def div(x, y):
            return x / y

        return div
    elif operation == "multiply":
        def multiply(x, y):
            return x * y

        return multiply


print("Задача номер 1")
function_div = create_operation("div")
print(function_div(6, 2))
function_multiply = create_operation("multiply")
print(function_multiply(6, 2))

print("Задача номер 2")
square = lambda x: x * x
print(square(6))


def square(x):
    return x * x


print(square(6))

print("Задача номер 3")


class React:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f'стороны: {x}, {y}')

    def __call__(self):
        return f'площадь: {self.x * self.y}'


my_count = React(5, 6)
print(my_count())
