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

    def sieve(n):
        """
        Generates all prime numbers up to n using the Sieve of Eratosthenes.

        Args:
            n (int): The upper limit for prime generation.

        Returns:
            list: A list of prime numbers up to n.
        """
        if n < 2:
            return []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for current in range(2, int(n**0.5) + 1):
            if sieve[current]:
                for multiple in range(current * current, n + 1, current):
                    sieve[multiple] = False
        return [num for num, is_prime in enumerate(sieve) if is_prime]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = sieve(n)
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    isWinner(x, nums)
