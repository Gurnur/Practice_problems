import sys

def solution(num):
    count = 2
    tmp = 2
    if len(num) == 0:
        return 0

    for i in range(2, len(num)):
        if num[i] == num[i-2]:
            count += 1
        else:
            if count > tmp:
                tmp = count
                count = 2
    return count

A = [3, -7, 3, 7, 3]
print(solution(A))

'''
for line in sys.stdin:
    num = []
    line = line.rstrip().split(' ')
    for l in line:
        num.append(int(l))
    print (solution(num))
'''