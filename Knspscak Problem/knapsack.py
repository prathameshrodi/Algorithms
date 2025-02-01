"""

"""

def knapsack(values, weights, capacity):
    """
    Solve the 0/1 Knapsack problem with optimized space complexity.

    Args:
        values (list[int]): List of item values.
        weights (list[int]): List of item weights.
        capacity (int): Maximum capacity of the knapsack.

    Returns:
        int: Maximum value that can be obtained.
    """
    n = len(values)
    # Use a 1D DP array for optimized space complexity
    dp = [0] * (capacity + 1)

    # Build the table in a bottom-up manner
    for i in range(n):
        # Traverse in reverse to avoid overwriting previous states
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]

# Example usage
if __name__ == "__main__":
    values = [24, 18, 31, 45, 78, 98, 35, 55]
    weights = [5, 8, 7, 10, 15, 18, 9, 14]
    capacity = 30

    max_value = knapsack(values, weights, capacity)
    print(f"Maximum value in knapsack of capacity {capacity}: {max_value}")