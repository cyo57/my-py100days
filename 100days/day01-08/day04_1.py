'''
循环结构
1. for-in
2. while
'''

# 打印三角图案

num = 5
for x in range(num):
    for y in range(x+1):
        print('*', end='')
    print()

for x in range(num):
    for y in range(num):
        if y < num-x-1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

