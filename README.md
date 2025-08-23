# Python Discovery Piscine

Welcome to the **Python Discovery Piscine**!  
This repository is a collection of beginner-friendly Python exercises designed for students at 42 Prague. The main goal is to introduce you to the basics of Python programming through practical, hands-on tasks.

## Overview

This repository is structured as a series of "cells," each containing several exercises. The progression goes from very basic Python concepts (like printing, variables, input/output, and control flow) to more advanced topics (like functions, working with arrays/lists, and dictionaries).

The exercises are inspired by the 42 Piscine methodology: learning by doing, with an emphasis on experimentation and self-discovery.

---

## Structure

- Each main directory (`cellXX`) represents a module or topic.
- Each sub-directory (`exYY`) contains a specific exercise.
- Exercises range from simple scripts (like checking if a number is zero) to more complex problems (working with arrays, dictionaries, or string manipulation).

Example directories:
```
cell02/
  ex00/  # Check if a number is zero
  ex02/  # Simple password checker
cell05/
  ex03/  # Remove duplicates from an array
  ex07/  # Lowercase string manipulation
cell07/
  ex00/  # Working with dictionaries and names
```

---

## Example Exercises

- **iszero.py**: Checks if the user input is zero.
- **password.py**: Simple password validation.
- **play_with_arrays.py**: Array/list processing and set operations.
- **downcase_it.py**: Converts input strings to lowercase.
- **append_it.py**: Appends 'ism' to given parameters unless they already end with 'ism'.
- **scope_that.py**: Demonstrates the concept of variable scope and function definitions.
- **your_namebook.py**: Combines first and last names from a dictionary.

---

## Running the Exercises

Most scripts are executable Python files. You can run them from the command line:

```bash
./cell02/ex00/iszero.py
```
or
```bash
python3 cell07/ex00/your_namebook.py
```

Some scripts may expect command-line arguments or user input.

---

## Who is this for?

- **42 Prague students** interested in learning Python from scratch.
- Anyone looking for a structured, hands-on introduction to Python basics.

---

## Notes

- Some scripts use terminal color codes for fun and to make outputs more readable.
- Many exercises include comments and sample usage to guide you.
- The repository is focused on learning and experimentation—code quality or "pythonic" style may be secondary to educational value.

---

## License

For educational use at 42 Prague.  
Feel free to fork and use for your own learning!

---

-------------------------------------


ORANGE      = \033[38;5;222m

GREEN_BR    = \033[38;5;118m

YELLOW_BR   = \033[38;5;227m

PINK_BR     = \033[38;5;206m

BLUE_BR     = \033[38;5;051m

PINK_BRR    = \033[38;5;219m
