# 논리 bool
# 논리 자료형. 참과 거짓을 의미있는 True와 False 값을 가질 수 있음
# True나 False 모두 첫 글자는 반드시 대문자로 작성

# 파이썬에는 False는 값이 없는 모든 경우를 의미. 숫자0, 빈 문자열 '', 빈 리스트[], 등은 모두 False로 인식
print(bool(0)) # False
print(bool('')) # False
print(bool([])) # Flase
print(type(True)) # <class 'bool>

print(3 > 4) # False
print(4 < 3) # False