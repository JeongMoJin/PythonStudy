# format() 메소드
# format() 메소드의 인수로 변수나 값을 표시하고, 해당 값이 표시될 위치를 중괄호({})로 표시하는 방식

zipcode = '06236'
print('우편번호 : {}'.format(zipcode)) # format() 메서드를 이용해 출력

zipcode_str = '우편번호 : {}'.format(zipcode)
print(zipcode_str)

address = '''서울특별시 강남구
테헤란로 146''' # multi line

print('주소 : {addr}'.format(addr=address)) # format() 메서드의 변수 이용
print('주소 : ' + address)