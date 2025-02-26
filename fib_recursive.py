def fib_recursive(n):
    if n <= 1:
        return n
    if n > 30:
        raise RecursionError("Recursão muito profunda")
    return fib_recursive(n-1) + fib_recursive(n-2)
