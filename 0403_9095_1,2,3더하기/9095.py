# 1 : 1
# 2 : 1 + 1, 2
# 3 : 1 + 1 + 1, 2 + 1, 1 + 2, 3
# 4 : 1+1+1+1 1+1+2 1+2+1 2+1+1 2+2 3+1 1+3
# 4 : 1+1+1+(1) 2+1+(1) 3+(1) 1+1+(2) 2+(2) 1+(3)
# f(n) = f(n-1) + f(n-2) + f(n-3)


dp = [0]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

T = int(input())

input_arr = []
for _ in range(T):
    input_arr.append(int(input()))

for d in input_arr:
    print(dp[d])