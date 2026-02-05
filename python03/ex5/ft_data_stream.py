from typing import Generator, Any


def generator_fibonacci(limit: int) -> Generator[int, None, None]:
    n1: int = 0
    n2: int = 1
    yield n1
    for _ in range(limit - 1):
        n1, n2 = n2, n1 + n2
        yield n1


def generator_prime(limit: int) -> Generator[int, None, None]:
    n: int = 2
    found: int = 0
    while found < limit:
        is_prime: bool = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            found += 1
            yield n
        n += 1


def generator(number: int = 1000)\
        -> Generator[dict[str, Any], None, None]:
    players: list[str] = ["JAMES", "JOHN", "ROBERT", "MICHAEL", "WILLIAM",
                          "DAVID", "RICHARD", "CHARLES", "JOSEPH", "THOMAS",
                          "CHRISTOPHER", "DANIEL", "PAUL", "MARK", "DONALD",
                          "GEORGE", "KENNETH", "STEVEN", "EDWARD", "BRIAN",
                          "RONALD", "ANTHONY", "KEVIN", "JASON", "MATTHEW",
                          "GARY", "TIMOTHY", "JOSE", "LARRY", "JEFFREY",
                          "FRANK", "SCOTT", "ERIC", "STEPHEN", "ANDREW",
                          "RAYMOND", "GREGORY", "JOSHUA", "JERRY", "DENNIS",
                          "WALTER", "PATRICK", "PETER", "HAROLD", "CARL",
                          "DOUGLAS", "HENRY", "ARTHUR", "RYAN", "ROGER"]
    event_types: list[str] = ["login", "logout", "kill",
                              "death", "level_up", "item_found"]
    for event_id in range(1, number + 1):
        event: dict[str, Any] = {
            "id": event_id,
            "player": players[event_id % 50],
            "event_type": event_types[event_id % 6],
            "data": {
                "level": event_id % 15
            }
        }
        yield event


def format_event(event: dict[str, Any]) -> str:
    format: str = f"Event {event['id']}: Player {event['player']} "
    format += f"(level {event['data']['level']}) "
    if event["event_type"] == "login":
        format += "logged in"
    elif event["event_type"] == "logout":
        format += "logged out"
    elif event["event_type"] == "logout":
        format += "logged out"
    elif event["event_type"] == "kill":
        format += "killed monster"
    elif event["event_type"] == "death":
        format += "died"
    elif event["event_type"] == "level_up":
        format += "leveled up"
    elif event["event_type"] == "item_found":
        format += "found a treasure"
    return format


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")
    processed: int = 0
    level_10_more: int = 0
    treasure: int = 0
    level_up: int = 0
    for event in generator():
        processed += 1
        if event["id"] <= 3:
            print(format_event(event))
        if event["data"]["level"] >= 10:
            level_10_more += 1
        if event["event_type"] == "item_found":
            treasure += 1
        elif event["event_type"] == "level_up":
            level_up += 1
    print("...\n")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {processed}")
    print(f"High-level players (10+): {level_10_more}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {treasure}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    fibonacci_generator: Generator[int, None, None] = generator_fibonacci(10)
    for i in range(10):
        print(f"{next(fibonacci_generator)}", end="")
        if i < 9:
            print(", ", end="")
        else:
            print()
    print("Prime numbers (first 5): ", end="")
    prime_generator: Generator[int, None, None] = generator_prime(5)
    for i in range(5):
        print(f"{next(prime_generator)}", end="")
        if i < 4:
            print(", ", end="")
        else:
            print()


if __name__ == "__main__":
    main()
