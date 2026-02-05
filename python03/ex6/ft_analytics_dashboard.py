from typing import Any


def list_example(data: dict[str, dict[str, Any]]) -> None:
    high_scorers: list[str] = [name
                               for name in data if data[name]["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    doubled_scores: list[str] = [data[name]["score"] * 2
                                 for name in data
                                 if data[name]["score"] > 2000]
    print(f"Scores doubled: {doubled_scores}")
    active_players: list[str] = [name
                                 for name in data if data[name]["active"]]
    print(f"Active players: {active_players}")


def dict_example(data: dict[str, dict[str, Any]]) -> None:
    players_scores: dict[str, Any] = {
        name: data[name]["score"] for name in data if data[name]["active"]
    }
    print(f"Player scores: {players_scores}")
    scores_cat: dict[str, int] = {
        "high": sum([1 for name in data if data[name]["score"] > 2000]),
        "medium": sum([1 for name in data
                       if 1900 < data[name]["score"] < 2200]),
        "low": sum([1 for name in data if data[name]["score"] < 1900])
    }
    print(f"Score categories: {scores_cat}")
    achmnt_count: dict[str, int] = {name: len(data[name]["achievements"])
                                    for name in data if data[name]["active"]}
    print(f"Achievement counts: {achmnt_count}")


def set_example(data: dict[str, dict[str, Any]]) -> None:
    unique_players: set[str] = {name for name in data}
    print(f"Unique players: {unique_players}")
    unique_achmnt: set[str] = {achievement for name in data
                               for achievement in data[name]["achievements"]}
    print(f"Unique achievements: {unique_achmnt}")
    active_regions: set[str] = {data[name]["region"] for name in data
                                if data[name]["active"]}
    print(f"Active regions: {active_regions}")


def combined_example(data: dict[str, dict[str, Any]]) -> None:
    total_players: int = sum([1 for _ in data])
    print(f"Total players: {total_players}")
    total_achievements: int = len({amt for name in data
                                   for amt in data[name]["achievements"]})
    print(f"Total unique achievements: {total_achievements}")
    avg_score: float = sum([data[name]["score"] for name in data])
    avg_score /= total_players
    print(f"Average score: {avg_score:.1f}")
    sorted_perf: list[str] = sorted([name for name in data],
                                    key=lambda x: -data[x]["score"])
    print(f"Top performer: {sorted_perf[0]} "
          f"({data[sorted_perf[0]]['score']} points, "
          f"{len(data[sorted_perf[0]]['achievements'])} achievements)")


def main() -> None:
    data: dict[str, dict[str, Any]] = {
        "alice": {
            "score": 2300,
            "active": True,
            "region": "north",
            "achievements": ['level_10', 'boss_slayer', 'boss_slayer',
                             'boss_slayer', 'boss_slayer']
        },
        "bob": {
            "score": 1800,
            "active": True,
            "region": "east",
            "achievements": ['boss_slayer', 'level_10']
        },
        "charlie": {
            "score": 2150,
            "active": True,
            "region": "central",
            "achievements": ['first_kill']
        },
        "diana": {
            "score": 2050,
            "active": False,
            "region": "north",
            "achievements": ['first_kill']
        }
    }
    print("=== Game Analytics Dashboard ===")
    print("\n=== List Comprehension Examples ===")
    list_example(data)
    print("\n=== Dict Comprehension Examples ===")
    dict_example(data)
    print("\n=== Set Comprehension Examples ===")
    set_example(data)
    print("\n=== Combined Analysis ===")
    combined_example(data)


if __name__ == "__main__":
    main()
