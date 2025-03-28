# Алгоритм бутера 3 задача
def booth(s):
    s = s+s
    n = len(s) // 2
    f = [-1] * (2 * n)
    k = 0

    for j in range(1, 2 * n):
        i = f[j - k - 1]
        while i != -1 and s[j] != s[k + i + 1]:
            if s[j] < s[k + i + 1]:
                k = j - i - 1
            i = f[i]

        if s[j] != s[k + i + 1]:
            if s[j] < s[k]:
                k = j
            f[j-k] = -1

        else:
            f[j-k] = i + 1

    return s[k:k + n]

print(booth("bac"))
