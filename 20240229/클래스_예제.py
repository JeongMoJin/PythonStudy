# 가방을 만들 때 마다 현재 만들어진 가방이 몇 개 인지 계산할 수 있는 Bag 클래스

class Bag:
    count = 0 # 클래스 변수

    def __init__(self): # 생성자가 실행될 때 마다 증가
        Bag.count += 1
        # __class__.count += 1

    @classmethod
    def sell(cls): # 판매시 감소
        cls.count -= 1

    @classmethod
    def remain_bag(cls): # 남은 가방의 갯수 반환
        return cls.count

print('현재 가방: {}개'.format(Bag.remain_bag())) # 0
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print('현재 가방: {}개'.format(Bag.remain_bag())) # 3
bag1.sell()
bag2.sell()
print('현재 가방: {}개'.format(Bag.remain_bag())) # 1










