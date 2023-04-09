N = int(input())
arr = list(map(int, input().split()))

dp = [1]*(len(arr))

for i in range(len(arr)-1):
    max_val = max(dp)
    if arr[i] > arr[i+1]:
        dp[i+1] = dp[i]+1
    
    else:
        dp[i+1] = dp[i]

print(max(dp))
