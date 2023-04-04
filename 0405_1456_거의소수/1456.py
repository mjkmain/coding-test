import math

A = 1
B = 10
arr = list(range(B+1))

prime_list = [True] * (B+1)

for i in range(2, int(B ** 0.5)+1):
    for j in range(i+i, B+1, i):
        prime_list[j] = False

prime_list = prime_list[A:]
prime_nums = []
for idx in range(len(prime_list)):
    if prime_list[idx] == True:
        prime_nums.append(idx+A)

print(prime_nums)

count = 0
for num in prime_nums[1:]:
    if (num**2 < B+1) and (num**2 > A):
        print(num**2)
        count += 1
    else:
        break

print(count)