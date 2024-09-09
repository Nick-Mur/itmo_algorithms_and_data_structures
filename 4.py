with open('input — копия.txt') as f:
    n = int(f.readline())
if n == 0: answer = 0
elif n == 1: answer = 1
else:
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    answer = b
with open('output — копия.txt', 'w') as f:
    f.write(str(answer))
