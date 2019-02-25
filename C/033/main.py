strike = 0
ball = 0

N = int(input())
for i in range(N):
    result = input()
    if result == "strike":
        strike += 1
    elif result == "ball":
        ball += 1
    
    if strike == 3:
        print("out!")
    elif ball == 4:
        print("fourball!")
    elif result == "strike":
        print("strike!")
    elif result == "ball":
        print("ball!")
