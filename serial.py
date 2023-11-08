"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Create a serial generator beginning at start."""
        self.start = start
        self.other = start

    def __repr__(self):
        """Show representation."""
        return f"<SerialGenerator start={self.start} next={self.start + 1}"

    def generate(self):
        """Return subsequent values by 1 after beginning at start."""
        self.start += 1
        return self.start - 1

    def reset(self):
        """Reset to the initial start value."""
        self.start = self.other
