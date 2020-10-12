# Cellart <img src="web/frontend/src/logo.svg" width="40" height="40">

*CELLular Automaton for square RooT ~ The Art of Cellular Automata*

Uniform multi-state one-dimensional cellular automata (CA). Cellart attempts to solve the problem of square root calculations using an evolutionary algorithm.

This project consists of three parts:
* cellart - implementation of an evolutionary algorithm.
* cartist - GUI/CLI calculations with the found CA rule sets.
* web - simple React web for square root computation.

## Cellart

C++ program that attempts to find transition functions for square root computation with simple evolutionary algorithm.

### Usage

#### Requirements:

* [CMake](https://cmake.org/)
* C++17

#### Compilation:

```
mkdir build
cd build/
cmake ..
make && make install
cd ..
```

#### Run:

```
./bin/cellart
```

#### Output

During development it prints current generation and fitness when better rule set is found (to `stderr`).

When function with fitness 0 or maximum number of generations is reached, the best rule-set is printed.

#### Config

Edit evolutionary algorithm options in [`config.ini`](config.ini).

### Rule format

Currently, only one format is supported.

#### CSV

```
s1,s2,...,sN,t1
s1,s2,...,sN,t2
```

Each line contains one rule. Each rule describes N states `s` that decide about new state `t` for a cell.

## Cartist

GUI and CLI tools to test/represent the generated transition functions (rule-set).

GUI requires [tkinter](https://docs.python.org/3/library/tkinter.html) installed.

### Run

```
# Run some default automaton (GUI, if tkinter is installed)
./cartist.py

# Runs automaton with the given rule set and computes square root of 36.
./cartist.py -r rule_sets/sq-4-11 36

# CLI version of the above.
./cartist.py -r rule_sets/sq-4-11 -c 36

# CLI version of the above, prints just square root of the given number.
./cartist.py -r rule_sets/sq-4-11 -s 36
```

### Examples

Square root 9, 16 and 25

![cellart9](https://user-images.githubusercontent.com/14038418/115896409-b0caec00-a45b-11eb-873a-cc85c288f33a.png)
![cellart16](https://user-images.githubusercontent.com/14038418/115896004-4ade6480-a45b-11eb-976c-22316485da6d.png)
![cellart25](https://user-images.githubusercontent.com/14038418/115896415-b1fc1900-a45b-11eb-8719-ab967096fdb7.png)


## Credits

This project is extension of my school project at [FIT BUT](https://www.fit.vut.cz/.en) - [Bio-Inspired Computers](https://www.fit.vut.cz/study/course/BIN/.en), inspired by [Evolution of Generic Square Calculations in Cellular Automata](https://www.scitepress.org/PublicationsDetail.aspx?ID=fUDdabZdceo=&t=1) by [Ing. Michal Bidlo, Ph.D.](https://www.fit.vut.cz/person/bidlom/.en).
