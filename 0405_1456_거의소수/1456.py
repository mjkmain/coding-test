A, B = list(map(int, input().split()))

prime_list = list(range(0, B+1))

for i in range(2, int(B ** 0.5)+1):
    if prime_list[i] > 0:
        for j in range(i+i, B+1, i):
            prime_list[j] = -1

prime_list[0] = -1
prime_list[1] = -1

count = 0
for num in range(len(prime_list)):
    cur_num  = prime_list[num]
    if cur_num > 0:
        i = 2
        while True:
            
            if (cur_num**i <= B) and (cur_num**i >= A):
                count += 1
                i += 1
            else:
                break

print(count)