# 2. 리스트 메소드
# 1) append()
# 리스트의 끝에 인수로 전달된 데이터를 추가

my_list = ['apple', 'banana']
my_list.append('cherry')
print(my_list) # ['apple', 'banana', 'cherry']

# 2) extend()
# 리스트에 다른 리스트나 튜플과 같은 반복가능객체를 추가하여 기존 리스트를 확장
print()
my_list = ['apple', 'banana']
my_list.extend(['cherry', 'mango'])
print(my_list) # ['apple', 'banana', 'cherry', 'mango']

my_list = ['apple', 'banana']
my_list += ['cherry', 'mango']
print(my_list) # ['apple', 'banana', 'cherry', 'mango']

# 3) insert()
# 리스트의 특정 인덱스에 데이터를 추가
print()
my_list = ['apple', 'banana']
my_list.insert(0, 'cherry')
print(my_list)

# 4) clear()
# 리스트에 저장된 모든 요소를 삭제
print()
my_list = ['apple', 'banana']
my_list.clear()
print(my_list) # []

my_list = ['apple', 'banana']
my_list = []
print(my_list) # []

# 5) pop()
# 리스트이 마지막 요소가 반환되면서 삭제
print()
my_list = ['apple', 'banana']
item = my_list.pop()
print(item) # banana
print(my_list) # ['apple']

# 인덱스 값을 인수로 전달하면 해당 인덱스 값이 삭제
my_list = ['apple', 'banana']
item = my_list.pop()
print(item) # apple
print(my_list) # ['banana']

# 6) remove()
# 인수로 전달된 값과 동일한 요소를 찾아서 제거. 동일한 요소가 여러 개인 경우에는 첫 번째 요소가 제거
print()
my_list = ['apple', 'banana']
my_list.remove('cherry')
print(my_list) # ['apple', 'banana', 'mango']

# 중복된 값이 있는 경우 제일 앞에 있는 것만 삭제
my_list = ['apple', 'banana', 'cherry', 'mango', 'cherry']
my_list.remove('cherry')
print(my_list) # ['apple', 'banana', 'mango', 'cherry']

# 특정 값을 전부 삭제를 원할 경우 반복문 사용
my_list = ['apple', 'banana', 'cherry', 'mango', 'cherry']
for idx in range(my_list.count('cherry')):
    my_list.remove('cherry')
print(my_list)