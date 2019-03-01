N = int(input())
card_nums =[]
for i in range(N):
    card_nums.append(input())

# 全てのカード番号に対し
for num in card_nums:
    # 偶数桁の数字をそれぞれ2倍し総和をとったものをeven
    # 2, 4, 6, ...
    even = 0
    for n in num[:-1][::2]:
        n_tmp = int(n)
        even += n_tmp*2 if n_tmp*2 < 10 else int(n_tmp*2/10) + n_tmp*2%10
    # 奇数桁の数字の総和をとったものをodd
    # 1, 3, 5, ...
    odd = 0
    for n in num[:-1][1::2]:
        n_tmp = int(n)
        odd += n_tmp
    
    sum = even + odd
    # sumに最も近い10の倍数を求める
    if sum % 10 == 0:
        print("0")
    else:
        ten = int(sum/10)
        target = (ten+1)*10
        print(str(target-sum))
