///
/// @file
/// Cellular Automaton.
///

#pragma once

#include <vector>

#include "cell.hpp"
#include "rules.hpp"
#include "utils.hpp"


class CASqrt {
private:
	using Row = std::vector<Cell>;

public:
	CASqrt(int init_value, int radius);

	void init();

	void develop(const RuleSet &rules, int development_loops);
	int fitness() const;
	Row get_states(int middle, const Row &cells) const;

	void print() const;

public:
	static const std::size_t BEST_FIT;

private:
	std::size_t cell_count;
	int null_cells;
	int rule_size;
	std::size_t radius;
	int steps;
	int value;
	int target;
	std::vector<Cell> cells;
	std::vector<Cell> prev_cells;
};
