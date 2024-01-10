def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci (n - 1) + fibonacci (n - 2)
    
def lucas (n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas (n - 1) + lucas (n - 2)
    
def sum_series (n, param1 = 0, param2 = 1):
    if n == 0:
        return param1
    elif n == 1:
        return param2
    # Note to self for when I inevitably forget how I did this: param1 and param2 are the first two numbers in the series with default values of 0 and 1 (Fibonacci); this function can also be used to generate any other series that uses the same formula after the first two numbers. The user entering the parameters must know the correct first two numbers for the series they want to generate.
    else:
        return sum_series (n - 1, param1, param2) + sum_series (n - 2, param1, param2)
