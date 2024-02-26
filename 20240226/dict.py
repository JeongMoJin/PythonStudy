d = {'a' : 'apple', 'b':'banana'} # {key : vlaue, key:value}
print(d)
print(type(d)) # <calss 'dict'>
print(d['a'])  # apple / 인덱스 대신 key를 사용하면 value가 반환
print(d['b']) # banana

# 키값의 자료형이 문자열(str) 이라면 dict() 함수를 이용해서 생성 가능
d = dict(a = 'apple', b='banana')
print(d) # {'d' : 'apple', 'b' : 'banana')

# 딕셔너리 요소의 추가와 삭제
# 새로운 키와 값을 조합해서 작성
print()
dic = {'apple' : '사과'}
dic['watermelon'] = '멜론'
print(dic) # {'apple' : '사과', 'watermelon' : '멜론'}

# 존재하는 키값을 이용해서 정의하면, value 수정으로 인식
dic['watermelon'] = '수박'
print(dic) # {'apple' : '사과', 'watermelon' : '수박'}

# setdefault() 메소드를 이용한 추가
me = {'name' : 'james'}
me.setdefault('age', 20)
print(me) # {'name':'james', 'age' :20}
me.setdefault('age',30) # 동일한 키가 있는 경우에 무시
print(me) # {'name' : 'james', 'age' : 20}

# update() 메소드의 경우 존재한느 키값이면 수정
me.update(age = 25)
print(me)

# update() 메소드의 경우 존재하지 않는 키값이면 추가
me.update(address='seoul')
print(me)

# pop() 메소드에 키값을 전달하면 해당 키값의 데이터가 삭제
me.pop('address')
print(me) # {'name' : 'james', 'age' : 25}

# get() 메서드가 전달한 key에 해당하는 value를 반환
print(me.get('name')) # james

# mutable 과 immutable
# mutable : 생성된 후에도 변경이 가능한 자료형 : list, set, dict
# immutable : 생성된 후에는 변경이 불가능한 자료형 : int, float, str, tuple

# mutable
# 할당받는 메모리에 저장된 값을 다른 값으로 바꿀 수 있음
# id() : 객체의 고유값 변환. 메모리 주소를 구별하기 위한 용도로 사용
me = [1,2,3]
print(id(me)) # 객체 고유값
me.append(4)
print(id(me)) # 객체 고유값 / 할당된 메모리 주소는 변경이 되지 않음

# immutable
# 한 번 생성하면 최초로 저장된 값을 다른 값으로 바꿀 수 없음
obj = 10
print(id(obj)) # 객체 고유값
obj = obj + 1
print(obj) # 11
print(id(obj)) # 객체 고유값 / 할당된 메모리 주소가 변경이 됨
# 메모리에 저장된 데이터를 수정하는 것이 아니라, 새로 할당을 받아서 데이터를 저장











