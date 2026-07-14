def knapsack_recursive(weights, value, capacity, n):
    if n == 0 or capacity == 0:
        return 0

    if weights[n - 1] > capacity:
        return knapsack_recursive(weights, value, capacity, n - 1)

    include = value[n - 1] + knapsack_recursive(
        weights, value, capacity - weights[n - 1], n - 1)

    exclude = knapsack_recursive(weights, value, capacity, n -1)

    return max(include, exclude)