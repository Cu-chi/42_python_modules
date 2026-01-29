def garden_operations(test) -> None:
    if test == 0:
        try:
            raise ValueError
        except ValueError:
            print("Caught ValueError: invalid literal for int()")
    elif test == 1:
        try:
            raise ZeroDivisionError
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
    elif test == 2:
        try:
            raise FileNotFoundError
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'nono.txt'")
    elif test == 3:
        try:
            raise KeyError
        except KeyError:
            print("Caught KeyError: 'nono'")
    elif test == 4:
        try:
            raise ValueError
        except (ValueError, ZeroDivisionError):
            print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError")
    garden_operations(0)
    print()
    print("Testing ZeroDivisionError")
    garden_operations(1)
    print()
    print("Testing FileNotFoundError")
    garden_operations(2)
    print()
    print("Testing KeyError")
    garden_operations(3)
    print()
    print("Testing multiple errors together...")
    garden_operations(4)
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
