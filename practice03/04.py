# 문제4
# 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다. 프로그램은 정답 여부를 다시 출력합니다.
#
# 실행 결과:
# 4 X 2 = ?
#
# 18	9	7
# 63	54	35
# 8	28	81
#
# answer: 8
# 정답
#
# Process finished with exit code 0

import random


a = random.randrange(1,10)
b = random.randrange(1,10)

print("{} X {} = ?".format(a, b))

c = a * b
print('')
k = []
i = 0
while i < 8:
    g = random.randrange(1, 10) * random.randrange(1,10)
    if g == c:
        continue
    else:
        k.append(g)
    i += 1

k.append(c)

random.shuffle(k)

j = tuple(k)
print('{0} {1} {2}'.format(j[0], j[1], j[2]))
print('{0} {1} {2}'.format(j[3], j[4], j[5]))
print('{0} {1} {2}'.format(j[6], j[7], j[8]))








