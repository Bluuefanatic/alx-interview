#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    :param coins: List[int] - available coin denominations
    :param total: int - the total amount to meet
    :return: int - the fewest number of coins needed, or -1 if it's impossible
    """
    if total <= 0:
        return 0
    
    # Initialize dp array with infinity (a large number)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make 0
    
    # Process each amount from 1 to total
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, return -1 (impossible to make total)
    return dp[total] if dp[total] != float('inf') else -1
