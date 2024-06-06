def incremental_for_loop(start, step):
    """Generates an incremental for loop."""
    current = start
    while True:
        yield current
        current += step


# Example usage:
start = int(input("Enter the start number: "))
step = int(input("Enter the step size: "))
for number in incremental_for_loop(start, step):
    print(number)
