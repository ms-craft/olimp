arr = [15, 3, 9, 1, 7, 20, 11, 50, 53, 52, 57, 9999]
target = 51
# линейный поиск первая задача
def liner(arr, target):
    return min(arr, key=lambda x: abs(x - target))

print(liner(arr, target))
