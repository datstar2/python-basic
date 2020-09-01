# 기본 인수 값
def incr(a, b=1):
    return a + b


# 오류
#def incr(a=1, b):
#    return a + b


print(incr(10))
print(incr(10, b=5))
print(incr(10, 5))


# 키워드 인수
def area_rect(width, height):
    return width * height

print(area_rect(10, 20))
print(area_rect(height=20, width=10))

#가변인수

def vargs(a, *args):
    print(a, args)

vargs(10)
vargs(10, 20, 30)


def _print(*args, sep=' ', end='\n'):
    for c in args:
        print(c, end=' ')
        print(sep, end = ' ')

    print(end, end=' ')