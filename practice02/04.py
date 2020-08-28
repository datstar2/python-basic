# 문제4
# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요.
#
#
# 실행 결과:
# 3 짝
# 6 짝
# 9 짝
# 13 짝
# 16 짝
# 19 짝
# 23 짝
# 26 짝
# 29 짝
# 30 짝
# 31 짝
# 32 짝
# 33 짝짝
# 34 짝
# 35 짝
# 36 짝짝
# 37 짝

counts = 0

for k in range(1,100):
    if str(k).count('3') > 0 or str(k).count('6') > 0 or str(k).count('9') > 0:
        counts += str(k).count('3')
        counts += str(k).count('6')
        counts += str(k).count('9')
        print(k, '짝'*counts)
        counts = 0
    else:
        continue


