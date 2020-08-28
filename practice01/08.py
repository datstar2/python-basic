# 문제8.
# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.
#
# <<실행결과>>
#
# 입력>  Python Programming!
# 결과> !gnimmargorP nohtyP



# 함수 직접 만들어서 해보기

def reverses():
    words = list(input('입력> '))
    print("결과> ", end='')
    for k in range(len(words)-1, 0 , -1):
        print(words[k], end='')



reverses()