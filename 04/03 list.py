# 생성
l1 = []
l2 = [1, True, 'Python', 3.14]

# 인덱싱(sequence 타입 특징)

print(l2[0], l2[1], l2[2], l2[3])
print(l2[-4], l2[-3], l2[-2], l2[-1])

#slicing
print(l2[1:4])
print(l2[:])
print(l2[2:])
print(l2[3::-1])

# 반복(sequence 타입 특징)
l3 = l2 * 2
print(l3)

# 연결(sequence 타입 특징)

l4 = l2 + [1, 2, 3]
print(l4)

#길이(sequence 타입 특징)
print(len(l4))

# in, not in(sequence 타입 특징)
print(5 not in l4)
print('python' in l4)

# 삭제(변경 가능한 객체)
del l4[2]
print(l4)


# 변경 가능한 객체(mutable)
l5 = ['apple', 'banana', 10, 20]
print(l5)
l5[2] = l5[2] + 90
print(l5)


# 삭제(slicing을 이용한..))

l6 = [1, 1, 123, 1234]
l6[0:2] = []
print(l6)


# 삽입(sliceing을 이용한..))
l7 = [1, 12, 123, 1234, 12345]

# 중간 삽입
l7[1:1] = [2, 23]

print(l7)

# 마지막 삽입

l7[7:] = [2324,35435]
print(l7)

# 처음 삽입
l7[:0] = [23545,25667]
print(l7)
# 삭제, 치환, 삽입,

# 치환(slicing을 이용한...)

l8 = [1, 12, 123 , 1234, 123456]
print(l8)

l8[0:2] = [10,20]
print(l8)

l8[0:2] = [100]
print(l8)

l8[1:2] = [200]
print(l8)

l8[2:4] = [300, 400, 500, 600]
print(l8)


print("============ 객체함수 ===============")
l9 = [1, 3, 4]

# 중간함수


#마지막 삽입
l9.append(5)
print(l9)


# 처음삽입
l9.insert(0, 0)
print(l9)

# 반전 reverse
l9.reverse()
print(l9)

# 삭제  remove = 값을 삭제 / 동질한 객체를 삭제한다.
l9.remove(3)
print(l9)

# 없는 객체 삭제할 경우

try:
    l9.remove(3)
except ValueError as e:
    print('없는 객체 삭제할 경우 예외 발생')


# 확장
l9.extend([-1, -2, -3, -4, -5])
print(l9)


# stack
stack = []
stack.append(10)  # push
stack.append(10)  # push

print(stack)
print(stack.pop())
print(stack.pop())

print(stack)


# queue 로 사용해보기

q = [1, 2]
q.append(3)
q.append(4)
q.append(5)
print(q)


print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
print(q)

# sort
l10 = [1, 5, 3, 9, 8, 11]
l10.sort()
print(l10)

l11 = [10, 2, 33, 9, 8, 4, 11]
l11.sort(key=str)
print(l11)

l11.sort(key=int)
print(l11)

# cf : sorted 전역함수    ,,  객체함수?
l12 = [19 , 46, 7, 28, 91, 55, 64]
l13 = sorted(l12)
print(l13)


def f(i):
    return i % 10


l14 = sorted(l12, key=f, reverse= False)
print(l14)