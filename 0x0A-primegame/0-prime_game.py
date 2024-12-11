#!/usr/bin/python3
"""
Prime Game Module
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): The number of rounds.
        nums (list): An array of integers where each integer represents
        the value of n for a round.

    Returns:
        str: The name of the player that won the most rounds. If the winner
        cannot be determined, returns None.
    """

    def count_primes(n):
        """
        Counts the number of prime numbers up to n using the Sieve of
        Eratosthenes.

        Args:
            n (int): The upper limit for prime counting.

        Returns:
            int: The number of prime numbers up to n.
        """
        if n < 2:
            return 0
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for current in range(2, int(n**0.5) + 1):
            if sieve[current]:
                for multiple in range(current * current, n + 1, current):
                    sieve[multiple] = False
        return sum(sieve)

    # Handle edge cases
    if x <= 0 or not nums:
        return None  # No rounds or no values in nums

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes(n)
        if prime_count == 0:
            ben_wins += 1  # No primes available, Ben wins by default
        elif prime_count % 2 == 0:
            ben_wins += 1  # Even number of primes, Ben wins
        else:
            maria_wins += 1  # Odd number of primes, Maria wins

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None  # Tie or no clear winner


if __name__ == "__main__":
    isWinner(x, nums)
