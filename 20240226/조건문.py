# 조건문

# 1. if 문
# if 조건식 :
#       조건식의 결과가 True 일 때 실행문

num = 15
if num > 0:
    print('양수') # 조건식이 True라서 실행이 됨

# 들여쓰기 indentation 규칙
# 1. 공백 space이나 탭 tab을 이용하여 들여쓰기를 수행
# 2. 공백의 개수는 상관이 없음
# 3. 탭은 1개만 사용
# 4. 동일 구역에서 들여쓰기는 통일해야 함. 공백과 탭을 혼용해서 사용불가
# 들여쓰기 수준도 동일해야 함
# 5. 주로 사용하는 들여쓰기는 공백 4개, 공백 2개, 탭 1개.

if num > 0: print('양수') # 실행문이 하나면 한 줄 코드 가능

# 2. if-else 문

print()
num = -1
if num >= 0:
    print('양수')
else:
    print('음수')

# 3. if-elif 문
print()
important = 56

if important >= 100:
    print('상')
elif important >= 50:
    print('중')
else:
    print('하')
    

age = int(input('몇 살입니까? >>> ')) # int() 함수를 이용해서 정수로 변환
if age <= 7:
    print('미취학')
elif age <= 13:
    print('초등학생')
elif age <= 16:
    print('중학생')
elif age <= 19:
    print('고등학생')
else:
    print('성인')