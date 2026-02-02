import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    args_len: int = len(sys.argv)
    if args_len <= 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              "<score1> <score2> ...")

    scores: list[int] = []
    for arg in sys.argv[1:]:
        try:
            scores = scores + [int(arg)]
        except ValueError:
            print(f"Error: conversion error of '{arg}' to int")
            return
    print(f"Scores processed: {scores}")
    print(f"Total players: {args_len - 1}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / (args_len - 1)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
