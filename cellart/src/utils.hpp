///
/// @file
/// Utilities.
///

#pragma once

#include <string>
#include <string_view>


///
/// Converts the given container to string. Items are separated with the
/// delimiter.
///
template <typename Container>
std::string join_container(const Container &container,
		std::string_view delimiter = ",") {
	std::string s;
	for(std::size_t i = 0; i < container.size(); ++i)
	{
		if(i != 0) {
			s += delimiter;
		}
		s += std::to_string(container[i]);
	}
	return s;
}

