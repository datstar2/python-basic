t1= (1, 2, 3)

t2 = t1*2
print(t2)

t3 = t1 +(4,5,6)
print(t3)


print(len(t3))


print(4 in t3)
print(7 not in t3)

try:
    t4 = ('apple', 'banana', 10, 20)
    t4[2] = 90
except TypeError as e:
    print('튜플은 변경 불가 - immutable')


# 튜플을 이용한 여러 값의 대입
x, y, z = 10, 20, 30

print(x, y, z)


# 튜플을 이용한 여러 값의 치환
x, y = 10, 20
print(x, y)
x, y = y, x
print(x,y)



print("================== 객체함수  ====================")
t5 = (20,30,40,50,20)
print(t5.index(50))
print(t5.count(20))



# 변환 : tuple -> set

s = set(t5)
print(t5)
