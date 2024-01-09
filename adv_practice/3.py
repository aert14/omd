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

    def __eq__(self, __value: object) -> bool:
        """Redefine __eq__."""
        if isinstance(__value, Color):
            return self.red_level == __value.red_level and self.green_level ==\
                  __value.green_level and self.blue_level == __value.blue_level
        return None

    def __add__(self, __value: object) -> object:
        """Redefine __add__."""
        if isinstance(__value, Color):
            new_red = min(self.red_level + __value.red_level, 255)

            new_blue = min(self.blue_level + __value.blue_level, 255)

            new_green = min(self.green_level + __value.green_level, 255)

            return Color(new_red, new_green, new_blue)
        return None


if __name__ == "__main__":
    c_1 = Color(255, 0, 0)
    c_2 = Color(0, 255, 0)
    print(c_1 + c_2)
