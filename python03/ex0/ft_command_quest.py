import sys

if __name__ == "__main__":
    args_len = len(sys.argv)
    print("=== Command Quest ===")
    if args_len <= 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if args_len > 1:
        print(f"Arguments received: {args_len - 1}")
    i = 1
    while i < args_len:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1

    print(f"Total arguments: {args_len}")
