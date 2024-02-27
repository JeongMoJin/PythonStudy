# # for 문
# # 값의 범위나 횟수가 정해져 있을 때 사용하면 편리한 반복문
# # 1) 특정 횟수 반복
# # 2) 데이터 순회
#
# # 기본 구조
# # for 변수 in 반복가능객체 :
# #   반복실행문
#
# for n in [2, 4, 6]:
#     print(n)
#
# # 반복가능객체
# # 1. 시퀀스 sequence 자료형 : 순서를 가지고 있는 자료형
# #    문자열, 리스트, 튜플, range
# # 2. 비시퀀스 non-sequence 자료형 : 순서를 가지고 있지 않은 자료형
# #    세트, 딕셔너리
#
# # 1. 문자열
# # for 문자 in 문자열:
# #     반복실행문
#
# for ch in "Hello": # 문자열 내부의 문자를 하나씩 꺼내서 사용할 수 있음
#     print(ch)
#
# # 2. 리스트
# # for 요소 in [리스트]:
# #     반복실행문
#
# for item in ['가위', '바위', '보']:
#     print(item)
#
# # 인덱스 번호 사용  enumerate() 사용.
# li = ['가위', '바위', '보']
# for i, v in enumerate(li): # i:index, v:요소의 값 value
#     print(f'{i} {v}')
#
# # 리스트 내포
# # 리스트 생성할 때 for문을 유용하게 사용할 수 있음
# # 기본 형식
# # 리스트 = [표현식 for 변수 in 반복가능객체]
# li = [n * 2 for n in [1,2,3]]
# print(li) # [2, 4, 6]
#
# # 조건에 맞는 데이터만 추출 가능
# # 리스트 = [표현식 for 변수 in 반복가능객체 if 조건식]
# li = [n * 2 for n in [1,2,3,4,5]]
# print(li) # [2,4,6,8,10]
#
# li = [n * 2 for n in [1,2,3,4,5] if n % 2 == 1]
# print(li)
#
# li2 = [1,2,3,4,5]
# for n in li2:
#     if (n % 2 == 1):
#         li2.append(n * 2)
# print(li2)
#
# # 3. 튜플
# # 기본 형식
# # for 요소 in (튜플):
# #   반복실행문
#
# four_seasons = ('Spring', 'Summer', 'Autumn', 'Winter')
# for season in four_seasons:
#     print(season)
#
# # 4. range() 함수
# # '정수 범위'를 만들어 낼 때 유용한 함수. 일정 횟수 반복시에 많이 사용
# # 기본 구조
# # range(초깃값, 종료값, 증감값)
#
# # 특징
# # 1. 초깃값부터 종료값 전까지 숫자(n)들의 컬렉션을 만듬 (초기값 <= n < 종료값)
# # 2. 초깃값을 생략하면 0부터 시작
# # 3. 종료값은 생략할 수 없음
# # 4. 증감값을 생략하면 1씩 증가
#
# # 예
# # range(5) : 0, 1, 2, 3, 4
# # range(1, 11) : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# # range(1, 10, 2) : 1, 3, 5, 7, 9
#
# print()
# print(list(range(1, 6))) # [1, 2, 3, 4, 5]
# print(tuple(range(1, 6))) # (1, 2, 3, 4, 5)
#
# print()
# for n in [1,2,3,4,5,6,7,8,9,10]:
#     print(n)
#
# # 아래와 같이 변경 가능
# for n in range(1,11):
#     print(n)
#
# # range() 함수를 이용해 생성한 값을 사용하지 않는 경우
# for n in range(10): # 10번 반복
#     print("Hello")
#
# # 문자열로 비밀번호를 입력 받아 숫자와 문자가 모두 포함이 되었는지 확인
#
# pwd = input("비밀번호를 입력하세요 >>> ")
#
# ch_conut = 0
# num_count = 0
#
# for ch in pwd:
#     if ch.isalpha(): # ch가 문자인 경우 True 반환
#         ch_conut += 1
#     elif ch.isnumeric(): # ch가 숫자인 경우 True 반환
#         num_count += 1
#
# if ch_conut > 0 and num_count > 0:
#     print("가능한 비밀번호입니다.")
# else:
#     print("불가능한 비밀번호입니다.")
#
# # 출력하고자 하는 구구단을 입력받아 구구단을 출력
# # dan = int(input('출력할 구구단을 입력하세요 >>> '))
# # for n in range(1, dan):
# #     print()
#
# dan = 2
# while dan < 10:
#     print(f"{dan}단")
#     for n in range(1,10):
#         print(f"{dan} * {n} = {dan*n}")
#     print("========================")
#     dan += 1

# # 1. 1부터 5사이에 존재하는 모든 정수를 역순으로 출력하는 프로그램을 구현하세요.
# for n in range(5, 0, -1):
#     print(n)
#
# # 2. 사용자로부터 임의의 양의 정수를 하나 입력받은 뒤 1부터 입력받은 정수까지 모든 정수의 합계를 출력하는 프로그램을 구현하세요.
# num = int(input("임의의 양수를 입력하세요 >>> "))
# sum = 0
# for n in range(1, num+1):
#     sum += n
# print(f"1부터 {num}사이 모든 정수의 합계는 {sum}입니다.")
#
# # 3. 사용자로부터 임의의 양의 정수를 하나 입력 받은 뒤 그 숫자만큼 '과일 이름'을 입력받아 'basket' 리스트에
# # 저장하는 프로그램을 구현하세요.
# basket = []
# fruNum = int(input("임의의 양수를 입력하세요 >>> "))
# for n in range(1, fruNum+1):
#     fru = input(f"{n}번째 과일을 입력하세요 >>> ")
#     basket.append(fru)
# print(f'입력받은 과일들은 {basket}입니다.')
#

# 1. 세트 set
# 비시퀀스 자료형이기 때문에 저장된 요소들 사이에 순서가 없음

# 기본 형식
# for 요소 in {세트} :
#    반복실행문

for item in {'가위', '바위', '보'}: # 순서가 지켜지지 않음
    print(item)


# 2. 딕셔너리
# key와 value의 조합이라 다른 자료형과 다른 방식으로 사용됨
# 키만 출력
print()
person = {'name' : "에일리", 'age': 20}
for item in person:
    print(item) # name age

# value 출력
for key, value in person.items():
    print(f'{key} = {value}')

for key in person:
    print(person[key]) # 에일리 20

for key in person: # get() 메소드를 이용해서 해당 key에 value를 가져옴
    print(person.get(key))

# 영어 사전을 딕셔너리 자료형으로 구현하고
# 영어 사전에 등록된 모든 단어와 그 단어의 의미를 출력
eng_dict = {
    'sun' : '태양',
    'moon': '달',
    'star': '별',
    'space': '우주'
}
for word in eng_dict:
    print(f'{word}의 뜻: {eng_dict[word]}')
    print(f'{word}의 뜻: {eng_dict.get(word)}')





