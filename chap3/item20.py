def careful_divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('Invalid inputs')

x, y = 0, 5
try:
    result = careful_divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print(f'result is ${result}')