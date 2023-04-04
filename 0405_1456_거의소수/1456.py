A, B = list(map(int, input().split()))

prime_list = list(range(0, int(B**0.5)+1))

for i in range(2, int(B ** 0.5)+1):
    if prime_list[i] > 0:
        for j in range(i+i, int(B**0.5)+1, i):
            prime_list[j] = -1


prime_list[0] = -1
prime_list[1] = -1

count = 0
for prime_num in prime_list:
    if prime_num > 0:
        i = 2
        while True:
            
            if (prime_num**i <= B) and (prime_num**i >= A):
                count += 1
                i += 1
            elif (prime_num**i <= B) and not(prime_num**i >= A):
                i += 1
            else:
                break

print(count)