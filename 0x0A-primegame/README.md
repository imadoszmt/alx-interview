# Prime Game

## Description

The Prime Game is a strategic number game played between Maria and Ben. In each round, players take turns selecting prime numbers from a set of consecutive integers ranging from 1 to n. After choosing a prime number, the player removes that number and all of its multiples from the set. The player who cannot make a move loses the game. The objective is to determine which player wins the most rounds when both players play optimally.

## Game Rules

- The game is played over multiple rounds.
- Players take turns selecting prime numbers.
- After selecting a prime number, the player removes the number and all of its multiples from the set.
- The player who cannot make a move loses the round.

## Prototype Function

```python
def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): The number of rounds.
        nums (list): An array of integers where each integer represents the value of n for a round.

    Returns:
        str: The name of the player that won the most rounds. If the winner cannot be determined, returns None.
    """
```

## Example

```python
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))  # Output: Ben
```

## Requirements

- **Editors**: vi, vim, emacs
- **Interpreter/Compiler**: Python 3 (version 3.4.3) on Ubuntu 20.04 LTS
- **File Ending**: All files should end with a new line
- **Shebang**: First line of all files should be `#!/usr/bin/python3`
- **Code Style**: Follows PEP 8 style guide (version 1.7.x)
- **Executable**: All files must be executable

## Concepts Involved

1. **Prime Numbers**
   - Understanding prime number identification
   - Efficient algorithms for finding prime numbers

2. **Sieve of Eratosthenes**
   - Efficient algorithm for finding prime numbers up to a given limit

3. **Game Theory**
   - Principles of competitive games
   - Optimal play strategies
   - Win condition determination

4. **Dynamic Programming/Memoization**
   - Using previous results to optimize calculations
   - Efficient problem-solving approach

5. **Python Programming**
   - Loops and conditional statements
   - Array and list manipulation
   - Game logic implementation

## Solution Approach

The solution involves a comprehensive strategy to determine the game's winner:

1. **Prime Number Identification**
   - Utilize the Sieve of Eratosthenes to find prime numbers
   - Efficiently identify primes up to n for each round

2. **Game Simulation**
   - Simulate the game by alternately removing prime numbers
   - Track removals of prime numbers and their multiples

3. **Win Counting**
   - Count wins for Maria and Ben across all rounds
   - Keep track of successful moves and game outcomes

4. **Result Determination**
   - Determine the player with the most wins
   - Handle scenarios where a clear winner cannot be identified

## Recommended Learning Resources

### Prime Numbers and Sieve of Eratosthenes
- [Khan Academy: Prime Numbers](https://www.khanacademy.org/math/pre-algebra/pre-algebra-prime-and-composite/pre-algebra-prime-numbers/a/prime-numbers-review)
- Sieve of Eratosthenes in Python tutorials

### Game Theory
- Introductory Game Theory resources
- Competitive game strategy guides

### Dynamic Programming
- Python-specific Dynamic Programming tutorials
- Memoization techniques

### Python Documentation
- [Python Lists Official Documentation](https://docs.python.org/3/tutorial/introduction.html#lists)

