N, K = list(map(int, input().split()))
# N = 7
# K = 3

count = 0
arr = list(range(2, N+1))
for i in range(len(arr)):
    if arr[i] > 0:
        cur_val = arr[i]
        for j in range(i, len(arr)):
            if arr[j] % cur_val == 0:
                target = arr[j]
                arr[j] = -1
                
                count += 1

            if count == K:
                break    
        
        if count == K:
            break

print(target)
