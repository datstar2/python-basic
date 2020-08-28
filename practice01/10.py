# 문제10
# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.
#
# a. 입력 받은 숫자가 홀수인 경우에는, 0 부터 입력 값까지 홀수의 합을 출력합니다.
# - 예제 : 입력이 7 이면 16을 출력 ( 1 + 3 + 5 + 7 = 16 )
# b. 입력 받은 숫자가 짝수인 경우에는, 0 부터 입력 값까지 짝수의 합을 출력합니다.
#     - 예제 : 입력이 10 이면 30을 출력 ( 2 + 4 + 6 + 8 + 10 = 30 )

#
# 실행 결과:
#
# 숫자를 입력하세요: 7
# 결과 값 : 16
#
# 숫자를 입력하세요: 10
# 결과 값 : 30
#
# 숫자를 입력하세요: 11
# 결과 값 : 36


num = int(input('숫자를 입력하세요: '))

sum = 0
if num % 2 == 0:
    for k in range(1,num+1):
        if k % 2 == 0:
            sum += k
        else:
            continue
else:
    for k in range(1,num+1):
        if k % 2 != 0:
            sum += k
        else:
            continue
print('결과 값 : %d' % sum)