# Bottom-up
import random  # 램덤 모듈 임포트
import pprint  # pretty print 모듈 임포트

arr = ['A', 'C', 'G', 'T']  # 수열을 구성하는 원소

while True:
    X = ""
    Y = ""
    n = int(input("Size: "))  # 생성할 문자열의 길이
    for _ in range(n):
        X += random.choice(arr)  # 아무 원소나 하나 뽑아주는 choice() 함수
        Y += random.choice(arr)  # 아무 원소나 하나 뽑아주는 choice() 함수

    print("X: ", X)  # 입력 수열1 출력
    print("Y: ", Y)  # 입력 수열2 출력

    matrix = [[0 for col in range(len(Y) + 1)] for row in range(len(X) + 1)] 
    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            if X[i - 1] == Y[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                if matrix[i][j-1] >= matrix[i-1][j]:
                    matrix[i][j] = matrix[i][j-1]
                else:
                    matrix[i][j] = matrix[i-1][j]

    print("Length of LCS: ", matrix[-1][-1])

    pprint.pprint(matrix)
    print("")
