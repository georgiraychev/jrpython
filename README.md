# Python Developer Interview Task

Welcome to your coding interview! This is a hands-on assessment of your Python programming skills.

## Environment Setup

This repository uses GitHub Codespaces with an integrated SQLite database.

### Initial Setup

1. Open a terminal in Codespaces
2. Initialize the database:
   ```bash
   python -m interview.services.db_init
   ```
3. Verify the database:
   ```bash
   sqlite3 data/interview.db
   ```
   Try some queries:
   ```sql
   .tables
   SELECT * FROM products LIMIT 3;
   .quit
   ```

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

### 1. SQL Command Line Task (20 minutes)
Using the SQLite command line:
1. Find all products with price > $100
2. Calculate total revenue per category
3. Find users who made more than 1 order

### 2. Python & SQL Integration (40 minutes)
Fix the implementations in:
- `interview/sql_problems.py`
- `interview/data_analyzer.py`

The tasks are interconnected - the SQL queries you write will be used by the Python analysis functions.

### 3. Data Analysis (30 minutes)
Implement the analysis functions in `data_analyzer.py` that combine:
- SQL queries
- Python data processing
- Business logic

## Evaluation Criteria

You will be evaluated on:
- SQL query optimization
- Python data processing efficiency
- Understanding of database relationships
- Code organization and clarity
- Problem-solving approach

## Tips

- Use `sqlite3 data/interview.db` to explore the database
- Useful SQLite commands:
  - `.tables` - list all tables
  - `.schema table_name` - show table structure
  - `.mode column` - pretty print results
  - `.headers on` - show column headers
- Test your SQL queries in the command line before implementing them in Python
- Consider the relationships between tables when writing queries
- Commit your changes regularly
- Focus on making the tests pass first, then improve the code if time permits

## File Structure

All the code you need to modify is in the `interview/problem.py` file.
The tests in `tests/test_calculator.py` will help you understand what needs to be fixed.

Good luck! 