///
/// @file
/// Cellular Automaton.
///

#include <iostream>
#include <cmath>

#include "ca.hpp"

const std::size_t CASqrt::BEST_FIT = 0;


CASqrt::CASqrt(int init_value, int radius) : radius(radius), value(init_value) {
	// Add empty cells to both sides of the size 2 * radius + 1 => number
	// of cells that is used to choose new state.
	rule_size = 2 * radius + 1;
	null_cells = rule_size;
	cell_count = value + null_cells * 2;
	target = std::sqrt(value);
	init();
}


void CASqrt::init() {
	cells.clear();
	for (int i = 0; i < null_cells; ++i) {
		cells.push_back(0);
	}
	for(int i = 0; i < value; ++i) {
		cells.push_back(1);
	}
	for (int i = 0; i < null_cells; ++i) {
		cells.push_back(0);
	}
}

void CASqrt::develop(const RuleSet &rules, int development_loops) {
	steps = 0;
	auto next_cells = cells;
	int loops = 0;
	bool stable = false;
	do {
		steps++;
		loops++;
		for (std::size_t i = 0; i < cell_count; ++i) {
			auto states = get_states(i, cells);
			auto next = rules.get(states);
			next_cells[i] = next;
		}
		if (cells == next_cells) {
			steps--;
			stable = true;
		}
		prev_cells = cells;
		cells = next_cells;
	} while (!stable && loops < development_loops);
}

int CASqrt::fitness() const {
	int maxf = 0;
	bool seq = false;
	bool after = false;
	int redund = 0;

	// First and last cell should be 0, penalty otherwise.
	if (cells[0] != 0) {
		redund++;
	}
	if (prev_cells[0] != 0) {
		redund++;
	}
	if (cells[cell_count - 1] != 0) {
		redund++;
	}
	if (prev_cells[cell_count - 1] != 0) {
		redund++;
	}
	for (std::size_t i = 1; i < cell_count - 1; ++i) {
		int val = cells[i];
		if (cells[i] != prev_cells[i]) {
			redund++;
		}
		if (after) {
			if (val != 0) {
				redund++;
			}
		} else {
			if (val == 0 && seq) {
				seq = false;
				after = true;
			} else if ((val != 0 ) && (i == (cell_count - 1))) {
				maxf++;
			} else if (val == 0) {
				continue;
			} else {
				seq = true;
				maxf++;
			}
		}
	}
	auto res = (maxf - target) > 0 ? maxf - target : target - maxf;
	res += redund;
	return res;
}

CASqrt::Row CASqrt::get_states(int middle, const Row &cells) const {
	Row res;
	res.reserve(rule_size);

	int left_start = middle - radius;
	while (left_start < 0) {
		res.emplace_back(0);
		left_start++;
	}

	for (int i = left_start; i <= (middle + radius); ++i) {
		if (i >= cell_count) {
			res.emplace_back(0);
		} else {
			res.emplace_back(cells[i]);
		}
	}

	return res;
}

void CASqrt::print() const {
	std::cout << join_container(cells, " ") << "\n";
}
