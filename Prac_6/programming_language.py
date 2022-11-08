"""
programming_language class
Estimate: 60 minutes
Actual: 25 minutes
"""


class ProgrammingLanguage:
    """Creates class"""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise programing language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """String of programing info"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Returns true if self is dynamic"""
        if self.typing == "Dynamic":
            return True
        else:
            return False
