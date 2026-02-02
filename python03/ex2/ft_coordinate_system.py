import sys
import math


class CoordinatesError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def get_distance(pos_1: tuple[int, int, int],
                 pos_2: tuple[int, int, int]) -> float:
    x1: int
    y1: int
    z1: int
    x2: int
    y2: int
    z2: int
    x1, y1, z1 = pos_1
    x2, y2, z2 = pos_2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def main() -> None:
    args_len: int = len(sys.argv)
    print("=== Game Coordinate System ===\n")

    pos_1: tuple[int, int, int] = (10, 20, 5)
    pos_2: tuple[int, int, int] = (0, 0, 0)
    print(f"Position created: {pos_1}")
    print(f"Distance between {pos_2} and {pos_1}: "
          f"{get_distance(pos_1, pos_2):.2f}\n")

    i: int = 1
    while i < args_len:
        arg: str = sys.argv[i]
        try:
            pos: tuple[int, ...] = tuple([int(value)
                                          for value in arg.split(",")])
            if (len(pos) != 3):
                raise CoordinatesError("Coordinates must be 'int,int,int'")
            print(f"Parsing coordinates: {arg}")
            print(f"Parsed position: {pos}")
            print(f"Distance between {pos_2} and {pos}: "
                  f"{get_distance(pos, pos_2):.2f}\n")
        except Exception as e:
            print(f"Parsing invalid coordinates: \"{arg}\"")
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {e.__class__.__name__}"
                  f", Args {e.args}\n")
        i += 1

    print("Unpacking demonstration:")
    x: int
    y: int
    z: int
    x, y, z = (3, 4, 0)
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
