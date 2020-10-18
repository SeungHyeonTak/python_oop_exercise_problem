# 연습문제 6
# Shape를 부모 클래스로 Square자식 클래스를 정의하는 코드를 작성하시오.
# Square 클래스는 length필드를 가지며, 0을 반환하는 Shape 클래스의 area 메서드를
# length*length값을 반환하는 메서드로 오버라이딩 한다.

class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.__length = length

    def area(self):
        return self.__length ** 2


if __name__ == "__main__":
    sq = Square(3)
    print(f"정사각형의 면적 : {sq.area()}")
