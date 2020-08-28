# 문제9.
# 주어진 if 문을 dict를 사용해서 수정하세요.
#
#
#
# #
menu = input('메뉴: ')

menup_dic={'오뎅' : 300 , '순대': 400, '만두': 500}

print('가격: {0}'.format(menup_dic.get(menu)))

## menu_dic = {}  << 딕셔너리 활용, get함수 활용