# 연습문제 2
# 국적을 출력하는 printNationality 정적 메서드를 갖는 Korean 클래스를 정의하고 메서드를 호출하는 코드를 작성하자

class Korean:
    Nationality = "대한민국"

    def __init__(self):
        self.data = self.Nationality

    @classmethod
    def class_printNationality(cls):
        return cls()

    @staticmethod
    def static_printNationality():
        return Korean()


class Usa(Korean):
    Nationality = "미국"


if __name__ == "__main__":
    print(Usa.class_printNationality().data)
    print(Usa.static_printNationality().data)

# 정적 메소드
# 정적메소드라 함은 클래스에서 직접 접근할 수 있는 메소드이다.
# 파이썬에서는 staticmethod, classmethod가 있다.
# 파이썬에서는 정적 메소드임에도 불구하고 인스턴스에서도 접근이 가능하다.(이 차이에 유의 해야한다.)
# clasmethod는 첫번째 인자로 cls를 입력한다.
# staticmethod는 특별히 추가되는 인자가 없다.
# 둘의 차이는
# staticmethod에서는 부모클레스의 속성값을 가져오지만, classmethod에서는 cls인자를 활용하여 cls의 클래스 속성을 가져오는 것을 알 수 있다.
