# # 1. 문자열 메소드
# # 문자열 str을 처리하기 위해 많은 메소드를 제공
#
# # 1) format()
# # 정렬 옵션
# # < : 지정된 공간 내에서 왼쪽 정렬
# # > : 지정된 공간 내에서 오른쪽 정렬
# # ^ : 지정된 공간 내에서 가운데 정렬
#
# # 10d는 10자리의 필드 폭을 의미
# print("10자리 폭 왼쪽 정렬 '{:<10d}'".format(123)) # 10자리 폭 왼쪽 정렬 '123    '
#
# # 2) count()
# # 문자열 내부에 포함된 특정 문자열의 개수를 반환하는 메소드
#
# print()
# s = '내가 그린 기린 그림은 목 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다'
# print(s.count('기린')) # 4
#
# # 인덱스를 지정해서 범위를 지정할 수 있음
# s = 'best of best'
# print(s.count('best', 5)) # 1 / 인덱스 5번부터 검색
#
# # 마이너스 인덱스를 사용할 수 있음
# s = 'best of best'
# print(s.count('best', -7)) # 1 / -7 인덱스인 o 부터 검색
#
# # 3) find()
# # 문자열 내부에 포함된 특정 문자열을 찾고자 할 때 사용
# # 찾고자 하는 문자열이 있으면 그 문자열이 처음으로 나온 위치 즉 인덱스 index를 반환
# print()
# s = 'apple'
# print(s.find('p')) # 1
#
# # 찾는 문자열이 없는 경우 -1 반환
# s = 'apple'
# print(s.find('z')) # -1
#
# if s.find('z') == -1:
#     print(s)
#
# # find() 메소드와 착는 방향이 다른 rfind() 메소드
# # right와 find를 합친 이름으로 오른쪽부터 찾음
# s = 'best of best'
# print(s.rfind('best')) # 8
#
# # 4) index()
# # find() 메소드와 같은 역할을 수행하며 사용방법도 동일. 두 메소드의 차이점은 문자열이 없을 때 발생
# # find() 메소드는 찾는 문자열이 없는 경우 -1을 반환, index() 메소드는 오류 발생
# print()
# s = 'apple'
# print(s.index('p')) # 1
# # print(s.index('z')) # ValuesError : substring not found
#
# # 5) 대소문자 변환 메소드
# # upper : 모두 대문자로 변환한 결과를 반환
# # lower : 모두 소문자로 변환한 결과를 반환
# # capitalize : 첫 글자는 대문자로 변환하고 나머지는 소문자로 변환한 결과를 반환
# print()
# s = 'BEST of best'
# print(s.upper()) # BEST OF BEST
# print(s.lower()) # best of best
# print(s.capitalize()) # Best of best
#
# # 6) join()
# # 인수로 전달한 반복가능객체의 각 요소 사이에
# # 문자열을 포함시켜 새로운 문자열을 만들고 그 결과를 반환
# print()
# print('-'.join('python')) # p-y-t-h-o-n
#
# # 7) split()
# # 하나의 문자열을 여러 개의 문자열로 분리해서 저장한 리스트를 반환
# print()
# s = 'Life is too short'
# s2 = s.split() # split() 메소드에 아무 인수도 전달하지 않으면 공백문자를 기준으로 각 문자열이 분리
# print(s2) # ['Life', 'is', 'too', 'short']
#
# s = '010-1234-5678'
# s2 = s.split('-') # 공백대신 특정 문자열을 기준으로 분리하는 방법
# print(s2) # ['010', '1234', '5678']
#
# # 8) replace()
# # 문자열의 일부 문자열을 다른 문자열로 바꾼 결과를 반환
# print()
# s = 'Life is too short'
# s2 = s.replace('short','long')
# print(s2) # Life is too long
#
# # 특정 문자열을 제거하기 위한 용도로 사용
# s = '010-1234-5678'
# s2 = s.replace('-','')
# print(s2) # 01012345678
#
# # 9) 불필요한 문자열 제거 메소드
# # 문자열 양끝에 있는 불필요한 문자열을 제거
# # strip() : 양쪽 끝에 있는 불필요한 문자열을 제거한 결과를 반환
# # lstrip() : 왼쪽 끝에 있는 불필요한 문자열을 제거한 결과를 반환
# # rstrip() : 오른쪽 끝에 있는 불필요한 문자열을 제거한 결과를 반환
#
# print()
# s = '     apple'
# print(len(s)) # 10
#
# s2 = s.lstrip()
# print(s2) # apple
# print(len(s2)) # 5
#
# # 주민등록번호에서 생년월일 6자리 추출하는 프로그램
# # 하이픈 위치가 올바르지 않다면 오류 메시지 출력 후 다시 입력 받도록 처리
# while True:
#     p = input('하이픈을 포함하여 전체 주민등록번호를 입력하세요 >>> ')
#     if p.find('-') != 6: # 문자열 내부에 포함된 특정 문자열을 찾고자 할 때 사용
#         print('하이픈의 위치가 잘못되었습니다.')
#         continue
#
#     birthday = p.split('-')
#     print(birthday)
#     print(f'생년월일은 {birthday[0]}입니다.')
#     print(f'생년월일은 {p[0:6]}입니다.') # 문자열 슬라이싱 사용
#     break


