import sys
import time


def timed_output(func: callable) -> callable:
    """Add timestamp to the output of the function."""
    def wrapper(*args, **kwargs) -> any:
        """Wrapp function."""
        original_write = sys.stdout.write

        def my_write(string_text: str) -> None:
            """My own write function that adds timestamp to the output."""
            if string_text != "\n":
                curr_time = time.strftime("[%Y-%m-%d %H:%M:%S]: ",
                                          time.localtime())
                string_text = curr_time + string_text
            original_write(string_text)

        sys.stdout.write = my_write
        try:
            return func(*args, **kwargs)
        finally:
            sys.stdout.write = original_write
    return wrapper


if __name__ == "__main__":
    @timed_output
    def print_greeting(name: str) -> None:
        """Print greeting to the user."""
        print(f"Hello, {name}!")

    print_greeting("Nikita")
