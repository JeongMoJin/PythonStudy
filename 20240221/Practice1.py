# 전체 차량번호에서 뒤에 숫자 4자리만 출력하는 프로그램을 구현하세요.
# 전체 차량번호는 '서울2가 1234', '10가 1234', '288가 1234'와 같이 다르지만, 모두 차량번호 4자리는 '1234'입니다.
# 실행 예)
# 서울2가 1234의 차량번호 4자리는 1234입니다.

car1 = '서울2가1234'
car2 = '10가1234'
car3 = '288가1234'
car_no1 = car1[-4:]
car_no2 = car2[-4:]
car_no3 = car3[-4:]
print(car1, '의 차량번호 4자리는', car_no1, '입니다.')
print(car2, '의 차량번호 4자리는', car_no2, '입니다.')
print(car3, '의 차량번호 4자리는', car_no3, '입니다.')