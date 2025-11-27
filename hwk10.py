# Name:  - your name (and your partners name) <br>
# Peers:  - names of CSC252 students who you consulted or ``N/A'' <br>
# References:  https://www.geeksforgeeks.org/dsa/coin-change-dp-7/<br>
from random import randint

### Part 1: Lumber Mill
def lumberSelection(prices:list, n:int) -> float:
    '''
    Returns the max best price for a board of length n and prices[] as prices of different lengths.

    :param prices: (list) list of prices of different length 
    :param n: (int) board length 
    :return: (float) Max price of the board
    
    >>> lumber_prices = [0.25, 1.45, 0, 3.58, 0, 4.4, 0, 5.18, 0, 6.58, 0, 8.28]
    >>> print(lumberSelection(lumber_prices, 8))
    7.16
    '''
    # Make an nxn matrix -> time : O(n), space: O(n^2)
    m = [0] * (n+1)
    for i in range(0,n+1):
        row = [0] * (n+1)
        m[i] = row

    # Fill matrix -> time : O(n^2)
    for i in range(1, n+1): 
        row_value = prices[i-1]
        for j in range(1, n+1):
            if i > j:                   # If the row < column, carry value from directly above
                m[i][j] =  m[i-1][j]
            else:
                if j % i == 0:          # If the column is divisible by the row, calculate price
                    m[i][j] = (j/i) * row_value       
                else:                   # If the column is not divisible by the row, determine price of remainder 
                    m[i][j] = (j//i * row_value) + m[i][j//i]

    max = m[n][n]                       # Current max is corner of grid
    col = n-1                       
    curr = m[n][col]
    while col != 0:
        total = 0
        if n % col == 0:                # If the n is divisible by column, determine price by multiplying
            total = curr * n/col
        else:
            total += curr + m[i][n-col] # Otherwise find remainder, determine price
        if total > max:                 # If bigger than max replace
            max = total
        col-=1                          # Increment counters
        curr = m[n][col]
    return max

### Part 2: Cash Register
def calcPermutations(val:int) -> None:
    '''
    Prints out all possible combinations of val 
    :param val: (int) integer value to calculate the permutations
    
    >>> calcPermutations(12)
    111111111111 
    11111111112 
    1111111122 
    111111222 
    11112222 
    1122222 
    222222 
    11111115 
    1111125 
    111225 
    12225 
    1155 
    255 
    1110 
    210 
    '''
    bills = [1, 2, 5, 10, 20, 50, 100]
    m = {} # a set to keep track of all possible combinations
    for i in range(0, val + 1):
        m[i] = []

    m[0] = [[]]

    for bill in bills:
        for i in range(1, val + 1):
            if i - bill >= 0:
                for lst in m[i - bill]:
                    m[i].append(lst + [bill])

    for combos in m[val]: 
        for j in combos: 
            print(j, end="")
        print(" ")

# helper function for calc Permutations
def append(l:list, item:int) -> list: 
    '''
    Appending items into the list 

    :param l: (list) list to append items to
    :param item: (int) int item to append to list 
    :return: (list) New list with appended item 

    >>> l = [1, 2]
    >>> print(append(l, 3))
    [1, 2, 3]
    '''
    n_arr = [0] * (len(l) + 1) 

    # copy the items from old array to new 
    for i in range(0, len(l)): 
        n_arr[i] = l[i]
        
    # add the appended item to the end
    n_arr[len(l)] = item

    return n_arr


def getNumberOfWays(change_amount:int, bill_list:list) -> int:
    '''
    Returns the number of ways to make combinatinos of change_amount using values in bill_list

    :param change_amount: (int) The value to calculate the number of ways 
    :param bill_list: (list) list of values to calculate the number of combinations of change_amount
    :return: (int) The number of combinations for change_amount using only values in bill_list

    >>> calcPermutations(12)
    111111111111 
    11111111112 
    1111111122 
    111111222 
    11112222 
    1122222 
    222222 
    11111115 
    1111125 
    111225 
    12225 
    1155 
    255 
    1110 
    210 
    '''
    m = [0] * (change_amount + 1) # array 
    m[0] = 1
    
    for bill in bill_list: # for each value in bill 
        for i in range(1, change_amount + 1):
            if i - bill >= 0: #
                m[i] += m[i - bill] # need to include possible repeated combos subpart (ex: 5 5 2 -> 5 5 1 1)
            
    return m[change_amount]


def main():
    """ This function drives the program and will call each of your functions.
    """
    lumber_prices = [0.25, 1.45, 0, 3.58, 0, 4.4, 0, 5.18, 0, 6.58, 0, 8.28]
    size = randint(1,len(lumber_prices))
    print("The max value for " + str(size) + " feet is $" + str(lumberSelection(lumber_prices, size)))
    

    bills = [1, 2, 5, 10, 20, 50, 100]
    change = randint(1, 100)
    print("For $" + str(change) + " there are " + str(getNumberOfWays(4, bills)) + " combinations.")

    calcPermutations(12)

if __name__ == '__main__': 
    main()

