# 0725. OOP-2 & Exception

### 오늘 실습을 통해 배운 내용

* 상속 `Inheritance`
  - 기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것
- 상속이 필요한 이유
  1. 코드 재사용
    - 상속을 통해 기존 클래스의 속성과 메서드를 재사용
    - 새로운 클래스를 작성할 떄 기존 클래스의 기능을 그대로 활용 + 중복된 코드 필요 X
  2. 계층 구조
    - 상속을 통해 클래스들 간의 계층 구조 형성
    - 부모 클래스와 자식 클래스 간의 관계를 표현
  3. 유지 보수의 용이성
    - 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 됨
    - 코드의 일관성을 유지 & 수정이 필요한 범위를 최소화

- 다중 상속
  - 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속 받을 수 있는 것
  - 중복된 속성이나 메서드가 있는 경우 `상속 순서에 의해 결정`

- 메서드 결정 순서 MRO(Method Resolution Order)
  - 프로그래밍 언어의 신뢰성 있고 확장성 있는 클래스를 설계할 수 있도록 도움
  - 클래스 간의 메서드 호출 순서가 예측 가능하게 유지되며, 코드의 재사용성과 유지보수성이 향상
  - 필요한 이유
    - 부모 클래스들이 여러 번 액세스 되지 않도록, 각 클래스에서 지정된 왼쪽에서 오른쪽으로 가는 순서를 보존
    - 각 부모를 오직 한 번만 호출하고, 부모들의 우선순위에 영향을 주지 않으면서 서브 글래스를 만드는 단조적인 구조 형성
  - `super()`
    - 부모 클래스 객체를 반환하는 내장 함수
    - 다중 상속 시 MRO를 기반으로 현재 클래스가 상속하는 모든 부모 클래스 중 다음에 호출될 메서드를 결정하여 자동으로 호출
    ```py
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class Student(Person):
        def __init__(self, name, age, student_id):
            # Person의 init 메서드 호출
            super().__init__(name, age)
            self.student_id = student_id
    ```
  - `mro()`
    - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
    - 기존의 인스턴스-> 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 -> 자식 클래스 -> 부모 클래스로 확장

    ```python
    class A:
        def __init__(self):
            print('A Constructor')

    class B(A):
        def __init__(self):
            super().__init__()
            print('B Constructor')

    class C(A):
        def __init__(self):
            super().__init__()
            print('C Constructor')
          
    class D(B, C):
        def __init__(self):
            super().__init__()
            print('D Constructor')


    print(D.mro())

    '''
    [<class '__main__.D'>, 
    <class '__main__.B'>, <class '__main__.C'>, 
    <class '__main__.A'>, <class 'object'>]
    '''
    ```
    ----
    </br>

  - 디버깅 `Debugging`
    - 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정
    - 프로그램의 오작동 원인을 식별하여 수정하는 작업 
    - print 함수 활용, python tutor 활용
    - 개발 환경(text editor, IDE)에서 제공하는 기능(breakpoint, 변수 조회 등) 활용
  - 에러 `Error`
    - 문법 에러 + 예외
    - 프로그램 실행 중에 발생하는 예외 상황
  - 문법 에러 `Syntax Error`
    - 프로그램의 구문이 올바르지 않은 경우 발생
    - 문법 오류 (Invalid Syntax)
    - 잘못된 할당 (assign to literal)
    - EOL (End Of Line)
    - EOF (End of File)

  - 예외 `Exception`
    - 프로그램 실행 중에 감지되는 에러
    - 내장 예외 Built-in Exceptions
    - 예외 상황을 나타내는 예외 클래스들
    
  - 예외 처리 `Exception Handling`
    - 예외가 발생했을 때 프로그램이 비정상적으로 종료되지 않고, 적절하게 처리할 수 있도록 하는 방법


  

* ....


## A. 첫번째 문제 제목

* 주요 요구 사항 : 이 편지는 영국으로 부터 API 를 요청하여 데이터를 가져와 가공한 데이터...

* 결과 : 10명의 사람에게 보내지 않으면 ....
  
  * 기억해볼 부분
  
    ```
    배운 부분에 대한 코드 조각
    ```
  
    * 핵심 내용
    * 생각해본 다른 활용 법
  * 트러블 슈팅한 부분
  
    ```
    트러블 코드 조각
    ```
  
    * 트러블 현상 및 에러 정보
    * 원인 및 해결 방법

-----

....





# 오늘 후기

* 오늘 프로젝트는 쉬워 보였지만 나의 착각이었다.
* 고수가 되기 위해 오늘도 난 매진한다!
* 일단 롤 한 판 하고... 
* 라고 생각만 하고 열공해야겠다!



### 참고 사이트

* [파이썬 공식 문서 JSON 파트](https://docs.python.org/3.9/library/json.html)
* ...
