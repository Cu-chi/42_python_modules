def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def recursive(day):
        print(f"Day {day}")
        if day >= days:
            print("Harvest time!")
            return
        recursive(day + 1)

    recursive(1)
