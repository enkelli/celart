#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <vector>

#include <INIReader.hpp>

#include "ca.hpp"
#include "rules.hpp"
#include "utils.hpp"


constexpr auto CONFIG_FILE = "config.ini";

std::vector<int> INIT_CA = {
	9,
	16,
	25,
	36,
	49,
};


int main(int args, char* argv[]) {
	INIReader reader(CONFIG_FILE);
	if (reader.ParseError() < 0) {
		std::cerr << "Can't load config file '" << CONFIG_FILE << "'\n";
		return 1;
	}
	int population_size = reader.GetInteger("ecosystem", "population_size", 8);
	int max_generations = reader.GetInteger("ecosystem", "max_generations", 1000000);
	int rules_perc_to_mutate = reader.GetInteger("ecosystem", "rules_perc_to_mutate", 10);
	int state_count = reader.GetInteger("automata", "state_count", 4);
	int radius = reader.GetInteger("automata", "radius", 1);
	int max_development_loops = reader.GetInteger("automata", "max_development_loops", 10);
	int cells_in_rule = radius * 2 + 1;

	std::srand (std::time(NULL));

	int best = 10000000;
	auto rules = RuleSets();
	for (int i = 0; i < population_size; ++i) {
		rules.push_back(RuleSet(cells_in_rule, state_count));
	}
	RuleSet best_rule = rules[0];
	std::vector<CASqrt> cas;
	for (int i : INIT_CA) {
		cas.push_back(CASqrt(i, radius));
	}
	for (int i = 0; (i < max_generations || max_generations == 0) && best != CASqrt::BEST_FIT; ++i) {
		int local_best = 100000000;
		RuleSet local_best_rule = rules[0];

		for (const auto& rule_set : rules) {
			int fit = 0;
			for (auto& ca : cas) {
				ca.develop(rule_set, max_development_loops);
				fit += ca.fitness();
				ca.init();
			}
			if (fit <= best) {
				if (fit < best) {
					std::cerr << "Generation: " << i << ", fitness: " << fit << "\n";
				}
				best = fit;
				best_rule = rule_set;
			}
			if (fit <= local_best) {
				local_best = fit;
				local_best_rule = rule_set;
			}
		}
		if ((i % 4096) == 0) {
			std::cerr << "Generation: " << i << ", fitness: " << best << "\n";
		}
		rules.clear();
		for (int i = 0; i < population_size; ++i) {
			rules.push_back(local_best_rule.mutated(rules_perc_to_mutate));
		}
	}
	best_rule.print();

	return 0;
}
