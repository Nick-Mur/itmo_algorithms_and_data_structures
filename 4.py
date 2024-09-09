with open('input — копия.txt') as f:
    n = int(f.readline())
if n == 0: print(0)
elif n == 1: print(1)
else:
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
with open('output — копия.txt', 'w') as f:
    f.write(str(b))
