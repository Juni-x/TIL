class Stack:
    # stack 당 개별적으로 top 변수 관리가 되어야 함
    # 인스턴스 변수로 개별 값으로 관리할 필요있음
    # 클래스 변수로 top 을 관리하면 top 값이 공유가 됨 (인스턴스가 똑같이 동작)
    def __init__(self, size):   # size : stack의 크기를 나타냄
        self.s = [None] * size  # 빈 스택을 생성
        self.top = -1           # top 변수는 초기값 -1
        self.size = size        # stack 크기를 저장
        
    # push 메서드 구현
    def push(self, value):
        # 가득 차 있는 지 확인
        if (self.top + 1) == self.size:
            print('Stack is FULL!!')
            return 
        else:
            self.top += 1
            # 가득차 있지 않을 때는 
            self.s[self.top] = value   
    
    # 스택이 비어있는지 확인하는 메서드
    def is_empty(self):
        # if self.top == -1:
        #     return True
        # else:
        #     return False
        return self.top == -1
    
    # 가장 윗쪽 값 확인
    # def peek(self):
    #     if self.is_empty():
    #         print('Stack is Empty')
    #         return
    #     else:
    #         return self.s[self.top]


    # pop 메서드 구현
    def pop(self):
        # 스택이 비어있다면
        if self.is_empty():
            print('Stack is Empty!!')
            return
        else:
            # 교재
            # self.top -= 1
            # return self.s[self.top + 1]
            # 값도 삭제하고 싶다.
            temp = self.s[self.top]     # 현재 top 위치의 값을 임시 저장
            self.s[self.top] = None     # 값 지우기
            self.top -= 1               # top 감소
            return temp                 # 아까 저장한 가장 위의 값을 반환

        # 단순 참고
        # temp = self.peek()
        # if temp:
        #     return
        # else:
        #     self.top -= 1
        #     return temp

    # <__main__.Stack object at 0x000001C5C7720FD0>
    def __str__(self):
        return f'{self.s}'

# set1 = set()
stack1 = Stack(5)

print(stack1)
stack1.push(100)
stack1.push(200)
stack1.push(300)
stack1.push(400)
stack1.push(500)
print(stack1)
stack1.push(600)
print(stack1)

res1 = stack1.pop()
print(stack1, res1)
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
print(stack1)
        
        
        
        