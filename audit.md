# README Audit Table

| Claim made in README | True? | Evidence or correction made |
| :--- | :---: | :--- |
| Requires `pip install -r requirements.txt` | No | No `requirements.txt` exists; standard library only. Delete the line. |
| Repository title is `Python-basics-25BCON1802` | Yes | Verified from GitHub repository page title and URL. |
| Contains `dictionary.py` | Yes | Verified file exists in repository root folder. |
| Contains `factorial.py` | Yes | Verified file exists in repository root folder. |
| Contains `fibonacci.py` | Yes | Verified file exists in repository root folder. |
| Requires Python 3.x | Yes | All `.py` scripts use Python 3 standard syntax. |
| Commands run directly via `python <script_name>.py` | Yes | No external dependencies or build steps needed. |
## Peer Repository Review
I recently shared my repository with CHHAVI AGGARWAL and she provided me some needed claims and fixes.
### 1. Repository Overview
The repository contains beginner-friendly Python programs demonstrating dictionaries, factorial calculation, and Fibonacci sequence generation.

### 2. Verified Claims
- `dictionary.py` exists and demonstrates dictionary key-value pairs.
- `factorial.py` calculates the factorial of a fixed number.
- `fibonacci.py` generates the first 10 Fibonacci numbers.
- The programs use Python 3 and standard Python features only.

### 3. Review of Code
- The programs are simple and suitable for beginners.
- The code is readable and easy to understand.
- The programs run without external dependencies.

### 4. Specific Improvement
In `factorial.py`, replace the fixed value `n=5` with user input so the program can calculate the factorial of any number.

Example:
```python
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial of", n, "=", fact)
