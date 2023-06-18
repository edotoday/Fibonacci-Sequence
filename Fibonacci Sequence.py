def fibonacci(n):
    if n <= 0:
        return []

    sequence = [0, 1]
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)

    return sequence

num_terms = int(input("Enter the number of terms: "))
fib_seq = fibonacci(num_terms)
print(fib_seq)
