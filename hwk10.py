# Name:  - your name (and your partners name) <br>
# Peers:  - names of CSC252 students who you consulted or ``N/A'' <br>
# References:  - URL of resources used <br>
from random import randint

### Part 1: Lumber Mill
def lumberSelection(prices:list, n:int) -> float:
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
    pass

def getNumberOfWays(change_amount:int, bill_list:list) -> int:
	return 0



def main():
    """ This function drives the program and will call each of your functions.
    """
    lumber_prices = [0.25, 1.45, 0, 3.58, 0, 4.4, 0, 5.18, 0, 6.58, 0, 8.28]
    size = randint(1,len(lumber_prices))
    print("The max value for " + str(size) + " feet is $" + str(lumberSelection(lumber_prices, size)))
    
    bills = [1, 2, 5, 10, 20, 50, 100]
    change = randint(1, 100)
    print("For $" + str(change) + " there are " + str(getNumberOfWays(6, bills)) + " combinations.")

if __name__ == '__main__': 
    main()

