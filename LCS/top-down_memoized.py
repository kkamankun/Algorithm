import string  # 스트링 모듈 임포트
import random  # 랜덤 모듈 임포트
import timeit  # 함수 및 코드 실행시간 측정


def lcs(a, b, k, j, matrix):  # top-down, memoized
    if k == 0 or j == 0:  # 두 수열 중 하나라도 길이가 0이라면,
        return 0  # length of LCS = 0

    if matrix[k - 1][j - 1] != -1:   # 중복 부분 문제라면,
        return matrix[k - 1][j - 1]  # 이전에 계산하여 저장한 값을 재사용

    if a[k - 1] == b[j - 1]:  # 최적 부분 구조 성질 1번

        # store it in arr to avoid further repetitive
        # work in future function calls
        matrix[k - 1][j - 1] = 1 + lcs(X, Y, k - 1, j - 1, matrix)
        return matrix[k - 1][j - 1]

    else:  # 최적 부분 구조 성질 2번, 3번

        # store it in arr to avoid further repetitive
        # work in future function calls
        matrix[k - 1][j - 1] = max(lcs(X, Y, k, j - 1, matrix), lcs(X, Y, k - 1, j, matrix))
        return matrix[k - 1][j - 1]


n = int(input("Size: "))  # 생성할 문자열의 길이
string_pool = string.ascii_uppercase  # 대문자만 이용하여 문자열 생성
X = ""
Y = ""
for i in range(n):  # 랜덤한 문자열 생성
    X += random.choice(string_pool)  # 랜덤한 문자열 하나 선택
    Y += random.choice(string_pool)  # 랜덤한 문자열 하나 선택

print("X: ", X)  # 입력 수열1 출력
print("Y: ", Y)  # 입력 수열2 출력
n = len(Y)  # 입력 수열의 길이 n

dp = [[-1] * (n+1) for _ in range(n+1)]  # 이전에 계산한 값을 저장할 2차원 리스트 선언

t1 = timeit.default_timer()  # LCS 알고리즘 시작시간
print("Length of LCS:", lcs(X, Y, n, n, dp))  # LCS 함수 호출 및 반환값 출력
t2 = timeit.default_timer()  # LCS 알고리즘 종료시간
print("Running time: ", (t2 - t1) * 1000)  # 삽입 정렬 실행시간
