results = []

for n in [1, 2, 3, 4, 5, 6, 7 ,8]:
    result = n * n
    results.append(result)

print(results)


results = [num*num for num in [1, 2, 3, 4, 5, 6, 7, 8]]
print(results)


# 문자열 리스트에서 길이가 2 이하인 문자열 리스트 만들기

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
results = []

for s in strings:
    if len(s) <= 2:
        results.append(s)



print(results)


results = [s for s in strings if len(s) <= 2]
print(results)

# 1~100 사이의 수 중에 짝수 리스트 만들기

results = [k for k in range(1, 101) if k % 2 ==0]
print(results)

# 문자열 리스트에서 각각의 문자열의 길이를 담은 리스트 만들기

results = [len(k) for k in strings]
print(results)
# 369게임 : 1~100 사이에 3, 6, 9 가 있는 수 리스트 ㅁ나들기
results = [num for num in range(1, 101) if str(num).count('3') > 0 or str(num).count('6') > 0 or str(num).count('9') > 0]
print(results)


# set comprehension
results = {len(k) for k in strings}
print(results)


# dict comprehension
results = {v: s for v, s in enumerate(strings) if len(s) <= 2}
print(results)


