# 문제3.
#
# 중첩 루프를 이용해 신문 배달을 하는 프로그램을 작성하세요. 단, 아래에서 arrears 리스트는 신문 구독료가 미납된 세대에 대한 정보를 포함하고 있는데, 해당 세대에는 신문을 배달하지 않아야 합니다.
#
#
# apart = [[101, 102, 103, 104], [201, 202, 203, 204], [301, 302, 303, 304], [401, 402, 403, 404]]
# arrears = [101, 203, 301, 404]
#
#
# 실행 결과:
#
# Newspaper delivery: 102
# Newspaper delivery: 103
# Newspaper delivery: 104
# Newspaper delivery: 201
# Newspaper delivery: 202
# Newspaper delivery: 204
# Newspaper delivery: 302
# Newspaper delivery: 303
# Newspaper delivery: 304
# Newspaper delivery: 401
# Newspaper delivery: 402
# Newspaper delivery: 403


apart = [[101, 102, 103, 104], [201, 202, 203, 204], [301, 302, 303, 304], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]

for ap in apart:
    for de in ap:
        if de in arrears:
            continue
        else:
            print("Newspaper delivery: {}".format(de))

