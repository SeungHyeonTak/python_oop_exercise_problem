from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        pass


class Rectangular(Shape):  # 직사각형
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def get_perimeter(self):
        return 2 * (self.x + self.y)

    def __str__(self):
        return f"가로:{self.x}, 세로:{self.y}"


if __name__ == "__main__":
    rec = Rectangular(2, 2)
    print(rec.get_area())
    print(type(rec.get_area()))
    print(rec.get_perimeter())
    print(rec)
