T = int(input())

arr = []

for _ in range(T):
    arr.append(list(map(int, input().split())))

dp = [0] * (T)

k = 0
for i in range(T):
    day = arr[i][0]
    pay = arr[i][1]

    k = max(k, dp[i])
    if day + i > T:
        continue

    dp[i+day] = max(k + pay, dp[i+day])

print(max(dp))