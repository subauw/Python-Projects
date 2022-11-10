x = 5
for i in range(x):
    for j in range(x - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

for i in range(x - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(x - i - 1) - 1):
        if j == 0 or j == 2*(x - i - 1) - 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()