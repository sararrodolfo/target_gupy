def fibonacci(n):
    fib_list = [0, 1]
    while fib_list[-1] + fib_list[-2] <= n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    if n in fib_list:
        print(f"{n} pertence a sequência de Fibonacci.")
    else:
        print(f"{n} não pertence a sequência de Fibonacci.")

# exemplo
fibonacci(5) 
fibonacci(10) 
