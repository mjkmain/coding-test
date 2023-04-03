N = int(input())
stair = [0]

for _ in range(N):
    stair.append(int(input()))

dp = [0] * (len(stair))

dp[1] = stair[1]

if N > 1:
    dp[2] = dp[1] + stair[2]

if N >= 3:
    for i in range(3, len(stair)):
        dp[i] = max(stair[i-1] + dp[i-3] + stair[i], dp[i-2] + stair[i])


print(dp[-1])