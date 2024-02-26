# print() 함수
# end : value 출력 후 출력할 문자
# end 속성을 사용하지 않고 print() 함수를 사용하면 출력 후 자동으로 줄 바꿈이 진행
# sep : 출력할 value의 구분자
# sep 속성을 사용하지 않고 print() 함수를 사용하면 출력 대상은 공백으로 구분
# file : 출력 방향 지정
# file 속성을 사용하지 않고 print() 함수를 사용하면 출력 대상은 모니터에 출력

print('재미있는', '파이썬') # sep 값을 지정하지 않으면 공백이 들어감
print('재미있는', '파이썬', sep=' ') # 재미있는 파이썬 / 콤마(,)로 구분된 출력대상은 공백으로 구분
print('Python', 'Java', 'C', sep = ':') # Python:Java:C / sep 속성으로 구분

print()
print('영화 타이타닉', end='\n') # 지정하지 않았을때 기본값은 \n
print('평점', end=':')
print('5점') # 평점 : 5점 / value 출력 후 end 속성 출력. 줄 바꿈이 되지 않음

fos = open('sample.py', mode='wt')
print('print("Hello World")', file = fos) # file 속성으로 대상 출력. 파일 출력
fos.close()