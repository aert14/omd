class Color:
    """Color class."""

    def __init__(self, red_level: int, green_level: int, blue_level: int):
        self.red_level = red_level
        self.green_level = green_level
        self.blue_level = blue_level

    def __str__(self) -> str:
        """Redefine __str__."""
        end = "\033[0"
        start = "\033[1;38;2"
        mod = "m"
        return (f"{start};{self.red_level};{self.green_level};"
                f"{self.blue_level}{mod}●{end}{mod}")


if __name__ == "__main__":
    c = Color(255, 0, 255)
    print(c)
