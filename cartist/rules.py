"""Representation of CA rule set for SQRT."""

import csv


class RuleSet(dict):
    """Representation of a set of rules.

    Mapping from cell states to new state.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._radius = self._get_radius()
        self._rule_len = self._get_rule_len()

    def get(self, state):
        """Returns new state for the given state."""
        return super().get(state, self._default_state(state))

    @property
    def radius(self):
        return self._radius

    @property
    def rule_len(self):
        return self._rule_len

    def _get_radius(self):
        return None if not self else int(self._get_rule_len() / 2)

    def _get_rule_len(self):
        return None if not self else len(list(self.keys())[0])

    def _default_state(self, state):
        return state[self.radius]


DEFAULT_RULE_SET = RuleSet(
    {
        (0, 1, 1): 0,
        (1, 0, 0): 2,
        (1, 1, 2): 3,
        (1, 2, 2): 1,
        (1, 3, 2): 2,
        (3, 1, 2): 3,
        (3, 3, 2): 2,
    }
)


def get_rule_set_from_csv(csv_file):
    result = {}
    with open(csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                row = [int(num) for num in row]
            except ValueError:
                raise ValueError(f'invalid state value in {row}, integers expected')

            try:
                result[tuple(row[:-1])] = row[-1]
            except IndexError:
                raise IndexError(f'invalid rule: {row}')

    return RuleSet(result)
