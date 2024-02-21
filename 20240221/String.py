# 문자열 str
# 문자열 자료형. 기본적으로 따옴표로 묶어서 데이터를 표현
# 문자열을 한 글자이거나 여러 글자여도 작은 따옴표(')와 큰 따옴표(")를 모두 사용할 수 있음
# 각 따옴표를 3개씩 사용하는 삼중 따옴표(''' ''', """ """)도 사용할 수 있음
# single line : 한 줄의 문자열 : 작은 따옴표(')와 큰 따옴표(")
# multiple line : 여러 줄의 문자열 : 삼중 따옴표(''' ''', """ """)

# 문자열 변환
# str() 함수를 사용하면 다른 자료형의 값을 문자열 데이터로 변환 할 수 있음
print(str(100)) # '100' / 정수 100을 문자열 '100'으로 변환
print(str(True)) # 'True' / 논리 True를 문자열 'True'로 변환
print(str(False)) # 'Flase' / 논리 False를 문자열 'False'로 변환
print(type(str(3.14))) # <class 'str'> '3.14' / 실수 3.14를 문자열 '3.14'로 변환

# 문자열 인덱싱 indexing
# 0번 부터 시작
print()
s = 'hello'
print(s[1]) # e
# 마이너스(-) 인덱스는 문자열 뒤에서 부터 부여, 마지막 인덱스는 -1이 됨
print(s[1] == s[-4]) # True

# 문자열 슬라이싱 slicing
# 문자열 인덱스를 활용하여 한 문자 이상으로 구성된 단어나 문장을 추출 할 때 사용
# s[start:stop:step]
# start : 시작 인덱스를 지정. 생략하면 처음부터 추출
# stop : 종료 인덱스를 지정. 생략하면 끝까지 추출
# step : 인덱스의 증감값. 생략하면 1씩 변화

print()
s= 'banana'
print(s[0:3])
print(s[0:6:2])












