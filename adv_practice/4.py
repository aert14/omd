END = "\033[0"
START = "\033[1;38;2"
MOD = "m"
MAX_COLOR_VALUE = 255

class Color:

    def __init__(self, red_level: int, green_level: int, blue_level: int):
        self.red_level = red_level
        self.green_level = green_level
        self.blue_level = blue_level

    def __str__(self) -> str:

        return f"{START};{self.red_level};{self.green_level};{self.blue_level}{MOD}●{END}{MOD}"

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Color):
            return self.red_level == __value.red_level and self.green_level ==\
                  __value.green_level and self.blue_level == __value.blue_level
        return None

    def __add__(self, __value: object) -> object:
        if isinstance(__value, Color):
            new_red = min(self.red_level + __value.red_level, 255)

            new_blue = min(self.blue_level + __value.blue_level, 255)

            new_green = min(self.green_level + __value.green_level, 255)

            return Color(new_red, new_green, new_blue)
        return None
    def __hash__(self):
        return hash((self.red_level, self.green_level, self.blue_level))

if __name__ == "__main__":
    c_1 = Color(255, 0, 0)
    c_2 = Color(0, 255, 0)
    for i in {c_1, c_2, c_1}:
        print(i)
