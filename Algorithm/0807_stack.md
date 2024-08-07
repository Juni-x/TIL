# 0807

### 오늘 실습을 통해 배운 내용

- Memoization (Top-down)
  - 동적 계획법의 핵심이 되는 기술
  - 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
    ```python
    def fibo1(n):
      global memo
      if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
      return memo[n]
    
    memo = [0] * (n + 1)
    memo[0] = 0
    memo[1] = 1
    ```
- 동적계획 알고리즘 `Dynamic Programming` (Tabulation / bottom-up 작은->큰)
  - `최적화 문제`를 해결하는 알고리즘
  - 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 주어진 입력의 문제를 해결하는 알고리즘
    ```python
    # 피보나치 수 DP 적용 알고리즘
    def fibo2(n):
      f = [0] * (n + 1)
      f[0] = 0
      f[1] = 1
      for i in range(2, n + 1):
        f[i] = f[i-1] + f[i -2]
      
      return f[n]
    ```
  - DP의 구현 방식
    - revursive 방식 : fibo1()
    - iterative 방식 : fibo2()
    - memoization을 재귀적 구조에서 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적
    - 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생
- 비선형구조인 그래프 구조의 검색 방법
  - 너비 우선 탐색 `Breadth First Search, BFS`
  - 깊이 우선 탐색 `Depth First Search, DFS`
    - 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
    - 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 DFS를 반복해야하므로 LIFO 구조의 `Stack`을 사용
    - DFS 알고리즘 순서
    1. 시작 정점 v를 결정하여 방문한다.
    2. 정점 v에 인접한 정점 중에서
      - 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push 하고 정점 w를 방문한다. 그리고 w를 v하여 다시 2)를 반복한다.
      - 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2)를 반복한다.
    3. stack이 공백이 될 떄까지 2)를 반복한다.
      ```python
      # 초기 상태
      # visited[], stack[] 초기화
      # 배열 visited를 False로 초기화하고, 공백 스텍을 생성
      DFS(v)
        # 시작점 v 방문하여 깊이 우선 탐색을 시작
        visited[v] <- true;
        while{
          if ( v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            push(v);              # 정점 v에 방문하여, v를 스택에 push
            v <- w ; (w에 방문)
            visited[w] <- true;   # 인접 정점 중 오름차순에 따라 w를 선택하여 탐색
          else    # 방문하지 않은 인접 정점이 없으면
            if (스택이 비어 있지 않으면)    # 방문하지 않은 정점이 있을 때까지 pop
              v <- pop(stack);
            else
              break
        }
      end DFS()
      ```
      ```python
      # 연습 문제
      """
      1
      7 8
      1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
      """
      def DFS(s, V):              # s 시작정점, V 정점개수(1번부터인 정점의 마지막 정점)
          visited = [0] * (V+1)   # 방문한 정점을 표시
          stack = []              # stack 생성
          PRINT(s)
          visited[s] = 1          # 시작정점 방문 표시
          v = s
          while True:
            for w in adjL[v]:     # v에 인접하고, 방문 안 한 w가 있으면
              if visited[w] == 0:
                stack.append(v)   # push(v) 현재 정점을 push하고 
                v = w             # w에 방문
                print(v)
                visited[w] = 1    # w에 방문 표시
                break             # for w 에 대한 break, v부터 다시 탐색
            else:                 # for-else문 : (남은 인접 정점이 없어서) break가 걸리지 않은 경우
              if stack:           # 이전 갈림길을 스택에서 꺼내서.. if TOP > -1
                v = stack.pop()
              else:               # 되돌아갈 곳이 없거나, 남은 갈림길이 없으면 탐색 종료
                break             # while True:에 대한 break
                

      T = int(input())
      for tc in range(1,  T+!):
        V, E = map(int, input().split())
        adjL = [[] for _ in range(V+1)]
        arr = list(map(int, input().split()))
        for i in range(E):
          v1, v2 = arr[i*2], arr[i*2+1]
          adjL[v1].append(v2)   # [[], [2. 3]. [4. 5], [7], [6], [6], [7], []]
          adjL[v2].append(v1)   # [[], [2. 3]. [1, 4. 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]

        DFS(1, V)
      ```



링크 넣기 [Leaderboard 사진](https://www.vellum.ai/llm-leaderboard)
    
사진 넣기 ![Untitled](photo/photo_.png)

</br>

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
</br>

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
</br>

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

</br>




## 오늘 후기

* 오늘 프로젝트는 쉬워 보였지만 나의 착각이었다.
* 고수가 되기 위해 오늘도 난 매진한다!
* 일단 롤 한 판 하고... 
* 라고 생각만 하고 열공해야겠다!



### 참고 사이트

* [파이썬 공식 문서 JSON 파트](https://docs.python.org/3.9/library/json.html)
* ...
