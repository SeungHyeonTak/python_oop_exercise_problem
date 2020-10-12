# 연습문제 1
# 다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하기
# 학생 클래스의 객체는 객체생성시 국어, 영어, 수학 점수를 저장하고 수정할 수 있으며 추가로 총점을 구하는 메서드를 생성해보기

class Student:
    def __init__(self, kor, eng, math):
        self.__kor = kor
        self.__eng = eng
        self.__math = math

    @property
    def kor(self):
        return self.__kor

    @kor.setter
    def kor(self, kor):
        self.__kor = kor

    @property
    def eng(self):
        return self.__eng

    @eng.setter
    def eng(self, eng):
        self.__eng = eng

    @property
    def math(self):
        return self.__math

    @math.setter
    def math(self, math):
        self.__math = math

    def get_average(self):
        return (self.__kor + self.__eng + self.__math) // 3


if __name__ == "__main__":
    kor = 100
    eng = 80
    math = 80
    student = Student(kor, eng, math)

    print("각 과목의 점수")
    print(f"국어 {student.kor} / 영어 {student.eng} / 수학 {student.math}")
    print(f"세과목의 평균 점수는 : {student.get_average()}")
