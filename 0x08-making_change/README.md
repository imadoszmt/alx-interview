# Change Comes From Within

## Description

This project tackles the classic **Coin Change Problem** using dynamic programming. The challenge is to determine the minimum number of coins required to make up a given total amount from a set of available coin denominations. If it's impossible to create the total using the given coins, the function returns `-1`.

## Problem Statement

Given a list of coin denominations and a target total, find the fewest number of coins needed to meet that total. The solution requires an efficient algorithmic approach that handles various coin combinations.

## Prototype Function

```python
def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of coin denominations.
        total (int): The target amount to be met.

    Returns:
        int: The fewest number of coins needed to meet the total. If the total cannot be met, returns -1.
    """
```

## Examples

```python
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

## Requirements

- **Editors**: vi, vim, emacs
- **Interpreter/Compiler**: Python 3 (version 3.4.3) on Ubuntu 20.04 LTS
- **File Ending**: All files must end with a new line
- **Shebang**: First line of all files should be `#!/usr/bin/python3`
- **Code Style**: Follows PEP 8 style guide (version 1.7.x)
- **Executable**: All files must be executable

## Key Concepts

### 1. Greedy Algorithms
- Understanding the principles of greedy algorithmic approaches
- Recognizing the limitations of greedy strategies in solving complex optimization problems

### 2. Dynamic Programming
- Solving problems by breaking them down into simpler subproblems
- Utilizing memoization to store and reuse previous computational results
- Handling overlapping subproblems efficiently

### 3. Algorithmic Complexity
- Analyzing time and space complexity
- Developing solutions that are computationally efficient
- Balancing between solution accuracy and performance

### 4. Python Programming
- Effective use of lists and data structures
- Implementing control flow with loops and conditional statements
- Writing clean, readable, and efficient Python code

## Solution Approach

The solution to the Coin Change Problem typically involves:

1. **Dynamic Programming Strategy**
   - Create a dynamic programming table to store minimum coin counts
   - Initialize the table with base cases
   - Build solutions for larger totals using solutions to smaller subproblems

2. **Optimization Techniques**
   - Minimize the number of coins used
   - Handle cases where the total cannot be met
   - Efficiently explore different coin combinations

3. **Edge Case Handling**
   - Manage scenarios with various coin denominations
   - Return `-1` when no valid combination exists
   - Account for different total amounts

## Recommended Learning Resources

### Dynamic Programming
- [GeeksforGeeks: Dynamic Programming](https://www.geeksforgeeks.org/dynamic-programming/)
- [Coursera: Dynamic Programming Courses](https://www.coursera.org/courses?query=dynamic%20programming)

### Coin Change Problem
- [LeetCode: Coin Change Problem](https://leetcode.com/problems/coin-change/)
- [HackerRank: Coin Change Tutorials](https://www.hackerrank.com/topics/dynamic-programming)

### Python Programming
- [Python Official Documentation](https://docs.python.org/3/tutorial/)
- [Real Python: Dynamic Programming](https://realpython.com/tutorials/dynamic-programming/)
