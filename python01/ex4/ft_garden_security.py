class SecurePlant:
    """A SecurePlant class
    """
    def __init__(self, name: str, height: int, age: int):
        """Initialize a SecurePlant object

        Args:
            name (str): Name of the plant
            height (int): Height of the plant
            age (int): Age of the plant
        """
        print("Plant created: " + name)
        self.__name = name
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int):
        """Set height of the plant

        Args:
            height (int): height of the plant
        """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm "
                  "[REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = height
        print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int):
        """Set age of the plant

        Args:
            age (int): age of the plant
        """
        if age < 0:
            print(f"Invalid operation attempted: age {age} days "
                  "[REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__age = age
        print(f"Age updated: {age} days [OK]")

    def get_height(self):
        """Get height of the plant

        Returns:
            int: height of the plant
        """
        return self.__height

    def get_age(self):
        """Get age of the plant

        Returns:
            int: age of the plant
        """
        return self.__age

    def get_info(self):
        """print info of the plant
        """
        print(f"Current plant: {self.__name} ({self.__height}cm, {self.__age} "
              "days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(-10)
    rose.set_age(-5)
    rose.set_height(26)
    rose.set_age(31)
    rose.get_info()
