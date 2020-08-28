# enumerate() 함수 사용하기


index = 0
for color in ['red', 'yellow', 'blue', 'black', 'gray']:
    print(index, color)
    index = index + 1

for i, value in enumerate(['red', 'yellow', 'blue', 'white', 'gray']):
    print('{0}: {1}'.format(i, value))




#zip() 사용 예

seq1 = {'foo', 'bar', 'baz'}
seq2 = {'one', 'two', 'three'}
z = zip(seq1, seq2)
print(z)
print(type(z))


for t in z:
    print(t)





