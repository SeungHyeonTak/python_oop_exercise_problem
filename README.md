## 객체지향 연습하기

#### 연습문제 1
> 다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하시오.
> 이때 학생 클래스의 객체는 객체 생성시 국어 / 영어 / 수학 점수를 저장하며, 총점을 구하는 메서드를 제공한다.

**알고가기** <br>
@property란 무엇인가? <br>
python에서 @property 데코레이터를 이용하여 다른언어에서 사용되는 getter / setter 메소드 보다 더욱 직관적이게 표현가능하다. <br>
해당 문제 코드를 보면 알 수 있듯이 get부분은 property가 하고 set부분은 해당 함수뒤에 setter를 붙이는 형식으로 사용된다. <br>
참고로 property가 setter보다 윗줄에 사용되어야 한다.<br>
*****

#### 연습문제 2
> 국적을 출력하는 printNationality 정적 메서드를 갖는<br> 
> Korean 클래스를 정의하고 메서드를 호출하는 코드를 작성하자.

**알고가기** <br>
정적메소드란 무엇인가? <br>
정적메소드는 클래스에서 직접 접근할 수 있는 메소드이다. <br>
파이썬에서 사용할 수 있는 메소드는 두가지가 있다. `@staticmethod`와 `@classmethod` 이렇게 두가지이다. <br>
staticmethod는 따로 인자를 가질 필요없다. classmethod는 인스턴스 메소드와 달리 self가 아닌 cls라는 인자를 사용한다. <br>
그러면 차이가 뭐냐?  <br>
staticmethod는 부모클래스의 속성 값을 가져오지만 classmethod는 현재 클래스의 클래스 속성을 가져온다. 코드를 보고 이해할 수 있길 바란다.
*****

#### 연습문제 3
> name 프로퍼티를 가진 Student를 부모 클래스로 major 프로퍼티를 가진 <br>
> GraduateStudent 자식 클래스를 정의하고 이 클래스의 객체를 <br>
> 다음과 같이 문자열로 출력하는 코드를 작성하십시오. <br>

**알고가기** <br>
부모클래스와 자식클래스의 상속 관계를 어느정도 알고 갈 수 있는 부분 <br>
`super().__init__()`에 대해 알 수 있다.<br>
super()란 무엇인가?<br>
즉, 자식클래스에서 부모클래스의 내용을 사용하고 싶을 경우 사용할 수 있게 해주는 문구이다.<br>
아직 잘 모르겠다면 `오버라이딩`에 대해 알고오면 이해하기 쉬울것이다.<br>
*****

#### 연습문제 4
> 반지름 정보를 갖고, 원의 면적을 계산하는 메서드를 갖는 Circle 클래스를 정의하고,<br>
> 생성한 객체의 원의 면적을 출력하는 프로그램을 작성하십시오.<br>
*****

#### 연습문제 5
> 가로, 세로 정보을 갖고, 사각형의 면적을 계산하는 메서드를 갖는 Rectangle 클래스를 정의하고,<br>
> 생성한 객체의 사각형의 면적을 출력하는 프로그램을 작성하십시오.<br>
*****

#### 연습문제 6
> Shape를 부모 클래스로 Square 자식 클래스를 정의하는 코드를 작성하십시오.<br>
> Square 클래스는 length 필드를 가지며, 0을 반환하는 Shape 클래스의 area 메서드를<br>
> length * length 값을 반환하는 메서드로 오버라이딩합니다.<br>

**알고가기**<br>
오버라이딩이 무엇인가?<br>
간단하게 설명하자면 부모클래스의 메소드를 자식클래스에서 재정의한다고 생각하면 된다.<br>
**다른언어의 오버로딩 개념이 있지만 python에선 지원되지 않는다.**
*****

#### 연습문제 7
> Person를 부모 클래스로 Male, Female 자식 클래스를 정의하는 코드를 작성하십시오.<br>
> "Unknown"을 반환하는 Person 클래스의 getGender 메서드를 Male 클래스와 Female 클래스는<br>
> "Male", "Female" 값을 반환하는 메서드로 오버라이딩합니다.<br>