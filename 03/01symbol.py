# 심볼 테이블 내용확인
g_a = 1
g_b = 'symbol'

def f():
    l_a = 2
    l_b = 'table'
    print(locals())

for i in range(10):
    g_c = 3
    g_d = 'python'
    print(locals())

f()
print(globals())

#1. 정의된 함수

f.n = 'hello'
f.i = 10
print(f.__dict__)

# 2. 클래스
class MyClass:
    def __init__(self):
        self.i = 10   #인스탄스 객체
        self.j = 20

    x = 10 #클래스 객체체
    y  10


MyClass.z = 10
print(MyClass.__dict__)

#3. 내장함수
# 심벌테이블 X -> 확장 X
#print.z = 10
# print(print.__dict__)


#4. 내장 클래스
#심벌테이블 o -> 확장 x
# str.z = 10
print(str.__dict__)

#5. 사용자 정의 클래스로 생성된 객체
# 심벌테이블 o -> 확장 o
o = MyClass()
o.k = 30
print(o.__dict__)

6. 내장 클래스로 생성된 객체
# 심벌테이블 x -> 확장 x
# g_a_





