# Факториал числа и отбросить все нули

n = int(input())
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)

def remove_ziro(k):
    return int(str(k).rstrip('0'))

print(remove_ziro(fact(n)))
