def inv_A(num):
    return num//2

def inv_B(num):
    return (num - 1)/10

start, target = map(int, input().split())
count = 0

while True:
    if target%2 == 0:
        target = inv_A(target)
        count += 1
    
    elif target%10 == 1:
        temp = target
        target = inv_B(target)
        count += 1

    else:
        print(-1)
        break

    if target == start:
        count += 1
        print(count)
        break

    if target == 0:
        print(-1)
        break