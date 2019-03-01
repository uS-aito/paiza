N, M = [int(x) for x in input().split(" ")]

goukaku = []
for i in range(N):
    a, b = [int(x) for x in input().split(" ")]
    score = (a - b*5) 
    if score < 0:
        score = 0
    if score >= M:
        goukaku.append(i+1)

for g in goukaku:
    print(g)