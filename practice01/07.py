# 문제 7.
# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
#
# <<실행결과>>
#
# > 1
# > 2
# > 3
# > 4
# > 5
# 평균: 3.0

sums=0

numbers = [int(input(i)) for i in range(0, 5)]

for k in numbers:
    sums += k

print('평균 : {}'.format((sums/5)))