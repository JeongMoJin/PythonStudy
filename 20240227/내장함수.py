# # eval() : 실행하고자 하는 표현식을 문자열로 전달하면 표현식의 결과값 반환
# print(eval('100 + 200')) # 300
#
#
# # format() : 전달받은 인수와 포맷 코드에 따라 형식을 갖춘 문자열을 반환
#
# print()
# print(format(10000)) # 10000 / str(10000)과 같음
# print(format(10000, ',')) # 10,000 / 천단위 구분 기호로 쉼표(,)를 사용
#
# # str() : 전달받은 인수를 문자열로 변환하여 반환
#
#
# # 2. 숫자 내장함수
#
# # abs() : 전달된 인수 (정수 혹은 실수)의 절대값을 반환
# print(abs(10)) # 10
# print(abs(-10)) # 10
#
# # divmod() : 전달된 두 인수를 나누어 몫과 나머지를 한 쌍의 결과로 반환. 몫과 나머지는 하나의 튜플로 반환
# print(divmod(10, 3)) # (3, 1)
# print(type(divmod(10, 3))) # <class 'tuple'>
#
# # float() : 전달된 인수(숫자 또는 문자열)를 실수로 만들어 반환. 전달된 인수가 없는 경우에는 0.0을 반환
#
# # max() : 전달된 인수 중 가장 큰 값을 반환
# print()
# print(max(1,10)) # 10
# li = [5, 4, 3, 2, 1]
# print(max(li)) # 5
#
# # min() : 전달된 인수 중 가장 작은 값을 반환
#
# # pow() : 전달된 두 인수의 거듭제곱을 반환. 연산자 중에서 거듭 제곱 연산자 ** 와 같음
# print()
# print(pow(10, 2)) # 100
# print(pow(10, 3)) # 1000
#
# # round() : 전달된 인수를 이용해 반올림한 값을 반환
# # 전달된 인수가 하나이면 정수로 반올림한 값을 반환하고, 전달된 인수가 2개이면 두 번째로 전달한 인수만큼 소수점을 남겨둠
# print()
# print(round(1.5)) # 2
# print(round(1.4)) # 1
# print(round(1.55, 1)) # 1.6
# print(round(2.675, 2)) # 2.67 > 부동 소수점 에러로 인해 2.67 반환. 더 정확하게는 다른 함수 사용
#
# # sum() : 전달된 리스트나 튜플과 같은 반복가능객체의 합계를 반환
# # 숫자가 아닌 값을 전달하면 에러가 발생
# print()
# list1 = [1,2,3,4,5]
# print(sum(list1)) # 15
#
# # list2 = ['h', 'e', 'l', 'l', 'o']
# # print(sum(list2) # 에러 발생
#
# exam = []
# print("점수를 입력하세요.")
# print("더 이상 입력할 점수가 없으면 음수를 아무거나 입력하세요.")
# while True:
#     score = int(input("점수입력 >>> "))
#     if (score < 0):
#         print(f'평균 = {sum(exam)/len(exam)}, 최대 = {max(exam)}, 최소 = {min(exam)}')
#         break
#     else:
#         exam.append(score)

# len() : 함수에 전달된 객체의 길이(항목 수)를 반환
print()
li = ['a', 'b', 'c', 'd']
print(len(li)) # 4

d = {'a' : 'apple', 'b' : 'banana'}
print(len(d)) # 2 / 딕셔너리는 '키:값'으로 구성된 한 쌍을 하나의 데이터로 봄

print(len(range(10))) # 10 / range() 함수로 생성되는 값은 0 ~ 9
print(len(range(1,10))) # 9 / range() 함수로 생성되는 값은 1 ~ 9

# range() 함수와 리스트의 길이를 구하는 len() 함수를 함께 사용하면 리스트의 인덱스를 생성가능
seasons = ['봄', '여름', '가을', '겨울']
seasons_eng = ['spring', 'summer', 'fall', 'winter']
for idx in range(len(seasons)):
    print(f'{seasons[idx]} / {seasons_eng[idx]}')

months_eng = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September','October', 'Novemer', 'December']
months = [31, 28, 31, 30, 31, 30, 31, 31, 30 ,31,30,31]

# 1. range 사용
for idx in range(len(months)):
    print(f'{months_eng[idx]} = {months[idx]}')

print()
# 2. enumerate() 사용
for i, v in enumerate(months):
    print(f'{v} = {months[i]}일')
print()

# sorted() : 전달된 반복가능객체의 오름차순 정렬 결과를 반환
# reverse=True 옵션을 추가할 경우 내림차순 정렬 결과를 반환
print()
my_list2 = ['b', 'c', 'a', 'd']
print(sorted(my_list2))  # ['a', 'b', 'c', 'd']
print(sorted(my_list2, reverse=True))  # ['d', 'c', 'b', 'a']

my_list = [6, 3, 1, 2, 5, 4]
print(sorted(my_list))  # [1, 2, 3, 4, 5, 6]
print(sorted(my_list, reverse=False))  # [1, 2, 3, 4, 5, 6]
print(sorted(my_list, reverse=True))  # [6, 5, 4, 3, 2, 1]

print()
print(sorted(my_list))  # [1, 2, 3, 4, 5, 6]
print(my_list)  # [6, 3, 1, 2, 5, 4] / 실제로 정렬이 된건 아님

print()
my_list = sorted(my_list)  # 오름차순 정렬 결과를 덮어쓰기
print(my_list)  # [1, 2, 3, 4, 5, 6]

# zip() : 전달된 여러 개의 반복가능객체의 각 요소를 튜플로 묶어서 반환
# 전달된 반복가능객체들의 길이가 서로 다르면 길이가 짧은 반복가능객체 기준으로 동작
print()
names = ['james', 'emily', 'amanda']
scores = [60, 70, 80]
for student in zip(names, scores):
    print(student)
# ('james', 60)
# ('emily', 70)
# ('amanda', 80)

# 튜플은 언패킹이 가능하므로 다음과 같은 모습으로 구성 가능
for name, score in zip(names, scores):
    print(f'{name}의 점수는 {score}입니다.')
# james의 점수는 60입니다.
# emily의 점수는 70입니다.
# amanda의 점수는 80입니다.

print()
for idx, name in enumerate(names):
    print(f'{name}의 점수는 {scores[idx]}입니다.')

print()
for idx in range(len(names)):
    print(f'{names[idx]}의 점수는 {scores[idx]}입니다.')
