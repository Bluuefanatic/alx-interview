#!/usr/bin/python3
"""Prime Game - Determine the winner after multiple rounds."""


def sieve_of_eratosthenes(n):
    """Return a list of prime numbers up to n using Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def count_primes(n, primes):
    """Count how many primes exist up to n."""
    count = 0
    for prime in primes:
        if prime > n:
            break
        count += 1
    return count


def isWinner(x, nums):
    """
    Determine the winner of x rounds of the Prime Game.
    Maria plays first, Ben plays second, both play optimally.
    Args:
        x (int): the number of rounds.
        nums (list of int): list of n values for each round.
    Returns:
        str: name of the player who won the most rounds or None if tie.
    """
    if not nums or x < 1:
        return None

    # Find the maximum number in nums to compute all primes up to that point
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes(n, primes)
        # Maria wins if the number of primes is odd, Ben wins if even
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
