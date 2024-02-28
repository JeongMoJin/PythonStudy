import time, random, math
from datetime import datetime

""" 
1. 자동으로 실행되는 로또 추첨 프로그램을 다음 지시사항에 따라 구현하세요.

지시사항
1. 1에서 45 사이의 모든 정수를 순서대로 pot 리스트에 저장합니다.
2. 다음 과정을 6번 반복합니다.
 * pot 리스트를 무작위로 섞어줍니다.
 * pot 리스트의 마지막 숫자를 하나만 빼서 jackpot 리스트에 저장합니다.
 * 2초 동안 잠시 멈춥니다.
3. jackpot 리스트의 모든 요소를 오름차순 정렬합니다.
4. jackpot 리스트의 모든 요소를 출력합니다. 
"""
jackpot = []
for i in range(6):
    pot = random.randint(1,45)
    time.sleep(0.5)
    print(f'{i+1}번째 당첨번호는 {pot}입니다.')
    jackpot.append(pot)
jackpot = sorted(jackpot)
print(jackpot)

"""
2. 다음 지시사항에 따라 UpDown게임을 구현하세요.

지시사항
1. 1에서 100 사이의 정수 중 하나를 임의로 생성하면
사용자는 그 숫자를 맞힐 때까지 값을 예상하여 입력합니다.
2. 사용자가 입력한 값이 정답보다 작으면 Up, 정답보다 크면 Down을 출력합니다.
3. 정답을 맞히면 몇 초 만에 정답을 맞혔는지 출력하세요.
이때 소수 아래 값은 내림 처리하여 정수로 출력하세요."""

number = random.randint(1,100)
time1 = datetime.now()
while True:
    print("UpDown게임을 시작합니다.")
    numberAns = int(input("어떤 값일까요? >>>"))
    if numberAns > number:
        print("Down")
        continue
    elif number > numberAns:
        print("UP")
        continue
    elif numberAns == number:
        print(f'{numberAns}! 정답입니다.')
        print(f'{math.floor((datetime.now() - time1).total_seconds())}초 만에 성공했습니다.')
        break