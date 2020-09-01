def func1(a):
    x = 10
    return a + x


def func2(a):
    return a + x


def func3(a):
    return a + y




x = 1
g = 10

# LGB
r = func1(10)
print(r)
print(x)

# LGB  local에 없을시 글로벌에서 찾는다
r = func2(10)
print(r)

# LGB
print('__builtins__')

