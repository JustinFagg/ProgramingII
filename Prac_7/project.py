"""
project class
"""


class Project:
    """Creates class"""

    def __init__(self, name="", start_date_str="", priority=0, cost_estimate=0, completion_percentage=0):
        """Initialise programing language"""
        self.name = name
        self.start_date_str = start_date_str
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage
        self.start_date = start_date_str.split("/")
        self.start_year = self.start_date[2]
        self.start_month = self.start_date[1]
        self.start_day = self.start_date[0]

    def __repr__(self):
        """repr of programing info"""
        return f"{self.name}\t{self.start_date_str}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"

    def __str__(self):
        """String of programing info"""
        return f"{self.name}, started {self.start_date_str}, priority level {self.priority}, cost around {self.cost_estimate}, {self.completion_percentage}% compleat"

    def __lt__(self, other):
        return int(self.priority) > int(other.priority)

    def is_completed(self):
        return self.completion_percentage == 100

