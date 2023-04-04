import sys
input = sys.stdin.readline

N = int(input())

# input_arr = [[1, 2], [3, 5], [2, 4], [2, 6], [3, 4]]

input_arr = []
for _ in range(N):
    input_arr.append(list(map(int, input().split())))

input_arr = sorted(input_arr, key=lambda x:x[1])

arr = []

arr.append([input_arr[0][1]])
for data in input_arr[1:]:
    i = 0
    flag = True
    end_time = data[1]
    start_time = data[0]

    for i in range(len(arr)):
        if start_time >= max(arr[i]):
            arr[i].append(end_time)
            flag = False
            break

    if flag:
        arr.append([end_time])  

print(len(arr))