# for ~ in 반복문
# for in [sequence 객체]  :
for number in [10, 20, 30, 40]:
    result = number**2
    print(result, end=' ')
else:
    print('')

a = ['cat', 'cow', 'tiger']
for animal in a:
    print(animal, end=' ')
else:
    print('')


i = [('둘리', 10), ('마이클', 30), ('또치', 11)]

for t in i:
    print('이름 : %s, 나이 : %d' % t)
else:
    print('')

# 10번 반복 루프

for i in range(1, 11):
    print(i, end=' ')
else:
    print()


# 1~ 10까지 합을 구하기
sum = 0

for i in range(1, 11):
    sum += i
else:
    print(sum)


# break

for n in range(10):
    print(n, end=' ')
    if n == 5:
        break
else:
    print('\n-------------------------')


# break
for n in range(10):
    if n > 5:
        continue
    print(n, end=' ')
else:
    print('\n-------------------------')


