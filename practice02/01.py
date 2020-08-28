# 문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
#
#
#
# 실행 결과:
#
# ‘usr’, ‘local’, ‘bin’, ‘python’
#
#
#
#
# 또, 디렉토리 경로명과 파일명을 분리하여 출력하세요.
#
#
#
# 실행 결과:
#
# ‘/usr/local/bin’, ‘python’
#
#
#
#  split 사용


s = '/usr/local/bin/python'
dt=s.split('/')
print(dt)
print('\'{}/{}/{}/{}\',  \'{}\''.format(dt[0],dt[1],dt[2],dt[3],dt[4]))

