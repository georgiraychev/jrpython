# Python Developer Interview Task

Welcome to your coding interview! This is a hands-on assessment of your Python programming skills.

## Environment Setup

This repository uses GitHub Codespaces, which provides you with a complete development environment in the browser.

### Getting Started with Codespaces

1. Click the green "Code" button above
2. Select "Create codespace on main"
3. Wait for the environment to set up (this takes about 2 minutes)

### Using the Codespace

- **Terminal**: Access via Menu -> Terminal -> New Terminal, or press `` Ctrl+` ``
- **File Explorer**: Click the Explorer icon in the left sidebar or press `Ctrl+Shift+E`
- **Running Tests**: In the terminal, you can run:
  - All tests: `pytest`
  - Specific test file: `pytest tests/test_python_basics.py`
  - With output: `pytest -v`
  - Single test: `pytest tests/test_python_basics.py::test_string_manipulator`

## Tasks

You have 90 minutes to complete the following tasks:

### 1. Python Basics (30 minutes)
- Fix the string manipulation methods in `interview/python_basics.py`
- Fix the data structure implementations
- Run tests with: `pytest tests/test_python_basics.py`

### 2. PySpark Problems (30 minutes)
- Fix the PySpark transformations in `interview/spark_problems.py`
- Focus on correct DataFrame operations
- Run tests with: `pytest tests/test_spark_problems.py`

### 3. SQL Problems (30 minutes)
- Fix the SQL queries in `interview/sql_problems.py`
- Ensure proper joins, aggregations, and filtering
- Write clear and efficient queries

## Evaluation Criteria

You will be evaluated on:
- Code correctness (all tests passing)
- Code clarity and style
- Problem-solving approach
- Understanding of Python, PySpark, and SQL concepts

## Tips

- Read the test files to understand what each function should do
- Use `print()` statements for debugging
- Check the Python documentation when needed
- Commit your changes regularly
- Focus on making the tests pass first, then improve the code if time permits

## File Structure

All the code you need to modify is in the `interview/problem.py` file.
The tests in `tests/test_calculator.py` will help you understand what needs to be fixed.

Good luck! 