# Fibonacci Sequence Generator in Python

def fibonacci(n):
    """
    Generates the Fibonacci sequence up to the n-th term.

    Parameters:
    n (int): The number of terms in the Fibonacci sequence to generate.

    Returns:
    list: A list containing the Fibonacci sequence up to n terms.
    """
    # Check if the input is valid
    if n <= 0:
        print("Please enter a positive integer.")
        return []

    # Initialize the first two terms of the Fibonacci sequence
    sequence = [0, 1]

    # If only the first term is requested, return it
    if n == 1:
        return [0]

    # Generate the Fibonacci sequence up to the n-th term
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]  # Sum of the last two terms
        sequence.append(next_term)

    return sequence


# Driver code to test the function
if __name__ == "__main__":
    # Get input from the user for the number of terms
    try:
        num_terms = int(input("Enter the number of terms: "))
        # Call the fibonacci function and print the result
        result = fibonacci(num_terms)
        if result:
            print(f"Fibonacci sequence up to {num_terms} terms: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
