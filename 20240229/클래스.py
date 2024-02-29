# 3. 클래스 정의
# 클래스 정의 방법
# 1) class 키워드로 클래스를 정의
# 2) 클래스 이름은 Upper Camel Case 규칙을 따름
# 파이썬은 변수나 함수의 이름을 네이밍할 때 언더바 (_)를 이용해 단어를 연결하는 Snake Case 방식을 사용하지만
# 클래스는 Upper Camel Case 규칙을 따름
# print + member : printmember 1) print_member 2) printMember 3) PrintMember

# 클래스는 다음과 같은 형식으로 정의
# class 클래스 :
#     본문

# 4. 객체 생성
# 클래스가 정의되었다면 다음과 같은 형식으로 객체를 생성
# 객체 = 클래스()

# 2개의 객체를 만들고 싶으면
# 객체1 = 클래스()
# 객체2 = 클래스()

# 5. 클래스 정의와 객체 생성
class WaffleMachine: # WaffleMachine 이라는 클래스 정의
    pass

waffle1 = WaffleMachine() # WaffleMachine 이라는 클래스를 이용해 waffle이라는 객체 생성
waffle2 = WaffleMachine()

print(waffle1) # <__main__. .. ~ 주솟값>
# 메모리의 주소 번지에 저장된 WaffleMachine의 객체라는 의미
print(waffle2)

# 클래스의 구성
# 1. 클래스의 기본 구성
# 객체를 만들어내는 클래스는 객체가 가져야 할 '값과 기능'을 가지고 있어야 함
# 같은 변수, 기능은 함수
# 정리하면 클래스는 변수와 함수로 구성된다고 볼 수 있음

# 클래스를 구성하는 변수는 1) 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수인 '클래스 변수'와
# 2) 모든 인스턴스들이 개별적으로 가지는 변수인 '인스턴스 변수'로 분리됨

# 클래스를 구성하는 함수는 메소드 method라고 하고
# 1) 클래스 메소드 2) 정적 메소드 3) 인스턴스 메소드로 분리

# 2. 인스턴스 변수와 인스턴스 메소드
# 인스턴스 변수란 클래스를 기반으로 만들어지는 모든 인스턴스들이 각각 따로 저장하는 변수
# 모든 인스턴스 변수는 self 라는 키워드를 앞에 붙여줌
# 인스터스 메소드란 인스턴스 변수를 사용하는 메소드
# 인스턴스 메소드는 반드시 첫 번째 매개변수로 self를 추가해야 함

class Person: # Person 클래스를 정의

    # 첫 번째 매개변수가 self이므로 인스턴스 메소드
    # 모든 인스턴스는 who_am_i() 메소드를 호출할 수 있음
    # 매개변수 self에는 메서드를 호출하는 인스턴스가 전달
    # self를 제외한 나머지 매개변수의 실제로 사용될 데이터가 전달
    def who_am_i(self, name, age, tel, address):
        #인스턴스 변수 = 매개변수. 모든 인스턴스 변수는 최초에 값이 대입되는 시점에 알아서 생성
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

boy = Person() # 인스턴스 boy가 생성. 클래스의 생성자가 호출
# print(boy.name) # AttributeError: 'Person' object has no attribute 'name'
boy.who_am_i('john', 15,'123-1234', 'toronto') # 인스턴스 메서드 호출
print(boy.name) # john
print(boy.age) # 15
print(boy.tel) # 123-1234
print(boy.address) # toronto

# 클래스에 없는 속성도 추가가 가능함. 다른 언어의 객체와는 다른 방식
boy.email = 'test@test.com'
print(boy.email) # test@test.com

class Computer:
    def set_spec(self, CPU, RAM, VGA, SSD):
        self.CPU = CPU
        self.RAM = RAM
        self.VGA = VGA
        self.SSD = SSD

    def hardware_info(self):
        # print(self.CPU, self.RAM, self.VGA, self.SSD)>
        print(f'CPU = {self.CPU}')
        print(f'RAM = {self.RAM}')
        print(f'VGA = {self.VGA}')
        print(f'SSD = {self.SSD}')



computer1 = Computer()
computer1.set_spec('cpu', 32,16,512)
computer1.hardware_info()
print(computer1.CPU)
