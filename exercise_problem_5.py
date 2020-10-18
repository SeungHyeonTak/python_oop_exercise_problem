# 연습문제 5
# 가로, 세로 정보를 갖고, 사각형의 면적을 계한하는 메서드를 갖는 Rectangle 클래스를 정의하고
# 생성한 객체의 사각형의 면적을 출력하는 프로그램을 작성하십시오.

class Rectangle:
    def __init__(self, row, col):
        self.__row = row
        self.__col = col

    @property
    def get_row(self):
        return self.__row

    @property
    def get_col(self):
        return self.__col

    def area(self):
        return self.get_row * self.get_col


if __name__ == "__main__":
    rec = Rectangle(4, 5)
    print(rec.area())
