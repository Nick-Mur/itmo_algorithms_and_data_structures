while True:
    try:
        print(sum(map(int, input().split())))
        break
    except:
        print('Неверный ввод')
