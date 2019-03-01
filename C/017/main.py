a, b = [int(x) for x in input().split(" ")]
n = int(input())
for i in range(n):
    A, B = [int(x) for x in input().split(" ")]
    if a < A:
        print("Low")
    elif a == A and b > B:
        print("Low")
    else:
        print("High")