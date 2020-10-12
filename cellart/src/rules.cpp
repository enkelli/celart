///
/// @file
/// CA Rules.
///

#include <iostream>

#include "rules.hpp"
#include "utils.hpp"

RuleSet::RuleSet(int cell_count, int state_count) :
		cell_count(cell_count),
		state_count(state_count) {
	rule_count = 1;
	for (int i = 0; i < cell_count; ++i) {
		rule_count *= state_count;
	}
	initRandom();
}

void RuleSet::initRandom() {
	do {
		std::vector<int> states;
		for (int j = 0; j < cell_count; ++j) {
			states.push_back(std::rand() % state_count);
		}
		int next_state = std::rand() % state_count;
		rules_map[states] = next_state;
	} while (rules_map.size() < rule_count);

	for (const auto& [key, _] : rules_map) {
		rules_mutation_index.push_back(key);
	}
}

void RuleSet::mutate(int rules_perc_to_mutate) {
	//int rule_to_mutate_count = rule_count * rules_perc_to_mutate / 100;
	//for (int i = 0; i < rule_to_mutate_count; ++i) {
	//	int position = std::rand() % rule_count;
	//	int next_state = std::rand() % state_count;
	//	rules_map[rules_mutation_index[position]] = next_state;
	//}

	//// Neutralize some rules.
	//for (int i = 0; i < rule_to_mutate_count; ++i) {
	//	const int position = std::rand() % rule_count;
	//	const auto state = rules_map[rules_mutation_index[position]];
	//	rules_map[rules_mutation_index[position]] = state;
	//}

	for (const auto& [rule,state] : rules_map) {
		int number = std::rand() % rule_count;
		if (number < rules_perc_to_mutate) {
			int next_state = std::rand() % state_count;
			rules_map[rule] = next_state;
		}
		else if (number < (rules_perc_to_mutate * 2)) {
			rules_map[rule] = rule[1];
		}

	}
}

RuleSet RuleSet::mutated(int rules_perc_to_mutate) {
	auto newRuleSet = *this;
	newRuleSet.mutate(rules_perc_to_mutate);
	return newRuleSet;

}

int RuleSet::get(const std::vector<int> &key) const {
	return rules_map.find(key)->second;
}

void RuleSet::print() const {
	for (const auto & r : rules_map) {
		if (r.first[1] != r.second) {
			std::cout << join_container(r.first) << "," << r.second << "\n";
		}
	}
}
