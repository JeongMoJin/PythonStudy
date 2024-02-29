# 1. 다음 지시사항을 읽고 이름과 전체 인구수를 저장할 수 있는 Person 클래스를 생성하세요.
#
# 지시사항
# 1) 다음과 같은 방법으로 man과 woman 인스턴스를 생성하세요.
# man = Person('james')
# woman = Person('emily')
#
# 2) man과 woman 인스턴스가 생성되면 다음과 같은 메세지를 출력할 수 있도록 처리하세요.
# james is born.
# emily is born.
#
# 3) 다음 코드를 통해서 전체 인구수를 조회할 수 있도록 처리하세요.
# print('전체 인구수: {}명'.format(Person.get_population())) # 전체 인구수: 2명
#
# 4) 다음과 같은 방법으로 man 인스턴스를 삭제하세요.
# del man
#
# 5) man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 처리하세요.
# james is dead.


class Person:
    human = 0
    def __init__(self, name):
        self.name = name
        print(f'{name} is born')
        Person.human += 1

    def __del__(self):
        print(f'{self.name} is dead.')
        Person.human -= 1

    @staticmethod
    def get_population():
        print(f'전체 인구수: {Person.human}명')

    @classmethod
    def get_population(cls) -> int:
        return cls.human

man = Person('james')
woman = Person('emily')
Person.get_population()
del man
Person.get_population()
del woman

# 2. 다음 지시사항을 읽고 가게의 매출을 구할 수 있는 Shop 클래스를 구현하세요.
#
# 지시사항
# 1) Shop 클래스는 다음과 같은 클래스 변수를 가지고 있습니다.
# total은 전체 매출액을 의미하고 menu_list의 각 요소는 {메뉴명: 가격}으로 구성된 딕셔너리입니다.
#
# total = 0
# menu_list = [{'떡볶이': 3000}, {'순대': 3000}, {'튀김': 500}, {'김밥': 2000}]
#
# 2) 매출이 생기면 다음과 같은 방식으로 메뉴와 판매량을 작성합니다.
# Shop.sales('떡볶이', 1)  # 떡볶이를 1개 판매
# Shop.sales('김밥', 2)  # 김밥을 2개 판매
# Shop.sales('튀김', 5)  # 튀김을 5개 판매
#
# 3) 모든 매출을 작성한 뒤 다음과 같은 방식으로 전체 매출액을 확인합니다.
# 매출: 9500원

class Shop:
    total = 0
    menu_list = [{'떡볶이': 3000}, {'순대':3000}, {'튀김':500}, {'김밥': 2000}]

    @staticmethod
    def sales(name:str, count: int):
        for menu in Shop.menu_list:
            if menu.keys() == name:
                Shop.total += count * menu.values()

    @staticmethod
    def totalMoney():
        print(f'매출: {Shop.total}원')

Shop.sales('떡볶이',1)
Shop.totalMoney()

# 3. 다음 지시사항을 읽고 Hybrid 클래스를 구현하세요.
#
# 지시사항
# 1) 다음과 같은 슈퍼 클래스 Car를 가지고 있는 서브 클래스 Hybrid를 구현하세요.
# class Car:
#
#   max_oil = 50 # 최대 주유량
#
#   def __init__(self, oil):
#     self.oil = oil
#
#   def add_oil(self, oil):
#     if oil <= 0: # 0 이하의 주유는 진행하지 않음
#        return
#     self.oil += oil
#     if self.oil > Car.max_oil: # 주유 후 최대 주유량 초과 상태이면
#       self.oil = Car.max_oil # 현재 주유량을 최대 주유량으로 설정
#
#   def car_info(self):
#     print('현재 주유상태: {}'.format(self.oil))
#
# 2) 서브 클래스 Hybrid는 다음과 같은 특징을 가지고 있습니다.
# 최대 배터리 충전량은 30입니다.
# 배터리를 충전하는 charge() 메서드가 있습니다.
# 최대 충전량을 초과하도록 충전할 수 없고, 0보다 작은 값으로 충전할 수 없습니다.
# 현재 주유량과 충전량을 모두 확인할 수 있는 hybrid_info() 메서드가 있습니다.
#
# 3) 다음과 같은 방식으로 전체 동작을 확인할 수 있습니다.
# car = Hybrid(0, 0)
# car.add_oil(100)
# car.charge(50)
# car.hybrid_info() # 현재 주유상태: 50 # 현재 충전상태: 30
# 3
class Car:

  max_oil = 50 # 최대 주유량

  def __init__(self, oil):
    self.oil = oil

  def add_oil(self, oil):
    if oil <= 0: # 0 이하의 주유는 진행하지 않음
       return
    self.oil += oil
    if self.oil > Car.max_oil: # 주유 후 최대 주유량 초과 상태이면
      self.oil = Car.max_oil # 현재 주유량을 최대 주유량으로 설정

  def car_info(self):
    print('현재 주유상태: {}'.format(self.oil))

class Hybrid(Car):
    max_battery = 30

    def __init__(self, oil, battery):
        super().__init__(oil)
        self.battery = battery

    def add_charge(self, battery):
        if battery <= 0: # 0 이하의 주유는 진행하지 않음
            return
        self.battery += battery
        if self.battery > Hybrid.max_battery: # 주유 후 최대 주유량 초과 상태이면
            self.battery = Hybrid.max_battery # 현재 주유량을 최대 주유량으로 설정


    def hybrid_info(self):
        print(f'현재 주유상태 : {self.oil}, 현재 충전상태 : {self.battery}')
