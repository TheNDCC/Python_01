hashFibo = {}


def fibonacci(n):
    if n in hashFibo:
        return hashFibo[n]
    if n <= 1:
        return 1
    result = fibonacci(n-1) + fibonacci(n-2)
    hashFibo[n] = result
    return result


for i in range(100):
    print(fibonacci(i))
