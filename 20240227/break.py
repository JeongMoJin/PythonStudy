# # break문
# # while문이나 for문과 같은 반복문을 강제로 종료하고자 할 때 사용하는 제어문
# # 반복문 내에 break문이 나타나면 곧바로 break문이 포함된 반복문은 종료
#
# n = 1
# while True:
#     print(n)
#     if n == 10:
#         break # if문에서 break문을 작성했지만 실제로 종료되는 것은 while문
#     n += 1
# print(n) # 10
#
# while True: # 무한 루프
#     city = input('대한민국의 수도는 어디인가요? >>>')
#     city = city.strip() # 문자열의 양쪽끝에서 공백을 없앰
#     if city == '서울' or city == 'seoul' or city == 'SEOUL': # 대소문자 모두 정답처리
#         print('정답입니다.')
#         break # 정답을 맞춰야 종료
#     else:
#         print("오답입니다. 다시 시도하세요.")
#
# # 종료 조건이 2가지인 경우 : 5개까지 입력이 가능 혹은 그전에 그만두려면 q 입력
#
# hobbies = [] # 빈 리스트 생성
# while True: # 무한루프
#     hobby = input('취미를 입력하세요(종료는 그냥 q) >>> ')
#     if hobby == 'q':
#         print('입력된 취미가 모두 저장되었습니다.')
#         break
#     else:
#         hobbies.append(hobby)
#
#     if len(hobbies) >= 5:
#         print('5개 입력!')
#         break
# print(hobbies)
#
# # continue 문
# # 반복문의 시작 지점으로 제어의 흐름을 옮기는 역할
# # 반복에서 제외하거나 생략하고 싶은 코드가 존재할 때 사용
#
# # 1에서 100사이의 모든 정수를 합하는데 3의 배수는 제외
# total = 0
# for a in range(1, 101):
#     if a % 3 == 0: # 3의 배수인지 검사
#         continue
#     total == 0
# print(total)
#
# fruites = ['사과', '감귤']
# count = 3 # 입력 가능한 횟수
#
# while count > 0:
#     fruit = input('어떤 과일을 저장할까요? >>> ')
#
#     if fruit in fruites: # fruites 리스트에 fruit 변수에 있는 값이 있다면
#         print("동일한 과일이 있습니다.")
#         continue # while문의 시작 지점으로 돌아가서 다시 과일 이름을 입력
#
#     fruites.append(fruit) # 입력된 과일 이름을 리스트에 저장
#     count -= 1 # 입력 가능 횟수가 줄어듬
#     print(f'입력이 {count}번 남았습니다.')
#
# print(f'5개 과일은 {fruites}입니다.')

# 1. 현재 10000원을 가지고 있습니다.
# 얼마 사용할 지 반복해서 모두 사용하세요
# 0 이하의 공백은 사용할 수 없으며, 현재 가지고 있는 돈보다 더 큰 금액도 사용할 수 없습니다.

money = 10000
while (money != 0):
    print(f'현재 {money}원이 있습니다.')
    use = int(input("사용할 금액 입력 >>> "))
    if (use < 0 or use > money):
        print('잘못된 금액을 입력했습니다.')
        continue
    else:
        money -= use
        continue
print(f'현재 {money}원이 있습니다.')

# 2. 영화 평점

while True:
    point = int(input("이번 영화의 평점을 입력하세요 >>> "))
    if (point < 0 or point > 5):
        print('평점은 1~5 사이만 입력할 수 있습니다.')
        continue
    else:
        star = point * "*"
        print(f'평점 : {point * "*"}')
        break

# 3. 비밀번호를 맞히는 프로그램
# 저장된 비밀번호 = "qwerty"

password = "qwerty"
count = 5
while (count != 0):
    password1 = input('비밀번호를 입력하세요 >>> ')
    if password == password1:
        print("비밀번호가 맞습니다.")
        break
    else:
        print("비밀번호를 다시 입력해주세요")
        count -= 1
        continue

while True:
    password1 = input('비밀번호를 입력하세요 >>> ')
    count -= 1
    # 종료 조건이 2개인 경우에는 같이 적어주는 것이 가독성이 좋음
    if password1 == password1:
        print('비밀번호를 맞혔습니다.')
        break
    elif count == 0:
        print('비밀번호 입력 횟수를 초과했습니다.')
        break

