def fib(n:int):
     a, b = 0, 1
     while a < n:
        print(a, end=' ')
        a, b = b, a+b

if __name__ == "__main__":
    print(fib(1000))