# 연습문제 7
# Person을 부모클래스로 Male, Female를 자식 클래스를 정의하는 코드를 작성하시오.
# "Unknown"을 반환하는 Person 클래스의 getGender 메서드를 Male 클래스와 Female 클래스는 "Male", "Female"값을 반환하는 메서드로 오버라이딩하기

class Person:
    def getGender(self):
        return "Unknown"


class Male(Person):
    def getGender(self):
        return "Male"


class Female(Person):
    def getGender(self):
        return "Female"


if __name__ == "__main__":
    male = Male()
    female = Female()

    print(f"아들:{male.getGender()} / 딸:{female.getGender()}")
