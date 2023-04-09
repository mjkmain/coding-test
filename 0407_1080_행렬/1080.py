N, M = list(map(int, input().split()))

arr1 = [list(map(int, input())) for _ in range(N)]
arr2 = [list(map(int, input())) for _ in range(N)]

def change_matrix(arr, x=0, y=0):
    for row in range(x, x+3):
        for col in range(y, y+3):
            if arr[row][col] == 0:
                arr[row][col] = 1
            else:
                arr[row][col] = 0
    return arr

def print_matrix(arr):
    for row in arr:
        print(row)

count = 0
for row in range(N-2):
    for col in range(M-2):
        if arr1[row][col] != arr2[row][col]:
            arr1 = change_matrix(arr1, row, col)
            count += 1

if arr1 != arr2:
    print(-1)
else:
    print(count)
