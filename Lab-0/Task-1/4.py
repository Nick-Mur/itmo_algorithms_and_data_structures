with open('input.txt') as f:
    a, b = map(int, f.readline().split())
with open('output.txt', mode='w') as f:
    f.write(str(a + b ** 2))
