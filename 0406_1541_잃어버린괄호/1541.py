input_str = input()

def str_plus(plus_str):
    return sum(list(map(int,plus_str.split("+"))))

cur_sum = 0
init = input_str.split("-")[0]

if input_str.startswith("-"):
    cur_sum -= str_plus(init)

else:
    cur_sum += str_plus(init)

for d in input_str.split("-")[1:]:
    cur_sum -= str_plus(d)

print(cur_sum)