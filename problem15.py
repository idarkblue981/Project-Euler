"""
Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20 x 20 grid?
"""


from math import factorial

def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def number_of_routes(grid_size):
    return binomial_coefficient(2 * grid_size, grid_size)

if __name__ == "__main__":
    grid_size = 20
    result = number_of_routes(grid_size)
    print(result)