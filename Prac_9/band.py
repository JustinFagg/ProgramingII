"""Band class for CP1404"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with musician."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.members})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, member):
        """Add a musician to bands collection."""
        self.members.append(member)

    def play(self):
        """Return a string showing the instrument playing their first (or no) instrument."""
        if not self.members:
            return f"{self.name} needs a member!"
        return f"{self.name} is playing: {self.members[0]}"


