class Counter:
    def __init__(self, count):
        """Initializes data members for Counter class."""
        self._count = 0

    def get_count(self):
        """Returns current life count."""
        return self._count

    def set_count(self, new_count):
        """Sets the life count."""
        self._count = new_count

    def increment(self, amt = 1):
        """Adds one to the current life count."""
        self._count += amt

    def decrement(self, amt = 1):
        """Subtracts one from the current life count."""
        self._count -= amt

class CommanderCounter:
    def __init__(self, commander_count):
        """Initializes data members for CommanderCounter class."""
        self._commander_count = 0

    def get_commander_count(self):
        """Returns current life count."""
        return self._commander_count

    def set_commander_count(self, new_count):
        """Sets the life count."""
        self._commander_count = new_count

    def increment(self, amt = 1):
        """Adds one to the current life count."""
        self._commander_count += amt

    def decrement(self, amt = 1):
        """Subtracts one from the current life count."""
        self._commander_count -= amt