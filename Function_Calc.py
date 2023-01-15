def y_generate(x):
    out = 0
    if x < 1:
        out = x
    elif x >= 1 and x < 10:
        out = 2 * x - 1
    elif x >= 10:
        out = 3 * x - 11
    return out

print(y_generate(4))

print(y_generate(6))

print(y_generate(10))
