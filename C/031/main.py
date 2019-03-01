N = int(input())
users = {}
for i in range(N):
    p, s = input().split(" ")
    s = int(s)
    users[p] = s
q, t = input().split(" ")

ref = users[q]
for k in users:
    # 投稿地と表示地の時差をとる
    zisa = users[k] - ref
    # 投稿時刻を分割し、intにする
    h, m = [int(x) for x in t.split(":")]
    # 時差を足す
    h += zisa 
    # 負だった場合
    if h < 0:
        h = 24 + h
    elif h >= 24:
        h = h - 24
    print(str(h).zfill(2) + ":" + str(m).zfill(2))

