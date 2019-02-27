N = int(input())
for i in range(N):
    yakusu_sum = 0
    n_i = int(input())
    for j in range(1, n_i):
        if n_i % j == 0 and not j == n_i:
            yakusu_sum += j

    if yakusu_sum == n_i:
        print("perfect")
    elif abs(yakusu_sum-n_i) == 1:
        print("nearly")
    else:
        print("neither")