# 문제4.
# 다음과
# 같은
# 출력이
# 되도록
# 구구단을
# 작성하세요.(이중 for ~ in)


for m in range(1, 10):
    for n in range(1, 10):
            if n == 9:
                print('{} X {} = {}'.format(n, m, n*m))
            else:
                print('{} X {} = {}'.format(n, m, n*m), end='\t')