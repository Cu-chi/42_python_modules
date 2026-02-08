import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    args_len: int = len(sys.argv)
    if args_len <= 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
        return

    scores: list[int] = []
    proceed: int = 0
    for arg in sys.argv[1:]:
        try:
            scores = scores + [int(arg)]
            proceed += 1
        except ValueError:
            print(f"Error: conversion error of '{arg}' to int")
    if proceed == 0:
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {proceed}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / (proceed)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
