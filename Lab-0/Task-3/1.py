import time


start = time.perf_counter()
with open('input.txt') as f:
    n = int(f.readline())
if n == 0: answer = 0
elif n == 1: answer = 1
else:
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % 10
    answer = b
with open('output.txt', 'w') as f:
    f.write(str(answer))
print(time.perf_counter() - start)
