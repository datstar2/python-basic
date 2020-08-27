# 한줄 문자열
s = ''
str1 = 'Hello World'
str2 = "Hello World"
print((type(s)), type(str1), type(str2))

# 여러줄 문자열

str3 = 'ABC\ndDEF\n가나다라마바사\n아자차카타파하'
print(str3)


print("======== 문자열 연산 ==========")
s1 = "First String"
s2 = "Second String"

# 반복
s3 = s1*3
print(s3)

# + 연결  LIKE concat

#인덱싱
print(s1[0], s1[1], s1[2])
print(s1[-12], s1[-11], s1[-10])

# slicing
s7 = s1[2:5]
print(s7)
print(s1[2:])


# 문자열 객체와 정수 객체는 연결(+) 연산을 할 수 없다.
# 예외 : 발생
# print("hello" + 2)

print('hello' + str(2))

# in, not in 연산자 (sequence 타입이 가지는 특징)
print('s' in s2)
print('s' not in s2)


print('======== 포맷팅 ==========')
# tuple
f = "name : %s, age : %d"
print(f % ('둘리', 10))

# format() 함수
name = '마이콜'
age = 30
print("name: " + format(name, 's') + ',age:  ', format(age, 'd'))


print('============== 객체함수 ==================')
s8 = 'i like Python'
print(s8.upper())
print(s8.lower())
print(s8.swapcase())
print(s8.capitalize())
print(s8.title())
s9 = '1234567'
print(s9.isdigit())

s9 = 'I Like Python, I Like Java Also '

print(s9.count('Like'))
print(s9.find('Like'))
print(s9.find('Like', 5))
print(s9.find('Javascript'))
print(s9.rfind('Like'))



# str 객체는 변경할 수 없다
# s10 = "Hello"


#cf list는 변경 가능하다
l1 = ['hello', 'world']
print(l1)
l1[0] = 'HELLO'
print(l1)
l1.append('Python')
print(l1)