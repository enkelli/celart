///
/// @file
/// CA Rules.
///

#pragma once

#include <cstdlib>
#include <unordered_map>
#include <vector>

#include "cell.hpp"

class RuleSet {
public:
	RuleSet() = default;
	RuleSet(int cell_count, int state_count);

	void initRandom();

	void mutate(int rules_perc_to_mutate);
	RuleSet mutated(int rules_perc_to_mutate);
	int get(const std::vector<int> &key) const;

	void print() const;

private:
	struct rule_hash {
		std::size_t operator() (const std::vector<Cell> &rule_cells) const {
			std::size_t result = 0;
			for (int state : rule_cells) {
				result = result * 10 + state;
			}

			return result;
		}
	};

private:
	std::vector<std::vector<Cell>> rules_mutation_index;
	std::unordered_map<std::vector<Cell>, int, rule_hash> rules_map;

	int cell_count;
	int state_count;
	std::size_t rule_count;
};

using RuleSets = std::vector<RuleSet>;
