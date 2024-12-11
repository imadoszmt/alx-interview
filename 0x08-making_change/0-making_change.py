#!/usr/bin/python3
"""
Change Comes From Within Module
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of coin denominations.
        total (int): The target amount to be met.

    Returns:
        int: The fewest number of coins needed to meet the total.
        If the total cannot be met, returns -1.
    """
    if total <= 0:
        return 0

    # Initialize a DP array with infinity for all values except 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0 total

    # Iterate through all amounts from 1 to total
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

# Example usage:
if __name__ == "__main__":
    makeChange(coins, total)
