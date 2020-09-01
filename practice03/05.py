# 문제5.
# 선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
# 문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를 크기 순서대로 정렬하여 다음과 같은 출력이 되도록 완성하는 문제입니다.
#
#
# <<실행결과>>
#
# Before Sort.
# 5 9 3 8 60 20 1
# After Sort.
# 60 20 9 8 5 3 1



j = [ 5, 9, 3, 8, 60, 20, 1 ]


def sss(y):
    z = 0
    for l in range(0, len(y)-2):
        for k in range(l, len(y)-1):
            if j[l] < j[k+1]:
                z = j[l]
                j[l] = j[k+1]
                j[k+1] = z
    return y

print(sss(j))



