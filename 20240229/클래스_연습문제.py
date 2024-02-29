# 1. 다음 지시사항을 읽고 책 제목과 저자 정보를 저장할 수 있는 Book 클래스를 생성하세요.

# 지시사항
# 1. 책 제목과 책 저자 정보를 출력하는 print_info() 메서드를 구현하세요.
# 2. 다음과 같은 방법으로 book1과 book2 인스턴스를 생성하세요.
#
# # book1, book2 인스턴스의 생성
# book1 = Book()
# book2 = Book()
#
# # book1, book2 제목과 저자 정보 저장
# book1.set_info('파이썬', '민경태')
# book2.set_info('어린왕자', '생텍쥐페리')
#
# 실행 예)
# 책 제목: 파이썬
# 책 저자: 민경태
# 책 제목: 어린왕자
# 책 저자: 생텍쥐페리

# class Book:
#     def set_info(self, name, author):
#         self.name = name
#         self. author = author
#
#     def print_info(self):
#         print(f'책 제목: {self.name}')
#         print(f'책 저자: {self.author}')
#
# book1 = Book()
# book2 = Book()
#
# book1.set_info('파이썬', '민경태')
# book2.set_info('어린왕자', '생텍쥐페리')
#
# book1.print_info()
# book2.print_info()


# 2
# class Watch:
#
#     def watch(self,hour, minute, second):
#         hour.self = hour
#         minute.self = minute
#         second.self = second
#
#
#     def add_second(self, second):
#         self.second = self.second + second
#         if self.second > 59:
#             self.second -= 60
#             self.minute = self.minute + 1
#
#
#     def add_minute(self, minute):
#         self.minute = self.minute + minute
#         if self.minute > 59:
#             self.minute -= 60
#             self.hour = self.hour + 1
#
#
#     def add_hour(self, hour):
#         self.hour = self.hour + hour
#         if self.hour > 23:
#             self.hour -= 60
#
#     def print_time(self):
#         print(f'계산된 시간은 {self.hour}시 {self.minute}분 {self.second}초입니다')
#
# watch1 = Watch()
#
# time = input('시간을 입력하세요 >>> ')
# time = time.split(':')
# watch1.watch(int(time[0]), int(time[1]), int(time[2]))
# hour = int(input('계산할 시간를 입력하세요 >>> '))
# minute = int(input('계산할 분를 입력하세요 >>> '))
# second = int(input('계산할 초를 입력하세요 >>> '))
#
# watch1.add_second()
# watch1.add_minute()
# watch1.add_hour()
# watch1.print_time()

class Watch:
    def set_time(self) -> None:
        time : str = input("시간을 입력하세요 >>> ")
        self.hour : int = int(time[0:2])
        self.minute : int = int(time[3:5])
        self.second : int = int(time[6:8])

    def add_hour(self) -> None:
        hour: str = input('계산할 시간을 입력하세요 >>> ')
        self.hour += int(hour)

    def add_minute(self) -> None:
        minute = input('계산할 분을 입력하세요 >>> ')
        self.hour += int(minute) // 60
        self.minute += int(minute) % 60

    def add_second(self) -> None:
        second = input('계산할 초를 입력하세요 >>> ')
        self.hour += int(second) // 3600
        self.minute += int(second) % 3600 // 60
        self.second += int(second) & 60

    def print_time(self) -> None:
        print(f'계산된 시간은 {self.hour}시, {self.minute}분, {self.second}초입니다.')


# 3
class Song:
    def set_song(self, title, category):
        self.title = title
        self.category = category

    def print_song(self):
        print(f'노래제목: {self.title}({self.category})')

class Singer:
    def set_singer(self, name):
        self.name = name

    def hit_song(self, song):
        self.song = song

    def print_singer(self) -> None:
        print(f'가수이름 : {self.name}')
        self.song.print_song()