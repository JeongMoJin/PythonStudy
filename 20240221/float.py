# 실수 float
# 소수점이 있는 숫자를 실수 (floating point number)라고 함

# float() 함수를 이용하면 다른 자료형의 값을 실수형 데이터로 변환 할 수 있음
print(float(1)) # 1.0 / 정수 1을 실수 1.0으로 변환
print(float(True)) # 1.0/ True는 1.0으로 변환
print(float(False)) # 0.0 / False는 0.0으로 변환
print(float('3.14')) # 3.14 / 문자열 '3.14'를 실수 3.14로 반환
print(float('100')) # 100.0 / 문자열 '100'을 실수 100.0으로 반환
print(type(3.14)) # <class 'float'>

# 실수의 연산은 부정확
print(0.1 + 0.2) # 0.30000000000000004