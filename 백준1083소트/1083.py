N = int(input())
arr = list(map(int, input().split(" ")))
S = int(input())

def print_arr(arr):
    print(" ".join(map(str, arr)))

save_arr = []

while True:
    try:
        if S == 0:
            break
        
        maxval, maxidx = max(arr), arr.index(max(arr))
        if S < maxidx:
            new_arr = arr[:S+1]
            maxval, maxidx = max(new_arr), new_arr.index(max(new_arr))
            save_arr.append(maxval)
        else:
            save_arr.append(maxval)
        
        arr.remove(maxval)
        S -= maxidx
    
    except Exception:
        break

save_arr.extend(arr)
    
print_arr(save_arr)