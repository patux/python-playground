# TODO create the fibonacci generator and find the first Fibonacci number > 100
def fibonacci():
  a, b = 0, 1
  while True:
    a, b = b, a + b
    yield b


# Example usage:
for fib in fibonacci():
    if fib > 100:
        print(f"The first Fibonacci number greater than 100 is: {fib}")
        break