# 1. 우리나라의 전화번호는 '지역번호-국번-가입자 개별번호'형식으로 되어 있습니다.
# 어떤 형식의 전화번호를 입력하더라도 '국번'을 추출하여 출력하는 프로그램을 구현하세요.

number = input('전화번호를 입력하세요 >>> ')
hipenIndex = number.find('-')
hipenIndex2 = number.rfind('-')
print(number[hipenIndex+1:hipenIndex2])

# 1-1. find() 메서드와 슬라이싱 활용
phone = input('전화번호를 입력하세요 >>> ')
start = phone.find('-') + 1 # 첫번째 '-'이 나오는 인덱스의 다음 인덱스를 구함
end = phone.find('-',start) # 인덱스를 범위에 지정해 두번째 '-' 인덱스를 구함
code = phone[start:end] # 문자열 슬라이싱을 사용.
print(code)

# 1-2. split() 메소드 활용
phone = input('전화번호를 입력해주세요 >>> ')
code = phone.split('-')[1]
print(code)

#2. '숫자3자리-숫자2자리-숫자5자리' 형식(예: 123-45-67890)의 사업자등록번호를 입력받아서 형식이
# 맞는지 점검하는 프로그램을 구현하세요.
# 다음 지시사항을 모두 점검해야 합니다.

while True:
    saNumber = input('사업자등록번호를 입력하세요(예: 123-45-67890) >>> ')
    if len(saNumber) == 12:
        if saNumber.find('-') == 3 and saNumber.rfind('-') == 6:
            if saNumber.replace('-','').isdecimal() == True:
                print("올바른 형식입니다.")
                break
    else:
        print("올바른 형식이 아닙니다.")
        continue

no = input('사업자등록번호를 입력하세요(예: 123-45-67890) >>> ')
# case 1
if len(no) != 12: # 전체 글자 수 (12) 확인
    print('올바른 형식이 아닙니다.')
elif no.find('-') != 3: # 첫번째 '-' 위치 확인
    print('올바른 형식이 아닙니다.')
elif no.find('-', 4) != 6: #2번째 '-' 위치 확인
    print('올바른 형식이 아닙니다.')
elif not no.replace('-', '').isdecimal(): # '-'을 제외한 문자가 숫자인지 확인
    print('올바른 형식이 아닙니다.')
else:
    print('올바른 형식입니다.')

# case 2
conditon1 = (no.find('-') == 3) # 첫번째 '-' 위치 확인
conditon2 = (no.find('-', 4) == 6) # 두번째 '-' 위치 확인
conditon3 = (len(no) == 12) # 전체 글자 수 (12) 확인
conditon4 = (no.replace('-', '').isdecimal()) # '-'를 제외한 문자가 숫자인지 확인
if conditon1 and conditon2 and conditon3 and conditon4:
    print('올바른 형식입니다.')
else:
    print("올바른 형식이 아닙니다.")







