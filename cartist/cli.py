"""
    Cellular Automata ARTIST in CLI.
"""

import random
import string

from cartist import Artist
from cartist.ca import SqrtCA
from cartist.rules import DEFAULT_RULE_SET


class CLIArtist(Artist):
    """Cellular Automata artist in CLI.

    :param dict rule_set: Rule set used in cellular automaton.
    :param int number: Number to be squared.
    :param bool random_chars: Use random characters for each run?
    """

    _chars = string.punctuation + string.ascii_letters + string.digits
    _random_chars = random.sample(_chars, len(_chars))

    def __init__(self, number, rule_set=DEFAULT_RULE_SET, random_chars=True):
        super().__init__(number, rule_set)

        self._use_random_chars = random_chars

    def paint(self):
        """Prints CA generations to the console for the given value and rule
        set.
        """
        while True:
            self._draw_row()
            self._ca.evolve()
            if not self._ca.has_changed():
                self._draw_row()
                print(f'√{self._ca.number}: {self._ca.sqrt_value}')
                break

    def _draw_row(self):
        row = ''
        for state in self._ca:
            row += self._get_char_for_state(state)
        print(row)

    def _get_char_for_state(self, state):
        return (
            self._random_chars[state] if self._use_random_chars else self._chars[state]
        )
