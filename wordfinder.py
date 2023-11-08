"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Returns random words from dictionary (words.txt file)."""

    def __init__(self, path):
        """Reads words.txt and reports number of items read."""

        path = "words.txt"
        file = open(path)
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")

    def parse(self, file):
        """Parse words.txt for a list of words."""

        return [w.strip() for w in file]

    def random(self):
        """Return a random word from words.txt."""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines and comments."""

    def parse(self, file):
        """Parse words.txt for a list of words that skips blanks lines and comments"""

        return [w.strip() for w in file if w.strip() and not w.startswith("#")]
