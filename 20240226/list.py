print()
li = [10,20,30,40]
print(li[0:3])
print(li[:2])
print(li[::2])
print(li[-2::])

print()
scores = [50,40,30]
scores.append(100) # 마지막 요소에 100을 추가
print(scores) # [50,40,30,100]
print(scores[1]) # 40
scores.insert(0,90) # 인덱스 0에 90을 추가
print(scores) # [90,50,40,30,100]
print(scores[1]) # 50 \

# pop() : 인덱스를 전달하지 않으면 마지막 요소 삭제
# 인덱슬르 전달하면 전달된 인덱스의 요소를 삭제
scores.pop() # 마지막 요소를 제거
print(scores) # [90, 50, 40, 30]
scores.pop(0) # 0번 인덱스 요소를 제거
print(scores) # [50, 40, 30]