# 문제5.
# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

i = [10, 12, 14, 15, 17, 18, 19, 20, 25, 30, 32, 33, 37, 40, 42, 44, 46, 50]

counter = 0
sum = 0

for k in i:
    if k % 3 == 0:
        counter += 1
        sum += k
    else:
        continue
else:
    print('주어진 리스트에서 3의 배수의 개수=> %d' % counter)
    print('주어진 리스트에서 3의 배수의 합=> %d' % sum)


