def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

while True:
    try:
        # Prompt the user to enter a positive integer
        number = int(input("Enter a positive integer: "))
        if number > 0:
            sequence = collatz_sequence(number)
            print(f"The Collatz sequence for {number} is: {sequence}")
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
