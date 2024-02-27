# # while 문
# # 특정 조건을 만족하는 동안 반복해서 수행해야 하는 코드를 작성할 때 사용
# # while 조건식 :
# #   반복실행문
#
# n = 1
# while n <= 10:
#     print(n)
#     n += 1 # n = n+1
# print(n)
#
# # 1부터 10사이의 모든 정수를 역순으로 출력
# n = 10
# while n >= 1:
#     print(n)
#     n -= 1
#
# # 100 부터 50사이의 짝수를 출력
# n = 100
# while n >= 50:
#     if n % 2 == 0:
#         print(n)
#     n -= 1
#
# n = 100
# while n >= 50:
#     print(n)
#     n -= 2
#
# # 사용자로 부터 임의의 정수를 입력받아 모두 리스트에 보관
# # 단 사용자가 0을 입력하면 프로그램을 종료. 이 때 입력받은 0은 리스트에 보관하지 않음
#
# my_list = [] # 빈 리스트 생성
# n = int(input("정수를 입력하세요 (종료 : 0) >>> ")) # 한 번만 실행
#
# while n != 0:
#     my_list.append(n)
#     n = int(input('정수를 입력하세요 (종료 : 0) >>> '))
#
# print(my_list)
#
# # 구구단 2단 부터 9단 까지 출력
# # 단 앞에 제목, 마지막에 구분선을 넣어볼 것
# # 8 * 9 = 72
# # =================
# # 9 단
# # 9 * 1 = 9
#
# dan = 2 # 구구단의 단을 의미
# while dan <= 9:
#     n = 1
#     print(f'{dan}단')
#     while n <= 9:
#         print(f'{dan} * {n} = {dan * n}')
#         n += 1
#     print("=============")
#     dan += 1


# 정수를 입력받아서 그 횟수만큼 'Hello'를 출력하는 프로그램 구현하세요
# 0이하의 값이 입력되면 '잘못된 입력입니다'를 출력

greetingNum = int(input("정수를 입력하세요 >>> "))
if greetingNum < 0:
    print("잘못된 입력입니다.")
elif (greetingNum >= 0):
    num = 1
    while (greetingNum >= num):
        print(f"{num}번째 Hello")
        num += 1

# 3. 커피 1잔을 300원에 판매하는 커피자판기가 있습니다.
# 이 커피자판기에 돈을 넣으면 자판기에서 뽑을 수 있는 커피가 몇 잔이며 잔돈은 얼마인지를 함께 출력하는 프로그램을 구현하세요.

money = int(input("자판기에 얼마를 넣을까요? >>>"))
while (money > 300):
    coffee = 1
    money -= 300
    print(f'커피 {coffee}잔, 잔돈 {money}원')

# 4. 사용자에게 0부터 9사이의 정수를 입력받습니다.
# 이 때 입력된 정수가 5개가 될 때까지 입력받는 프로그램을 구현하세요.
# 이 때 중복된 값이 입력되면 해당 입력은 무시하세요.

number = set()
while len(number) < 5: # numbers에 저장된 요소의 개수
    n = int(input("0 ~ 9 사이 정수를 입력하세요 >>> "))
    number.add(n)
print('모두 입력되었습니다.')
print(f'입력된 값은 {number}입니다.')











