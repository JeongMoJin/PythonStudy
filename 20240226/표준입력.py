# 표준입력
# input() 함수 : 표준 입력 장치(키보드)로 부터 입력받을 때 사용
# n = input('')
# print(n)
#
# n = input('정수를 입력하세요.') # 100
# print(n) # '100'
# print(type(n)) # <class 'str'> / input() 함수는 모든 입력을 '문자열 str'로 저장
# n = int(n) # 정수로 형변환
# print(type(n)) # <class 'int'>
#
# name = input('이름을 입력하세요 >>> ')
# age = input('나이를 입력하세요 >>> ')
#
# print('입력된 이름은 {}입니다.'.format(name)) # format 메서드를 이용한 출력
# print('입력된 나이는 {}살입니다.'.format(age))
#
# print(f'입력된 이름은 {name}입니다.') # f-stirng 방식
# print(f'입력된 나이는 {age}입니다.')
#
#
# float1 = float(input('첫 번째 실수를 입력하세요 >>> '))
# float2 = float(input('두 번째 실수를 입력하세요 >>> '))
# # 바로 형변환 가능
# print(f'{float1}와 {float2}의 합은 {float1 + float2}입니다.')
#
# m = int(input('1 ~ 12 사이의 월을 입력하세요 >>> '))
#
# # 리스트 사용
# days = [31, 28, 31,30,31,30,31,31,30,31,30,31]
# print(f'{m}월은 {days[m-1]}일까지 있습니다.')
#
# dic = {1: 31, 2: 28, 3: 31, 4: 29, 5: 31, 6:30, 7: 31, 8: 31, 9: 30, 10:31, 11: 29, 12:31}
# print(f'{m}월은 {dic[m]}월까지 있습니다.')

english_dict = {
    'flower' : '꽃',
'fly': '날다',
'floor': '닥'
}

eng = input('영어 단어를 입력하세요 >>> ')
print(f'{eng} : {english_dict[eng]}')

travel = input('희망하는 수학여행지를 입력하세요 >>> ')
travel2 = input('희망하는 수학여행지를 입력하세요 >>> ')
travel3 = input('희망하는 수학여행지를 입력하세요 >>> ')

print(f'조사된 수학여행지는 {set([travel, travel2, travel3])} 입니다.')




