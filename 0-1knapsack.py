# 0-1 배낭 문제 (0-1 knapsack problem)
import random as rand  # 램덤 모듈 임포트
import timeit  # 함수 및 코드 실행시간 측정
import pprint  # pretty print 모듈 임포트20


# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
def knapsack(B, wt, val, num):
    memo = [[0] * (B + 1) for _ in range(num + 1)]  # 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
    for n in range(num + 1):  # 왼쪽에서 오른쪽으로 요소를 계산하여 채워나가고
        for w in range(B + 1):  # 그 다음 행을 채워나감
            if n == 0 or w == 0:  # 첫 번째 행과 첫 번째 열은
                memo[i][w] = 0  # 0으로 초기화
            elif wt[n - 1] <= w and w - wt[n - 1] >= 0:  # 배낭의 무게한도보다 물건의 무게가 작거나 같으면
                # i번째 물건을 위해 i번째 물건의 무게를 비웠을 때의 최적해에 i번째 물건의 가치를 더한 값과
                # i-1개의 물건을 가지고 구한 전 단계의 최적해 중 큰 값 선택
                memo[n][w] = max(val[n - 1] + memo[n - 1][w - wt[n - 1]], memo[n - 1][w])
            else:  # 배낭의 무게한도보다 물건의 무게가 큰 경우 물건을 넣을 수 없으므로
                memo[n][w] = memo[n - 1][w]  # i번째 물건을 뺀 i-1개의 물건들을 가지고 구한 전 단계의 최적해의 가치 선택
    pprint.pprint(memo)
    return memo[-1][-1]


weight = []  # 물건의 무게
value = []  # 물건의 가치
N = int(input('물품의 수: '))  # 물품의 수 N
K = N**2 // 2  # 배낭의 무게한도 K
for i in range(N):  # 각 물건의 무게 w와 해당 물건의 가치 v를 초기화
    weight.append(i)  # i번째 물건의 무게 w는 i
    value.append(rand.randint(1, 2*N))  # i번째 물건의 가치 v는 1과 2n 사이의 수로 랜덤하게 초기화
print('각 물건의 가치: ', value)
t1 = timeit.default_timer()  # 프로그램 시작시간
print('배낭에 넣을 수 있는 물건들의 가치의 최댓값: ', knapsack(K, weight, value, N))  # 최적해의 가치 출력
t2 = timeit.default_timer()  # 프로그램 종료시간
print("Running time: ", (t2 - t1) * 1000)  # 프로그램 실행시간
