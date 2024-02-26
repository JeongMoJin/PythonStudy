# % 연산자
# 형식문자를 포함한 문자열에 % 연산자를 사용해 형식 문자에 전달될 값을 작성

name = 'jeongmo'
print('내 이름은 %s입니다.' %name) # 내 이름은 jeongmo입니다. / %s : string
print('내 이름은 ', name, '입니다.', sep='')
print('내 이름은 ' + name + '입니다.')

height = 120.5
print('내 키는 %fcm입니다.' % height) # 내 키는 120.50000cm 입니다. / %f : float

weight = 23.55
print('내 몸무게는 %.1fkg입니다.' % weight) # 내 몸무게는 23.6kg 입니다.

year, month, day = 2014, 8, 25
print('내 생일은 %d년 %d월 %d일입니다.' %(year, month, day))
# 내 생일은 2014년 8월 25일입니다. / %d : decimal(십진법)