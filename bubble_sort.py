left = [60, 30, 20, 70]
right = [20, 50, 60, 90]


def bubble_sort(left):
    for i in range(len(left)-1):  # 外迴圈
        for j in range(len(left)-1-i):
            if left[j] > left[j+1]:
                left[j], left[j+1] = left[j+1], left[j]
    return left


result = bubble_sort(left)
print(result)
print(len(left))  # 4個元素
