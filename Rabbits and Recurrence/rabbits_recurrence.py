"""
Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, 
if we begin with 1 pair and in each generation, every pair of reproduction-age
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

    Assumptions:
        1. The population begins in the first month with a pair of newborn rabbits.
        2. Rabbits reach reproductive age after one month.
        3. In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
        4. Exactly one month after two rabbits mate, they produce one male and one female rabbit.
        5. Rabbits never die or stop reproducing.
 """

def rabbits(n, k):
    prev1 = 1
    prev2 = 1
    for months in range(2, n):
        cur = prev1 + k * prev2
        prev2 = prev1
        prev1 = cur
    return cur

if __name__ == '__main__':
    n = 35
    k = 5
    result = rabbits(n, k)
    with open('results.txt', 'w') as file:
        file.write(str(result))