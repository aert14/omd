import sys


def redirect_output(filepath: str) -> callable:
    """Redirect output of the function to the file."""
    def decorator(function: callable) -> callable:
        """Decorate function."""
        def wrapper() -> any:
            """Wrap function."""
            old_write = sys.stdout.write
            with open(filepath, "w") as file:
                sys.stdout.write = file.write
                function()
            sys.stdout.write = old_write
        return wrapper
    return decorator


@redirect_output("./function_output.txt")
def calculate() -> None:
    """Calculate the power of numbers."""
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=" ")
        print()


if __name__ == "__main__":

    calculate()

    with open("./function_output.txt") as file:
        print(file.read())
