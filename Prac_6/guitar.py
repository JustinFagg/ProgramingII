"""
guitar class
Estimate: 40 minutes
Actual: 57 minutes
"""

CURRENT_YEAR = 2022


class Guitar:
    """Creates class"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise programing language"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """String of programing info"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Returns age of guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returns true if is older than 50"""
        if self.get_age() >= 50:
            return True
        else:
            return False

    def __lt__(self, other):
        return int(self.year) < int(other.year)
