# 문제2. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.
#
#
s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""
#
# ###실행결과
#
#         Click
#         Here
#
#         	     To connect to the most powerful tools  in the world.
#




s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

k = s.split(">")

a= k[3][:5]
b= k[5][:4]
c= k[7][:-3]

print(a)
print(b)
print(c)

