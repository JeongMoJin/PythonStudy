# 지역변수와 전역변수
# 1. 지역변수 local variable
# 함수 내부에서 선언한 변수는 함수 내부에서만 사용. 함수 외부에서는 지역변수에 접근할 수 없음
from typing import Any


def f():
    a = 10
    print(f'f() 내부 : {a}')

f() # f() 내부 : 10
# print(f'f() 외부: {a}') # 함수 외부에서는 a 변수를 사용할 수 없음

# 2. 전역변수 global vairable
# 함수 외부에서 선언한 변수는 함수 내부나 함수 외부에서 모두 사용할 수 없음
print()

def f():
    print(f'f() 내부 : {b}')

b = 10 # 전역변수
f() # f() 내부 10
print(f'f() 외부 : {b}') # f() 내부 10

# 1) 전역변수를 단순히 참조만 하는 경우 -> 읽기만 하는 경우
print()
a = 0
def f():
    print(a) # 함수 f() 내부에서 전역변수 a를 참조

f() # 0
print(a) # 0 / 함수 f() 외부에서 전역변수 a를 참조

# 2) 전역변수의 값을 변경하는 경우 : 파이썬의 경우 변수 초기화와 변수 값 수정이 문법적으로 똑같음
print()
a = 0

def f():
    global a # 전역변수 a를 사용할 때, global을 붙혀 준다
    a = 10 # 전역변수 a의 값을 변경

f() # 함수 f() 실행
print(a) # 10 / 전역변수의 변경된 값을 확인

# 커피 자판기 프로그램
def coffee_machine(money: int, pick: str):
    print(f'{money}원에 {pick}를 선택하셨습니다.')
    # 커피와 가격을 하나의 데이터로 처리하기 위해 딕셔너리 dict를 사용
    menu = {
        '아메리카노' : 1000,
        '카페라떼' : 1500,
        '카푸치노' : 2000
    }

    if pick not in menu: # 없는 커피를 주문하는 경우
        print(f'{pick}는 판매하지 않습니다.')
        return money, '없는 메뉴'
    elif menu[pick] > money: # 구매할 금액이 부족한 경우
        print(f'{pick}는 {menu[pick]}원 입니다.')
        return money, '금액 부족'
    else: # 정상 주문이면 잔돈과 선택한 커피를 반환
        return money - menu[pick], pick


order = input('커피를 선택하세요. (아메리카노, 카페라떼, 카푸치노) >>> ')
pay = int(input('얼마를 내시나요? >>> '))
coffee_machine(pay, order)


# 1. 700원짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하세요.
# 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지 그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 구현하세요.

def vending_machine(money):
    for idx in range(0, (money//700)+1):
        print(f'음료수 = {idx}개, 잔돈 = {money - 700*idx}원')
vending_machine(3000)

def get_average(marks: dict[Any, int]) -> float:
    return sum(marks.values()) / len(marks)

marks = {'국어':90, '영어':80, '수학':85}
average = get_average(marks)
print(f'평균은 {average}입니다.')









