# 산술 연산자
#
# a = 7
# b = 2
# print('{} + {} = {}'.format(a,b,a+b)) # 9 / + 덧셈
# print('{} - {} = {}'.format(a,b,a-b)) # 5 / - 뺄셈
# print('{} * {} = {}'.format(a,b,a*b)) # 14 / * 곱셈
# print('{} ** {} = {}'.format(a,b,a**b)) # 49 / ** 거듭제곱
# print('{} / {} = {}'.format(a,b,a/b)) # 3.5 / / 나눗셈
# print('{} // {} = {}'.format(a,b,a // b)) # 3 / // 몫
# print('{} % {} = {}'.format(a,b,a%b)) # 1 / % 나머지
#
# # 대입 연산자
# # a = b > b에 있는 값을 a라는 변수에 저장을 하라
# a = 10
#
# a, b = 10, 20 # 2개 이상의 변수에 저장, 튜플을 이용
# print('a = %d, b = %d' % (a,b)) # 10, 20
# print(f'a = {a}, b = {b}')
#
# a,b = b, a # 값을 교환
# print('a = %d, b = %d' %(a,b)) # 20 , 10
#
# # 복합 대입 연산자
# # 연산을 먼저 진행하고, 그 결과를 변수에 저장
# c = 10
# c = c + 10
# print(c)
# c += 10
# print(c)
#
# c -= 10 # c = c - 10
# print(c) # 20
#
# c //= 10
# print(c)
#
# c *= 10
# print(c)
#
# # 비교연산자
# # 결과 값은 True 와 False 둘 중 하나
#
# a = 15
# print(f'{a} > 10 : {a > 10}') # True. a가 10보다 크다
#
# n = int(input('10 ~ 99 사이의 정수를 입력하세요 >>> '))
# n10 = n//10
# print(f'십의 자리 : {n10}')
# print(f'일의 자리 : {n-n10*10}')
#
#
# times = int(input('초를 입력하세요 >> '))
# hour = times // 3600
# minute = times % 3600 // 60
# second = times % 60
# print(f'변환 결과는 {hour}시간 {minute}분 {second}초 입니다.')
#
# a = 10
# b = 0
# print('{} > 0 and {} > 0 : {}'.format(a,b,a>0 and b > 0)) # False / True and False
# print('{} > 0 or {} > 0 : {}'.format(a, b, a>0 or b > 0)) # True / True or False
# print('not {} : {}'.format(a, not a)) # False / 0이 아니면 True
# print('not {} : {}'.format(b, not b)) # True / 0이면 False
#
# # 시퀀스 연산자 : 순서가 있는 시퀀스 (리스트, 튜플, range, 문자열 등) 에서 사용할 수 있는 연산자
# # + : 연결하기
# # * : 반복하기
# tree = '#'
# spece = ' '
# print(spece * 4 + tree * 1)
# print(spece * 3 + tree * 3)
# print(spece * 2 + tree * 5)
# print(spece * 1 + tree * 7)
# print(spece * 0 + tree * 9)
# print('-' * 20)
#
# # 삼항 조건 연산자
# # 일반적인 삼항 조건 연산자 : 조건식 ? 참 : 거짓
# # 파이썬 삼항 조건 연산자 : 참 if 조건식 else 거짓
#
# a = 10
# b = 20
# result = (a - b) if (a >= b) else (b - a) # 조건식 a >= b은 False, b - a 실행
# print('{}과 {}의 차이는 {}입니다.'.format(a,b,result)) # 10과 20의 차이는 10입니다.
#
# sawon = int(input('4자리 사원번호를 입력하세요 >>> '))
# # sawon1 = sawon % 1000 % 100 % 10
# sawon1 = sawon % 10 # 어떤 수를 10으로 나누면, 나머지는 0~9 사이의 값이 구해짐. 일의 자리 수
# result_2 = '오전' if sawon1 >= 5 else '오후'
# print(result_2)
#
# korean = int(input('국어 점수를 입력하세요 >>> '))
# english = int(input('영어 점수를 입력하세요 >>> '))
# math = int(input('수학 점수를 입력하세요 >>> '))
# avg = float((korean + english + math)/3)
# result_3 = '합격' if avg >= 80 else '불합격'
# print(f'평균은 {avg}점이고, 결과는 {result_3}입니다.')
#

ramen = int(input('라면의 개수를 입력하세요 >>> '))
result_4 = (ramen // 20) + 1 if (ramen % 20) > 0 else ramen // 20
print(f'{ramen}개의 라면을 담으려면 {result_4}박스가 필요합니다.')









