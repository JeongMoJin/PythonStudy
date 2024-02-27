# 1
score = int(input("점수를 입력하세요 >>>"))
if (score <= 100 and score >= 90):
    print(f"점수는 {score}점이고, 학점은 A 학점입니다.")
elif (score >= 80 and score <90):
    print(f"점수는 {score}점이고, 학점은 B 학점입니다.")
elif (score >= 70 and score < 80):
    print(f"점수는 {score}점이고, 학점은 C 학점입니다.")
elif (score >= 60 and score < 70):
    print(f"점수는 {score}점이고, 학점은 D 학점입니다.")
else:
    print(f"점수는 {score}점이고, 학점은 F 학점입니다.")

# 2
number = int(input("정수를 입력하세요 >>> "))
if (number % 3 == 0):
    print(f'{number}는 3의 배수입니다.')
else:
    print(f'{number}는 3의 배수가 아닙니다.')

# 3
num1 = int(input('정수를 입력하세요 >>> '))
num2 = int(input('정수를 입력하세요 >>> '))
num3 = int(input('정수를 입력하세요 >>> '))
if (num1 > num2 and num1 > num3):
    print(f'가장 큰 수는 {num1}입니다.')
elif (num2 > num1 and num2 ):
    print(f'가장 큰 수는 {num2}입니다.')
elif (num3 > num1 and num3 > num2):
    print(f'가장 큰 수는 {num3}입니다.')

# max_num = num1
# if num2 > max_num:
#     max_num = num2
# if num3 > max_num:
#     max_num = num3
# print(f'가장 큰 수는 {max_num}입니다.')
#
# print(f'가장 큰 수는 {max([num1, num2, num3])}입니다.')
