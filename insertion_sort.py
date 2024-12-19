# insertion sort

data = [87, 54, 12, 47, 24, 26, 24, 1, 235, 48, 87, 12]


def insertion_sort(data):
    n = len(data)
    for i in range(n-1):
        key = data[i+1]
        j = i
        while j >= 0 and key < data[j]:  # 第1個元素小於第0個元素
            data[j+1] = data[j]  # 第0個元素向右移
            j -= 1
        data[j+1] = key
    return data


print(data)
