# 사용자 정의 함수
# 사용자가 직접 만든 함수
# 1) 어떤 입력을 받아 2) 특정 연산을 수행한 뒤 3) 결과를 반환하는 기능

# 함수 용어 정리
# 1. 함수 정의 : 사용자 함수를 새로 만드는 것을 의미
# 2. 인수 : 사용자 함수에 전달할 입력(input)을 의미. argument
# 3. 매개변수 : 인수를 받아서 저장하는 변수를 의미. parameter
# 4. 반환값 : 사용자 함수의 출력(output)을 의미. return
# 5. 함수 호출 : 만들어진 사용자 함수를 실제로 사용하는 것을 의미


# 함수 정의
# 함수를 만드는 것을 의미. def 키워드를 이용

# def 함수이름(매개변수) :
#   본문
#   return 반환값
# 함수이름을 개발자가 마음대로 결정
# 매개변수, 반환값을 필수 사항이 아님

# 함수 호출
# 변수 = 함수이름(인수)
# 함수의 호출 결과를 저장할 변수를 생략가능

# 4가지 함수 호출 형태
# 1) 인수 : X, 반환값 : X
# 함수이름()
# 2) 인수 : O, 반환값 : X
# 함수이름(인수)
# 3) 인수 : X, 반환값 : O
# 변수 = 함수이름()
# 4) 인수 : O, 반환값 : O
# 변수 = 함수이름(인수)

# welcome() 함수 정의
def welcome():
    print('Hello Python')
    print("Nice to meet you")


welcome()  # 함수를 정의한 후에 호출 해야 함


# 파이썬 함수의 단점 : 데이터 타입이 없어서 다른 작업자가 만든 함수를 사용할 때 주의할 점이 많음
def process(number):
    return number / 1


process("helloo")  # TypeError: unsupported operand type(s) for /: 'str' and 'int'


# 어노테이션 사용 가능. 타입 강제는 아님
def process(number: int) -> float:
    return number / 1


# 인수와 매개변수
# 함수로 전달되는 인수(argument)를 저장하는 변수를 매개변수(parameter)라고 함

# 1. 인수가 있는 함수
def introduce(name, age):
    print(f'내 이름은 {name}이고, 나이는 {age}살 입니다.')


introduce('james', 25)  # 내 이름은 james이고, 나이는 25살 입니다.
introduce(age=25, name='james')  # 내 이름은 james이고, 나이는 25살 입니다.


# 2. 가변 매개변수
# 함수로 전달해야 하는 인수의 개수가 정해지지 않아도 매개변수를 선언할 수 있음
# 가변 매개변수를 만드는 키워드는 애스터리스크(*)
# 매개변수 앞에 *를 붙이면 곧바로 가변 매개 변수가 되면서 전달되는 모든 인수를 하나의 튜플(tuple)로 만들어 줌

def show(*args):
    for item in args:
        print(item)


show('python')  # show 함수 호출. 인수가 1개
show('happy', 'birthday')  # show 함수 호출. 인수가 2개

# 3. 디폴트 매개변수
# 매개변수로 전달되는 인수가 없는 경우에 기본적으로 사용할 수 있도록
# 매개변수에 기본값을 설정할 수 있음

print()


def greet(message='안녕하세요'):
    print(message)


greet('반갑습니다.')  # 반갑습니다
greet()  # 안녕하세요


# 디폴트 매개변수와 일반 매개변수를 같이 사용하는 경우 디폴트 매개변수를 뒤(오른쪽)으로 배치
def greet(name, message="안녕하세요"):
    print(f'{name}님 {message}.')


greet('김철수')  # 김철수님 안녕하세요
greet('김철수', '반갑습니다.')  # 김철수님 반갑습니다.

greet()  # 이철수님 안녕하세요
greet('김철수')  # 김철수님 안녕하세요. 왼쪽 부터 적용.
greet('김철수', '반갑습니다')  # 김철수님 반갑습니다.


# 반환값
# 함수 호출 결과를 반환값(return value)
# 반환값이 있으면 함수 내부에서 return 문을 통해 값을 반환할 수 있고,
# 반환값이 없으면 함수 내부에 return문을 작성할 필요가 없음

def address():
    string = "우편번호 12345\n"
    string += '서울시 영등포구 여의도동'
    return string


print(address())  # None : 반환값이 없어서 출력이 안됨

# 2. 다중 반환
# 하나의 반환값도 처리할 수 있고 여러 개의 반환값도 처리할 수 있음

print()


def calculator(*args):
    return sum(args), sum(args) / len(args), max(args), min(args)


a, b, c, d = calculator(1, 2, 3, 4, 5)  # 4개의 반환값을 모두 저장하기 위해서 변수 4개 배치
print('합계', a)  # 합계 15
print('평균', b)  # 평균 3.0
print('최댓값', c)  # 최댓값 5
print('최솟값', d)  # 최솟값 1

print()  # result는 4개의 반환값을 저장하는 튜플
result = calculator(1, 2, 3, 4, 5)
print('합계', result[0])
print('평균', result[1])
print('최댓값', result[2])
print('최솟값', result[3])

# 다중 반환 일 때, 변수 갯수에 맞게 또는 한개로 지정해야 함

# 3. 함수의 종료를 위한 return
# 반환값이 있으면 return문을 사용해 반환하고, 반환값이 없으면 return문을 생략하면 됨
# 반환값이 없을 때도 return문을 작성하는 경우 -> 함수를 종료할 때
print()


def charge(energy):
    if energy < 0:
        print('0보다 작은 에너지는 충전할 수 없습니다.')
        return  # charge() 함수의 종료를 의미
    print('에너지가 충전되었습니다.')


charge(1)  # 에너지가 충전되었습니다.
charge(-1)  # 0보다 작은 에너지는 충전할 수 없습니다.

# 4. 파이썬의 함수는 객체이고 자료형이다.
print(charge)  # <function charge at 0x000001EA42448DC0>


def print_charge(fun):
    fun(0)  # 에너지가 충전되었습니다.


print_charge(charge)  # 함수를 함수 호출시 인수로 사용이 가능


# 5. 함수안에 함수 선언도 가능하다.
def print_greet(name):
    def get_greet():
        return '안녕하세요'

    print(name + "님" + get_greet())


print_greet('김철수')