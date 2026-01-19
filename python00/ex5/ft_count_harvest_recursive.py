days: int = 0
counter: int = 0


def ft_count_harvest_recursive() -> None:
    global days
    global counter
    if counter == 0:
        days = int(input("Days until harvest: "))
        counter = 1
        ft_count_harvest_recursive()
        print("Harvest time!")
        return
    if counter <= days:
        counter = counter + 1
        print(f"Day {counter - 1}")
        ft_count_harvest_recursive()
