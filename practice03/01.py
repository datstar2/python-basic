# 문제1. 다음 세 개의 리스트가 있을 때,
#
# subs = [‘I’, ‘You’]
# verbs = [‘Play’, ‘Love’]
# objs = [‘Hockey’, ‘Football’]
#
# 3형식 문장을 모두 출력해 보세요
#
# 실행 결과:
#
# I Play Hockey.
# I Play Football.
# I Love Hockey.
# I Love Football.
# You Play Hockey.
# You Play Football.
# You Love Hockey.
# You Love Football.
#

subs = ['I', 'You']
verbs = ['Play','Love']
objs = ['Hockey', 'Football']

for s in subs:
    for v in verbs:
        for o in objs:
            print(f'{s} {v} {o}.')














