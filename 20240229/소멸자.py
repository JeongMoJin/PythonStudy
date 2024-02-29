# 소멸자
# 인스턴스가 생성될 때 자동으로 호출되는 생성자와 마찬가지로
# 인스턴스가 소멸될 때 자동으로 호출되는 메서드
# 소멸자는 __del__()

class Sample:
    def __del__(self):
        print('인스턴스가 소멸됩니다')

sample = Sample()
del sample # 인스턴스가 소멸됩니다

# 매직 메서드 샘플
class Sample:
    def __int__(self):
        pass

    def __len__(self):
        return 6

    def __str__(self):
        return 'what?'

li = [1,2,3]
print(len(li)) # 3

sample = Sample()
print(len(sample)) # 6
print(sample) # what?