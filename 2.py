while True:
    try:
        a, b = map(int, input().split())
        print(a + b ** 2)
        break
    except:
        print('Неверный ввод')
