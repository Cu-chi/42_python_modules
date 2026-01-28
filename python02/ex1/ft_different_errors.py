def garden_operations(test):
    try:
        if test == 0:
            tester = int("abc")
        elif test == 1:
            tester = 1/0
        elif test == 2:
            tester = open("nono.txt")
        elif test == 3:
            tester = {"t": 0, "b": 1}
            tester["nono"]
        elif test == 4:
            tester = "a" + 2
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'nono.txt'")
    except KeyError:
        print("Caught KeyError: 'nono'")
    except Exception:
        print("Caught an error, but program continues!")


def test_error_types():
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
